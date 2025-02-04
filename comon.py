num_list1 = list(map(int, input("Enter numbers separated by space: ").split()))
print(num_list1)
num_list2 = list(map(int, input("Enter numbers separated by space: ").split()))
print(num_list2)
common = [i for i in num_list1 if i in num_list2]
print("common elements are :  ",common)