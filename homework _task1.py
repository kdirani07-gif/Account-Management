numbers = input("Enter numbers seperated by a space (ex. 1 2 3) " )

even_numbers = []

numbers_list = list(map(int, numbers.split(" ")))
print(numbers_list)

for i in range(len(numbers_list)):
    answer = numbers_list[i]%2
    if answer == 0:
       print(numbers_list[i])
        