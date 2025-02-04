num_list = list(map(int, input("Enter numbers separated by space: ").split()))
print(num_list)
even=[num for num in num_list if num%2==0]
even.sort()
print("the even numbers are:  ",even)