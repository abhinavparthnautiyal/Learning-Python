
"""
Print this pattern:
@#@#@
#@#@#
@#@#@
#@#@#
@#@#@
"""
for i in range (1, 6):
    if i % 2 == 0:
        for j in range(1, 6):
            if j % 2 == 0:
                print("@",end="")
            else:
                print("#",end="")
        print()
    else:
        for j in range(1, 6):
            if j % 2 == 0:
                print("#",end="")
            else:
                print("@",end="")
        print()
