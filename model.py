import pandas as pd

def get_data_from_table(data_path):
    data = pd.read_table(data_path)
    data.head()
    print(data)
    return data

def get_features_names(data):
    features_names = []
    for col in data.columns:
        if col != 'type' and col != 'name':
            features_names.append(col)
    print(features_names)
    return features_names

def save_new_data_object(animal_object):
    f = open("data/zoo.csv", "a")
    f.write(animal_object.get_animal_data_to_save())
    f.close()
