shopping_list = ["apples","bananas","pinapples","chocolates","water","eggs","meat"]

# add an item to the list
shopping_list.append("mayonaisse")
print(shopping_list)

# change an item of the list
shopping_list[1]="ketchup"
# remove an item from the list
del shopping_list[0]
print (shopping_list)
# count the number of items in the list
print(len(shopping_list))
print("-------------------------------")

my_list = [1, 2, 3, 4, 5]

# print the list in the reversed format
for i in range(len(my_list)-1,-1,-1):
  print(my_list[i])

print("---------------------------------")
print(my_list[::-1])

