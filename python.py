import cv2
import mediapipe as mp
from collections import deque, Counter
import time

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

# Start webcam
cap = cv2.VideoCapture(0)

# Landmarks: corners and lids for each eye and iris landmark ranges
RIGHT_EYE = {
    "outer": 33, "inner": 133, "top": 159, "bottom": 145,
    "iris": [468, 469, 470, 471]
}
LEFT_EYE = {
    "outer": 362, "inner": 263, "top": 386, "bottom": 374,
    "iris": [473, 474, 475, 476]
}

# Smoothing and reporting parameters
history_len = 9
stable_required = 5
direction_history = deque(maxlen=history_len)
last_reported_direction = None
last_report_time = 0.0
report_cooldown = 0.7  # seconds

def avg_landmark_pos(landmarks, indices, frame_w, frame_h):
    """Return average (x, y) in pixel coords for given landmark indices."""
    xs, ys = [], []
    for i in indices:
        lm = landmarks[i]
        xs.append(int(lm.x * frame_w))
        ys.append(int(lm.y * frame_h))
    return (sum(xs) / len(xs), sum(ys) / len(ys))

def eye_direction_from_landmarks(landmarks, eye_spec, frame_w, frame_h):
    """
    Compute direction for one eye using iris center and eye corner/top/bottom.
    Returns one of: 'LEFT','RIGHT','UP','DOWN','CENTER' or None if uncertain.
    """
    try:
        # corners and eyelids
        outer = landmarks[eye_spec["outer"]]
        inner = landmarks[eye_spec["inner"]]
        top = landmarks[eye_spec["top"]]
        bottom = landmarks[eye_spec["bottom"]]

        # convert to pixels
        outer_x = outer.x * frame_w
        inner_x = inner.x * frame_w
        top_y = top.y * frame_h
        bottom_y = bottom.y * frame_h

        # iris center (average of iris points)
        iris_x, iris_y = avg_landmark_pos(landmarks, eye_spec["iris"], frame_w, frame_h)

        # horizontal normalization relative to eye corners
        left_x = min(outer_x, inner_x)
        right_x = max(outer_x, inner_x)
        eye_w = right_x - left_x
        if eye_w <= 0.0:
            return None
        x_norm = (iris_x - left_x) / eye_w  # 0..1

        # vertical normalization relative to eyelids
        top_y = min(top_y, bottom_y)
        bottom_y = max(top_y, bottom_y)
        eye_h = bottom_y - top_y if (bottom_y - top_y) > 0 else 1.0
        y_norm = (iris_y - top_y) / eye_h  # 0..1

        # confidence check: iris should be inside reasonable bounds
        if x_norm < -0.2 or x_norm > 1.2 or y_norm < -0.5 or y_norm > 1.5:
            return None

        # thresholds tuned for robustness: prioritize left/right, then up/down
        left_th = 0.36
        right_th = 0.64
        up_th = 0.36
        down_th = 0.64

        if x_norm < left_th:
            return "LEFT"
        elif x_norm > right_th:
            return "RIGHT"
        elif y_norm < up_th:
            return "UP"
        elif y_norm > down_th:
            return "DOWN"
        else:
            return "CENTER"
    except Exception:
        return None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_h, frame_w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    frame_dir = None
    if results.multi_face_landmarks:
        # take first face
        face_landmarks = results.multi_face_landmarks[0].landmark

        # get directions for both eyes
        dir_right = eye_direction_from_landmarks(face_landmarks, RIGHT_EYE, frame_w, frame_h)
        dir_left = eye_direction_from_landmarks(face_landmarks, LEFT_EYE, frame_w, frame_h)

        # gather non-None directions
        dirs = [d for d in (dir_left, dir_right) if d is not None]

        if dirs:
            # if both eyes agree -> use that, else use the most common
            if len(dirs) == 2 and dirs[0] == dirs[1]:
                frame_dir = dirs[0]
            else:
                frame_dir = Counter(dirs).most_common(1)[0][0]

        # optional: draw small markers for iris centers and eye corners (lightweight)
        try:
            iris_r = avg_landmark_pos(face_landmarks, RIGHT_EYE["iris"], frame_w, frame_h)
            iris_l = avg_landmark_pos(face_landmarks, LEFT_EYE["iris"], frame_w, frame_h)
            cv2.circle(frame, (int(iris_r[0]), int(iris_r[1])), 2, (0, 255, 0), -1)
            cv2.circle(frame, (int(iris_l[0]), int(iris_l[1])), 2, (0, 255, 0), -1)
        except Exception:
            pass

    # update history
    direction_history.append(frame_dir)

    # stability check: require last stable_required entries equal and not None
    stable_direction = None
    if len(direction_history) >= stable_required:
        tail = list(direction_history)[-stable_required:]
        if tail.count(tail[0]) == stable_required and tail[0] is not None:
            stable_direction = tail[0]

    # report when stable and on change or cooldown
    now = time.time()
    if stable_direction is not None:
        cv2.putText(frame, f"Looking: {stable_direction}", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        if stable_direction != last_reported_direction or (now - last_report_time) > report_cooldown:
            print(stable_direction)
            last_reported_direction = stable_direction
            last_report_time = now
    else:
        cv2.putText(frame, "Looking: ...", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    cv2.imshow("Eye Tracker", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
