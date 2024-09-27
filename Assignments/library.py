import random

#list of names
name_list = ["Mia", "Zack", "Emily", "James", "Noah", "Juan", "Kyle", "Jake", "Jill", "Rob", "Tom", "Bill",
             "Anna", "Max", "Luke"]

secretnumber = random.randint(10, 99)

secretname = random.choice(name_list)

def guess_number ():
    global secretnumber
    attempts = 0
    while attempts < 10:
        try: #using try and except to ensure number is integer 
            guess = int(input("Please input a guess for a two digit number: "))
        except:
            print("Please input an integer.")
        else:
            if guess == secretnumber:
                print("You Win!!")
                return
            elif guess >= secretnumber:
                print("Guess Lower")
                attempts += 1
            elif guess <= secretnumber:
                print("Guess Higher")
                attempts += 1
        #print(f"attempts: {attempts}")
    
    print(f"You Loose.") #this will print if attempts are = 10



def guess_name ():
    global secretname
    guessed_list = []
    attempts = 0
    secretname = secretname.lower() # force to be lower for checking purposes

    while attempts < 10:
        #this section of the code prints only the guessed letters of the name
        print("The secret name is: ", end = "")
        for i in secretname:
            if i in guessed_list:
                print(i, end = "")
            else:
                print("*", end = "")
        print("")

        #Take input
        guess = input("Please guess the letters that are asterisks: ")

        #check if guess is correct 
        if guess in secretname and len(guess) == 1 and guess not in guessed_list: #make sure user only inputed one letter
            print("You are correct! \n")
            guessed_list.append(guess)
        elif guess in guessed_list:
            print("You already guessed that! \n")
        else:
            attempts += 1
            print(f"Incorrect, {10 - attempts} attempts are left \n")


        #check if all letters in the name have been guessed, if so, return
        if set(guessed_list).issuperset(set(secretname)):
            print(f"Correct, you guessed the name: {secretname[0].upper() + secretname[1:]}")
            return
        
    #only prints out if all attempts are exhausted
    print(f"Sorry, have 0 attempts left, you loose. The name was {secretname}")

