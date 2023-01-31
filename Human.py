
class Human:
    def __init__(self, name, gender, yob, homeTown, id):
        '''
        Initialize personal information
        
        name: first namme
        gender: male, female or lgbt
        yob: year of born
        homeTown: home town
        id: id code
        '''
        self.__name = name
        self.__gender = gender
        self.__yob = yob
        self.__homeTown = homeTown
        self.__id = id
    
    def showInfo(self):
        '''
        Show the personal information on terminal
        '''
        print("Name: ", self.__name)
        print("Year of born: ", self.__yob)
        print("Gender: ", self.__gender)
        print("Home town: ", self.__homeTown)
        print("ID: ", self.__id)