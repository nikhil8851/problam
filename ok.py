def choose_file_for_read():
    filename = open('C:/Users/PC/AppData/Local/Programs/Microsoft VS Cod/.vscode/work/file/.txt', 'r')
    myfile = filename.readlines()

    list_box  = []
    print('/n')
    i = 1
    for r in myfile:
        print(i, r.strip())
        # append data with strip method to remov /n
        list_box.append(r.strip())
        i += 1
    
    option = input('/nEnter your options: ')
    print('/nOption: ', option)
    print('/nFinal list: ', list_box)

    user_options()
    filenam.close

# choose_to_write_in_file()
def choose_to_write_in_file():
    filename = input('/nEnter file name: ')

    # open file
    myfile = open('C:/Users/PC/AppData/Local/Programs/Microsoft VS Code/.vscode/work/file/'+filename+'.txt', 'a')

    # add data on this file
    user_message = input('Enter your message: ')

    # add message to file
    myfile.write(user_message)
    print('/nYour message is added on ' + filename + '.txt  file.')

    # finally close the file
    myfile.close()

    user_options()

# Provide option to user for read and write:

def user_options():
    message = '''
    ------------------------------------------
                Hello User
    ------------------------------------------
    Choose available options:
    
    1. Choose File for Read
    2. Choose to write in available file
    3. Exit
    -------------------------------------------
    '''
   

    print(message)

    try:
        options = int(input('Enter numbre to visist available options: '))
    except:
        print('/nOnly numbers allowed. Try again with number.')
    else:
        if options == 1:
            choose_file_for_read()
        elif options == 2:
             choose_to_write_in_file()
        elif options == 3:
            print('/nYou are successfully exit.')
        else:
            print('/nYou entered wrong options. Try again.')

user_options()
