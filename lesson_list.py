import random

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

for elem in lst:
    print(elem)
print("-------------------------")
print(lst[:3])
print("-------------------------")

print(lst[0])
print(lst[1])
print(lst[2])

print("-------------------------")
for i in range(3):
    print(i)

print("-------------------------")
for i in range(len(lst)):
    print(i, lst[i])
print("-----------------------------------")
lst1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
for i in  range(len(lst1)):
    lst1[i]**=2
print(lst1)
print("-------------------------------------")


zerros_lst = [0] * 100
print(zerros_lst)
def fill_list(zerros_lst, lower_bound, upper_bound):
    for i in range(len(zerros_lst)):
        zerros_lst[i] = random.randint(lower_bound, upper_bound)
fill_list (zerros_lst, 10, 20)
print(zerros_lst)

print("-------------------------------------")

def multply_list(lst, coeff):
    for i in range(len[lst]):
        lst[i] *= coeff
multply_list(lst, 2)

print(id(zerros_lst))
print(zerros_lst)

def nullify_list(lst):
    for i in range (len(lst)):
        lst1[i] = 0
nullify_list(zerros_lst)
print(id(zerros_lst), zerros_lst)