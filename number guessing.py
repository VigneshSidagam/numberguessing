import random
def fun():
    choice= int(input("enter your choice:"))
    computer = random.randint(1,100)
    while choice!=computer:
        if choice<computer:
            print("your guess is too low, Try again...!")
            choice= int(input("enter your choice:"))
        elif choice>computer:
            print("Your guess is too high, Try again...!")
            choice= int(input("enter your choice:"))
        else:
            print("Incorrect choice")
            break
    else:
        print("HURRAY!!! You won the game...")
fun()
ask= input("\nDo you wanna play again?(yes/no)\n")
while ask == "yes":
    fun()
    ask= input("Do you wanna play again?(yes/no)")
else:
    print("Thankyou!!!")
