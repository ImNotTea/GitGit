
class Human:
    def __init__(self, name, gender, yob, homeTown):
        '''
        Initialize personal information
        
        name: first namme
        gender: male, female or lgbt
        yob: year of born
        homeTown: home town
        '''
        self.__name = name
        self.__gender = gender
        self.__yob = yob
        self.__homeTown = homeTown
    
    def showInfo(self):
        '''
        Show the personal information on terminal
        '''
        print("Name: ", self.__name)
        print("Year of born: ", self.__yob)
        print("Gender: ", self.__gender)
        print("Home town: ", self.__homeTown)