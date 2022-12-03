class UserOriginal:
    def __init__(self, name, email):
        self.name = name
        self.email = email


    def modifyName(self, newName):
        self.name = newName 
    
    
    def modifyEmail(self, email):
        self.email = email

    def logUser(self):
        print("User's name: " + self.name)    
        print("User's email: " +  self.email)


# UserOriginal class violates the Single-Responsibility-Principle because the User's class has to worry about modifying the user's name or email.
# Meaning that it should have only one reason to change.



class Logger:
    def logMessage(self, message):
        print(message)


class UserModified:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logger = Logger()


    def modifyName(self, name):
        self.name = name;    

    def modifyEmail(self, email):
        self.email = email


    def logUser(self):
        self.logger.logMessage("User's name: " + self.name)    
        self.logger.logMessage("User's email: " + self.email)





# In the modfified version the user doesn't have to worry about logging the message to the console.
# The logger class will only worry about logging whatever message to the console and even if we wanted to send an email to the user instead of logging the message, we will need to only modify the logger class without having to worry about the other classes.

