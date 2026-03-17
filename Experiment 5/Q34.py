"""WAP: Insert Marks, Delete Failures, Sort
Input a list of student marks (0–100).
If any mark is > 100 or < 0, del that invalid mark
If a mark is < 35, insert the string "FAIL" right after that mark (use insert)"""
marks = [-3, 131, 43, 54, 32, 87, 44, 12, 0, 222, -5]

for i in marks:
    if i > 100 or i < 0:
        marks.remove(i)

marks.sort()


for i in marks:
    if i < 35:
        print(f"for marks {i}, you FAIL")
    else:
        print(f"for marks {i}, you PASS")