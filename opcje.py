import datetime
from model import get_data_from_table, get_features_names, save_new_data_object
import login
import model
import pandas as pd
import animal
from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier

users = pd.read_csv('/home/grencan/development/code/python/ProjektUEzaliczenie/data/users.csv')

def dodajusera():
    users = pd.read_csv('/home/grencan/development/code/python/ProjektUEzaliczenie/data/users.csv')
    nazwa = input("Podaj Imie i nazwisko osoby ")
    login = input("Podaj login osoby ")
    password = input("Nadaj hasło użytkownikowi ")
    new_user=pd.DataFrame([[
        len(users)+1,
        nazwa,
        login,
        password        
    ]])
    new_user.to_csv('/home/grencan/development/code/python/ProjektUEzaliczenie/data/users.csv',sep=';',mode='a',index=False,header=False)

def analiza():
    zooData = get_data_from_table('data/zoo.csv')
    features_names = get_features_names(zooData)
    X = zooData[features_names]
    y = zooData['type']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    # knn = KNeighborsClassifier()
    knn = MLPClassifier((16,10,7))
    knn.fit(X_train, y_train)
    animal_object = animal.Animal()
    animal_object.name = input("Jak nazywa się zwierze? ")
    animal_object.hair = input("Czy zwierze posiada sierść? ")
    animal_object.feathers = input("Czy zwierze posiada pióra? ")
    animal_object.eggs = input("Czy zwierze składa jaja? ")
    animal_object.milk = input("Czy karmi młode mlekiem? ")
    animal_object.airborne = input("Czy to zwierze latające? ")
    animal_object.aquatic = input("Czy to zwierze wodne? ")
    animal_object.predator = input("Czy to drapieżnik? ")
    animal_object.toothed = input("Czy zwierze posiada uzębienie? ")
    animal_object.backbone = input("Czy zwierze posiada kręgosłup? ")
    animal_object.breathes = input("Czy to zwierze oddychające? ")
    animal_object.venomous = input("Czy to zwierze jadowite? ")
    animal_object.fins = input("Czy zwierze posiada płetwy? ")
    animal_object.legs = input("Ile posiada nóg?? ")
    animal_object.tail = input("Czy zwierze posiada ogon? ")
    animal_object.domestic = input("Czy to zwierze domowe? ")
    animal_object.catsize = input("Czy to zwierze wielkości kota? ")
    # animal_object = animal.Animal().set_test_animal_data()
    animal_object.type = knn.predict(animal_object.get_animal_data_to_predict())[0]
    print(animal_object.name + " to " + animal_object.type_name())
    if input("Enter your option: [T/N]") == "T":
        model.save_new_data_object(animal_object)
    zooData = get_data_from_table('data/zoo.csv')

def wyloguj():
    users = pd.read_csv('/home/grencan/development/code/python/ProjektUEzaliczenie/data/users.csv', sep=';')
    users.loc[len(users)-1, "lastactivity"] = datetime.datetime.now()
    users.to_csv('/home/grencan/development/code/python/ProjektUEzaliczenie/data/users.csv',mode='a',sep=';',index=False,header=False)

def dodajzwierze():
    animal_object = animal.Animal()
    animal_object.name = input("Jak nazywa się zwierze? ")
    animal_object.hair = input("Czy zwierze posiada sierść? ")
    animal_object.feathers = input("Czy zwierze posiada pióra? ")
    animal_object.eggs = input("Czy zwierze składa jaja? ")
    animal_object.milk = input("Czy karmi młode mlekiem? ")
    animal_object.airborne = input("Czy to zwierze latające? ")
    animal_object.aquatic = input("Czy to zwierze wodne? ")
    animal_object.predator = input("Czy to drapieżnik? ")
    animal_object.toothed = input("Czy zwierze posiada uzębienie? ")
    animal_object.backbone = input("Czy zwierze posiada kręgosłup? ")
    animal_object.breathes = input("Czy to zwierze oddychające? ")
    animal_object.venomous = input("Czy to zwierze jadowite? ")
    animal_object.fins = input("Czy zwierze posiada płetwy? ")
    animal_object.legs = input("Ile posiada nóg?? ")
    animal_object.tail = input("Czy zwierze posiada ogon? ")
    animal_object.domestic = input("Czy to zwierze domowe? ")
    animal_object.catsize = input("Czy to zwierze wielkości kota? ")
    print("Gatunek, który należy wpisać liczbą\n"+
    '{1: "ssak", 2: "ptak", 3: "gad", 4: "ryba", 5: "płaz", 6: "owad", 7: "inny"}')
    animal_object.type = input("Jakiego gatunku jest zwierzę? ")
    if input("Enter your option: [T/N]") == "T":
        model.save_new_data_object(animal_object)