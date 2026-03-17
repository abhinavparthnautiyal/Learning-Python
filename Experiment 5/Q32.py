#WAP to delete duplicate elements in a list, sort the list, and print the first half.
original_list = ['1','2','3','4','5','6','7','8','9']
duplicate_list = ['',]

for i in original_list:
    duplicate_list.append(i)

mid = len(duplicate_list) // 2

for i in range(0, mid+1):
    print(duplicate_list[i], end=' ')
