import os

filename = input("Enter the filename: ")
while True:
    print('Choose the action:')
    print('1. Create file(if not exists)')
    print('2. Add data')
    print('3. Display data')
    print('4. Rename the file')
    print('5. Delete the file')
    x = int(input())
    match x:
        case 1:
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    file.write('')
                print(f"File '{filename}' created.")
                print(' ')
            else:
                print(f"File '{filename}' already exists.")
                print(' ')
        case 2:
            f = open(filename, "a")
            content = input('Write a text: ')
            f.write(content)
            f.close()
            print(' ')
        case 3:
            f = open(filename, "r")
            print(f.read())
            f.close()
            print(' ')
        case 4:
            new_filename = input("Enter the new filename: ")
            os.rename(filename, new_filename)
            print(f"File '{filename}' renamed to '{new_filename}'.")
            filename = new_filename
            print(' ')
        case 5:
            if os.path.exists(filename):
                os.remove(filename)
                print('File deleted successfully!')
                print(' ')
            else:
                print("The file does not exist!")
                print(' ')
