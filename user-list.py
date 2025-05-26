#Welcome to python project user list
import utils.session
print('welcome to user list')

users = {}

while True :
    print('1. Create user')
    print('2. View user')
    print('3. Update user')
    print('4. Delete user')
    print('5. Search user')
    print('6. Count user')
    print('7. Exit')

    choice = input("Enter your choice = ")

    if choice == '1':
        name = input("Enter your name = ")
        if name in users :
            print(f'User name {name} is already exisits !')
        else :
            age = int(input("Enter your age = "))
            country = input('Enter your country = ')
            phon = int(input('Enter your phon number = '))
            email = input("Enter your Email = ")

            users[name] ={'name':name,'age':age,'country':country,'phon':phon,'email':email}
            print('User is created successfull')

    elif choice =='2':
        name = input('Enter view user name =')
        if name in users :
            user = users[name]
            print(f'Name:{name} age:{age},country : {country} phon : {phon} email : {email}')
        else :
            print("user not found")
    
    elif choice == '3':
        name = input('Enter your user update name =')

        if name in users :
            age = int(input("Enter your age = "))
            country = input('Enter your country = ')
            phon = int(input('Enter your phon number = '))
            email = input("Enter your Email = ")

            users[name] ={'name':name,'age':age,'country':country,'phon':phon,'email':email}
            print('User is update successfull')
        else :
            print("User not found")
    
    elif choice == '4':
        name = input('Enter your delete user name = ')
        
        if name in users :
            del users[name]
            print("user is deleted successfull")
        else :
            print('user not found')
    
    elif choice == '5':

        search_name = input('Inter your name search = ')
        found = False

        for name,user in users.items():
            if search_name.lower() in name.lower() :
                 print(f'Name:{name} age:{age},country : {country} phon : {phon} email : {email}')
                 found = True
            if not found :
                print('user not found')

    elif choice == '6':
        print('Total user ',len(users))
        
    elif choice == '7':
        print('Good bye ... Close the program')
    else :
        print('Invalid chioce')