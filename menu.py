import datetime
from login import login
from opcje import analiza, dodajusera, dodajzwierze, wyloguj
import os, sys
import opcje
import pandas as pd

users = pd.read_csv("data/users.csv", sep=';')

def menu():
    opcja = input("Proszę wybrać odpowiednią opcje:\n"+
    "1. Zidentyfikuj zwierze\n"+
    "2. Dodaj nowe zwierzę\n"+
    "0. Wyjdż z programu\n")
    if opcja == '1':
        analiza()
    if opcja == '2':
        dodajzwierze()
    if opcja == '0':
        wyloguj()
        sys.exit()

def menu_adm():
    opcja = input("Proszę wybrać odpowiednią opcje:\n"+
    "1. Dodaj użytkownika\n"+
    "2. Sprawdź aktywność użytkowników\n"+
    "0. Wyjdż z programu\n")
    if opcja == '1':
        dodajusera()
    if opcja == '2':
        print(users)
    if opcja == '0':
        wyloguj()
        sys.exit()

