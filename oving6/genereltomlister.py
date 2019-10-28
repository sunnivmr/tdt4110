print("\na)")
my_first_list = [i for i in range(1, 7)]
# my_first_list = [1, 2, 3, 4, 5, 6]
print(my_first_list)

print("\nb)")
print(my_first_list[-1])
# print(my_first_list[len(my_first_list)-1])
# print(my_first_list[5])

print("\nc)")
my_first_list[-2] = "pluss"
# my_first_list[len(my_first_list)-1] = "pluss"
print(my_first_list)

print("\nd)")
#l = len(my_first_list)
# my_second_list = []

my_second_list = my_first_list[3:]

# for i in range(l-3, l):
#     my_second_list.append(my_first_list[i])

print(my_second_list)

print("\ne)")
print(my_second_list, "er lik", 10)