num_of_questions = int(input("Enter the number of questions you would like: "))

answers = []

for i in range(num_of_questions):
    answer = input("Enter an item you would like to add to the list: " )
    answers.append(answer)
print(answers)

numbers = input("Enter numbers seperated by a space (ex. 1 2 3) " )

even_numbers = []

numbers_list = numbers.split(" ")
print(numbers_list)
    