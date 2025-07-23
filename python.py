#!/usr/bin/python

# <true_statement> if <condition> else <false_statement>
x = 10
print("x is greater than 5") if x > 5 else print("x is 5 or less")

#   0           0 RESUME                   0

#   4           2 LOAD_CONST               0 (10)
#               4 STORE_NAME               0 (x)

#   5           6 LOAD_NAME                0 (x)
#               8 LOAD_CONST               1 (5)
#              10 COMPARE_OP              68 (>)
#              14 POP_JUMP_IF_FALSE        9 (to 34)
#              16 PUSH_NULL
#              18 LOAD_NAME                1 (print)
#              20 LOAD_CONST               2 ('x is greater than 5')
#              22 CALL                     1
#              30 POP_TOP
#              32 RETURN_CONST             4 (None)
#         >>   34 PUSH_NULL
#              36 LOAD_NAME                1 (print)
#              38 LOAD_CONST               3 ('x is 5 or less')
#              40 CALL                     1
#              48 POP_TOP  


x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")



#   0           0 RESUME                   0

#  32           2 LOAD_CONST               0 (10)
#               4 STORE_NAME               0 (x)

#  33           6 LOAD_NAME                0 (x)
#               8 LOAD_CONST               1 (5)
#              10 COMPARE_OP              68 (>)
#              14 POP_JUMP_IF_FALSE        9 (to 34)

#  34          16 PUSH_NULL
#              18 LOAD_NAME                1 (print)
#              20 LOAD_CONST               2 ('x is greater than 5')
#              22 CALL                     1
#              30 POP_TOP
#              32 RETURN_CONST             4 (None)

#  36     >>   34 PUSH_NULL
#              36 LOAD_NAME                1 (print)
#              38 LOAD_CONST               3 ('x is 5 or less')
#              40 CALL                     1
#              48 POP_TOP
#              50 RETURN_CONST             4 (None)