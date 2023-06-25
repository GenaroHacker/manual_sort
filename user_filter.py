
def user_filter(list_of_strings):
    best = []
    #the most efficient way to do this is to use a for loop
    for i in range(len(list_of_strings)):
        user_imput = input("Do you like this string? (y/n) \n" + list_of_strings[i] + "\n")
        if user_imput == "y":
            best.append(list_of_strings[i])
            print("You have selected " + str(len(best)) + " strings so far.")
    return best
