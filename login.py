from datetime import time
import datetime
import os, sys
import pandas as pd

def login(mail,pw):
    
    jest = False
    logged = False

    users = pd.read_csv("data/users.csv", sep=';')
    #print(users)

    for i in range(len(users)):
        if users['login'].loc[i] == mail:
            jest = True
            if users['password'].loc[i] == pw:

                print('Loged in as: ' + mail + '!')
                logged = True
                print("Twoja ostatnia aktywność była: "+ str(users['lastactivity'].loc[i]))
                users['lastactivity'].loc[i] = datetime.datetime.now()
                users.to_csv('data/users.csv',sep=';')
                # print(users)
            else:
                print('Niepoprawne hasło!')
    if not jest:
        print('Nie ma takiego użytkownika!')
        sys.exit()
    return logged

# login(mail,pwd)