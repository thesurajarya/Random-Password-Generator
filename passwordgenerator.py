#password generator
#imports
import random as r
print('WELCOME TO PASSWORD GENERATOR')
print('                Coded by Suraj Arya')
#pass_len = int(input('how many characters you want your password to have?: '))
def randompass():
    num = r.randint(10,99)
    num2 = r.randint(10,99)
    passnum2 = str(num2)
    passnum = str(num)
    specialchar_list = ("!@#$%^&*()_+{}|:<>?,./;'[]~`")
    var_list = ("abcdefghijklmnopqrstuvwxyz")
    var_list1 = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    str(specialchar_list)
    str(var_list)
    pa = passnum + specialchar_list[(r.randint(0,27))] + var_list[r.randint(0,25)] + passnum2 + var_list1[r.randint(0,25)] + specialchar_list[r.randint(0,27)]
    print(f'PASSWORD: {pa}')
a = 1
while a == 1:
    ask1 = input("Do you want a random password (y/n): ")
    while ask1 == 'y':
        randompass()
        exit()
    else:
        a = 2
        print('Exiting the script.......')
        exit()

