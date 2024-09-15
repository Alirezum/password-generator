import random
import string

length = int(input("Enter Password Length: "))

print(
    """Choose character set for password from these:
    1. Digits
    2. Letters
    3. Special characters
    4. Exit"""
)

character_list = ""


while True:
    choice = int(input("Pick a number "))
    if choice == 1:
        character_list += string.ascii_letters

    elif choice == 2:
        character_list += string.digits

    elif choice == 3:
        character_list += string.punctuation

    elif choice == 4:
        break
    else:
        print("Please Pick a Valid Option!")

password = []

for i in range(length):

    randomcher = random.choice(character_list)

    password.append(randomcher)


print("the random password is " + "".join(password))
