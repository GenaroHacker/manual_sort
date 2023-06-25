import functools

def ask_user_cmp(item1, item2):
    while True:
        print(f"[{item1}](1) or [{item2}](2) ?")
        cmp = input("--> ")
        if cmp == "1":
            return 1
        if cmp == "2":
            return -1
        print("1 or 2, please!")

ask_user_key = functools.cmp_to_key(ask_user_cmp)

items_to_sort = ["pizza", "cheeseburger", "beef", "soup", "ice cream"]
items_to_sort.sort(key=ask_user_key, reverse=True)
print("Here's your list from highest to lowest:")
print(items_to_sort)
