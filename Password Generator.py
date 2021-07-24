#Password generator with 3 levels of strength

#IMPORTS
import random

#GLOBAL VARIABLES
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '<', '>']
password_list = []

password_strength = int(input("How strong of a password would you like (1:Weak 2:Medium 3:Strong)? "))
password_length = int(input("How long would you like the password to be (8-24)? "))

#FUNCTIONS
def weak_gen(letters, passwordLength, password): #gens password with letters only
    count = 1
    
    while count <= passwordLength:
        random_select = random.randint(0, len(letters)-1)
        casing_select = random.randint(1, 3)
        if casing_select % 2 == 0:
            password.append(letters[random_select].upper())         
        else:
            password.append(letters[random_select])
        count += 1
        
    return "".join(password)

def med_gen(letters, numbers, passwordLength, password): #gens password with letters and numbers only
    count = 1
    
    while count <= passwordLength:
        random_select = random.randint(0, 2)
        if random_select == 0:
            random_select = random.randint(0, len(numbers)-1)
            password.append(str(numbers[random_select]))
        else:
            random_select = random.randint(0, len(letters)-1)
            casing_select = random.randint(1, 3)
            if casing_select % 2 == 0:
                password.append(letters[random_select].upper())         
            else:
                password.append(letters[random_select])
        count += 1
        
    return "".join(password)

def strong_gen(letters, numbers, special, passwordLength, password): #gens password with letters, numbers, and special characters
    count = 1
    
    while count <= passwordLength:
        random_select = random.randint(0, 4)
        if random_select == 0:
            random_select = random.randint(0, len(special)-1)
            password.append(special[random_select])           
        elif random_select == 1:
            random_select = random.randint(0, len(numbers)-1)
            password.append(str(numbers[random_select]))            
        else:
            random_select = random.randint(0, len(letters)-1)
            casing_select = random.randint(1, 3)
            if casing_select % 2 == 0:
                password.append(letters[random_select].upper())         
            else:
                password.append(letters[random_select])       
        count += 1
        
    return "".join(password)

#MAIN CODE
if password_length >= 8 and password_length <= 24:
    if password_strength == 1:
        print(weak_gen(letters_list, password_length, password_list))
    elif password_strength == 2:
        print(med_gen(letters_list, numbers_list, password_length, password_list))
    elif password_strength == 3:
        print(strong_gen(letters_list, numbers_list, special_list, password_length, password_list))
    else:
        print("ERROR... Please input a valid password strength.")
else:
    print("ERROR... Please input a valid password length.")
