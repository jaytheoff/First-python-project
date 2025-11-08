
def greet_user():
    print(f"please add your name")
    name = input("Enter your name: ")
    print(f"hello,{name}!, welcome to the game, this will be atext adventure game")

    part_1()

def part_1():
    print("one day your walking with ur friends and u come across a homeless man")
    
    print("he asks you for some money do you give him some money (1) or ignore him? (2)")
    choice = input("pick either 1 or 2: ")

    if choice == "1":
        print("you decide to be generous and pass the straving man a dollar")
        part_2()
    elif choice == "2":
        print("you ignore the old man and walk away")
        print("the homeless man begins to follow you and your friends so u feel uneasy...")
        part_2()
    else:
        print("invalid choice, please pick 1 or 2")
        part_1()

def part_2():
    print("you tell friends that the homeless man is following us they respond with ['we should call the cops'] 1 or ['lets confront him'] 2 they ask you what do you say?")
    choice = input("pick either 1 or 2: ")

    if choice == "1":
        print("you call the cops and they arrive shortly after, while the cops are arriving the homeless attempts to attack you" \
        " but the cops quickly subdue him and take him away")
        print("you and your friends are safe")
        print("the end")

    elif choice == "2":
        print("you and your friends confront the homeless man and ask him why he is follow you guys he responds with im hungry i just wanted to eat but u gave me no money i better kill one of you")
        print("suddenly he lunges at one of your friends and attacks them")
        print("you and your friends beat the fuck out of him and run out of there, the homeless man dies & was never seen again.")
        print("the end")

greet_user()