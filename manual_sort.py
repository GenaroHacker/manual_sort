
my_list = """
1
2
3
4
5
6
7
"""




def string_to_list(string):
    string = string.split('\n')
    string = [line.strip() for line in string if line.strip()]
    return string

import functools

def ask_user_cmp(item1, item2):
    while True:
        print(f"[{item1}](1) or \n[{item2}](2) ?")
        cmp = input("--> ")
        if cmp == "1":
            return 1
        if cmp == "2":
            return -1
        print("1 or 2, please!")

def user_filter(list_of_strings):
    best = []
    #the most efficient way to do this is to use a for loop
    for i in range(len(list_of_strings)):
        user_imput = input("Do you like this string? (y/n) \n" + list_of_strings[i] + "\n")
        if user_imput == "y":
            best.append(list_of_strings[i])
            print("You have selected " + str(len(best)) + " strings so far.")
    return best
ask_user_key = functools.cmp_to_key(ask_user_cmp)

items_to_sort =  string_to_list(my_list)
items_to_sort = user_filter(items_to_sort)
items_to_sort.sort(key=ask_user_key, reverse=True)
print("Here's your list from highest to lowest:")
for i in items_to_sort:
  print(i)
