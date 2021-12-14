import requests
import random

adrs = input("Enter a valid url: ")

try:
    response = requests.get(adrs)
    print("URL verified ✔")
except:
    print("URL does not exist on Internet")


username = input('Type username:')
conf_username = input('Confirm username:')
if username == conf_username:
    print('username is saved!')
else:
    print('''username can't be confirmed :/ ''')


choice = input("Enter 'N' to make a new password\nEnter 'O' to save a old password:")
if choice == 'O':
    ask_password = input("Enter password:")
    print('Password saved!')
elif choice == 'N':
    small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                    ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

    capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M'
                    ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    numbers = ['1','2','3','4','5','6','7','8','9','0']

    special_symbols = ['!','@','#','$','%','&','*','_','|']

    first_part = random.choice(small_letters)
    second_part = random.choice(capital_letters)
    third_part = random.choice(numbers)
    fourth_part = random.choice(special_symbols)
    list_part = [first_part,second_part,third_part,fourth_part]
    password = '#'.join(list_part)
    print(password)

else:
    print('Please enter a valid input (N or O)')

