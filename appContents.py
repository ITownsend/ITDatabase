
def accountMaker():
    accounts = []
    print('Account Creation: 1 \n Account Details: 2(not Working')
    begin = input('Press Number that coincides with your Wishes: ')

    if begin == '1':
        print("To Exit Account please press q") # how to leave accountMAker
        while True:    #infinite loop
                userAcc = str((input('Please Enter Account Username: ')))
                accounts.append(userAcc)                                      # adds username to account list
                print('Successfully added Account: ' + str(accounts))
                if userAcc == 'q':
                    print('Goodbye')
                    return


    if begin == '9':
        print('OK')


thelist = ['Account Maker',]
print(thelist)

app = input('To start an app, type the name: ')
if app == 'Account Maker':
    accountMaker()
