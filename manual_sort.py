def ask_user_cmp(item1, item2):
    while True:
        print(f" [ 1 ] [{item1}] ?" )
        print(f" [ 2 ] [{item2}] ?") 
        cmp = input(" --> ? ")
        if cmp == "1":
            return 1
        if cmp == "2":
            return -1
        print("1 or 2, please!")
