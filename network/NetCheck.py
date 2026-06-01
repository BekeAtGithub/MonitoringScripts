import os

#Startup process...
#author Adam Beke.
def netCheck():
    print('Welcome To NetCheck.')
    print('NetCheck is where you may utilize BusyBox functionality')
    print()

netCheck() # runs the netCheck function ,yea

# defining network operations = x and y are dynamic variable placeholders for user input 
def telnet (x, y):
    pass
def netcat (x, y):
    pass
def traceroute (x, y):
    pass

# defining control menu for the user to interact with
def menu():
    print('Which tool would you like to use?')
    print('telnet')
    print('netcat')
    print('traceroute')
# open menu
menu()

# functionality of the control menu - where user may interact with the menu to use the network operators defined previously in the script
while True:
    #take input from user
    choice = input("Type in choice: ")
    #check if the choice is valid
    if not choice in ('telnet', 'netcat', 'traceroute'):
        print('Invalid Input')
        continue

    num1 = float(input('Enter Target IP Address: '))
    num2 = float(input('Enter Target Port: '))
    if choice == 'telnet':
        f"ip {num1} port {num2} = "
        os.system('telnet num1 num2')
    elif choice == 'netcat':
        f"ip {num1} TCP port {num2} = "
        os.system('nc -vz num1 num2')
        f"ip {num1} UDP port {num2} = "
        os.system('nc -vzu num1 num2')
    elif choice == 'traceroute':
        f"ip {num1} port {num2} = "
        os.system('traceroute num1 num2')
    # to make another Network check without closing
    repeatNetCheck = input('Would you like to make another NetCheck?(Y/n)')
    if repeatNetCheck == None: repeatNetCheck = "Y"
    if repeatNetCheck == "Y":
        break
