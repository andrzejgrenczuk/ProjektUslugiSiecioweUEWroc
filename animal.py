types = {1: "ssak", 2: "ptak", 3: "gad", 4: "ryba", 5: "płaz", 6: "owad", 7: "inny"}


class Animal(object):
    global types

    def __init__(self):
        self._name = 0
        self._hair = 0
        self._feathers = 0
        self._eggs = 0
        self._milk = 0
        self._airborne = 0
        self._aquatic = 0
        self._predator = 0
        self._toothed = 0
        self._backbone = 0
        self._breathes = 0
        self._venomous = 0
        self._fins = 0
        self._legs = 0
        self._tail = 0
        self._domestic = 0
        self._catsize = 0
        self._type = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hair(self):
        return self._hair

    @hair.setter
    def hair(self, value):
        self._hair = value

    @property
    def feathers(self):
        return self._feathers

    @feathers.setter
    def feathers(self, value):
        self._feathers = value

    @property
    def eggs(self):
        return self._eggs

    @eggs.setter
    def eggs(self, value):
        self._eggs = value

    @property
    def milk(self):
        return self._milk

    @milk.setter
    def milk(self, value):
        self._milk = value

    @property
    def airborne(self):
        return self._airborne

    @airborne.setter
    def airborne(self, value):
        self._airborne = value

    @property
    def aquatic(self):
        return self._aquatic

    @aquatic.setter
    def aquatic(self, value):
        self._aquatic = value

    @property
    def predator(self):
        return self._predator

    @predator.setter
    def predator(self, value):
        self._predator = value

    @property
    def toothed(self):
        return self._toothed

    @toothed.setter
    def toothed(self, value):
        self._toothed = value

    @property
    def backbone(self):
        return self._backbone

    @backbone.setter
    def backbone(self, value):
        self._backbone = value

    @property
    def breathes(self):
        return self._breathes

    @breathes.setter
    def breathes(self, value):
        self._breathes = value

    @property
    def venomous(self):
        return self._venomous

    @venomous.setter
    def venomous(self, value):
        self._venomous = value

    @property
    def fins(self):
        return self._fins

    @fins.setter
    def fins(self, value):
        self._fins = value

    @property
    def legs(self):
        return self._legs

    @legs.setter
    def legs(self, value):
        self._legs = value

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self._tail = value

    @property
    def domestic(self):
        return self._domestic

    @domestic.setter
    def domestic(self, value):
        self._domestic = value

    @property
    def catsize(self):
        return self._catsize

    @catsize.setter
    def catsize(self, value):
        self._catsize = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def get_animal_data_to_save(self):
        attributesListString = ""
        attributesList = self.__dict__.values()

        for element in attributesList:
            if attributesListString != "":
                attributesListString += '\t'
            else:
                attributesListString += '\n'
            attributesListString += str(element)
        return attributesListString

    def type_name(self):
        return types[self.type]

    def get_animal_data_to_predict(self):
        attributesToCheckList = []
        attributesToCheckList.append(self.hair)
        attributesToCheckList.append(self.feathers)
        attributesToCheckList.append(self.eggs)
        attributesToCheckList.append(self.milk)
        attributesToCheckList.append(self.airborne)
        attributesToCheckList.append(self.aquatic)
        attributesToCheckList.append(self.predator)
        attributesToCheckList.append(self.toothed)
        attributesToCheckList.append(self.backbone)
        attributesToCheckList.append(self.breathes)
        attributesToCheckList.append(self.venomous)
        attributesToCheckList.append(self.fins)
        attributesToCheckList.append(self.legs)
        attributesToCheckList.append(self.tail)
        attributesToCheckList.append(self.domestic)
        attributesToCheckList.append(self.catsize)

        return [attributesToCheckList]
    
    def set_test_animal_data(self):

        self._name = 'hamster'

        self._hair = 1
        self._feathers = 0
        self._eggs = 0
        self._milk = 1

        self._airborne = 0
        self._aquatic = 0
        self._predator = 0
        self._toothed = 1

        self._backbone = 1
        self._breathes = 1
        self._venomous = 0
        self._fins = 0

        self._legs = 4
        self._tail = 1
        self._domestic = 1
        self._catsize = 1

        return self
