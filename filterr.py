num_list = list(map(int, input("Enter numbers separated by space: ").split()))
print(num_list)

check = int(input("enter the number to check "))
new_list = [ num for num in num_list if num < check]
print("Numbers less than ",check," are ",new_list)