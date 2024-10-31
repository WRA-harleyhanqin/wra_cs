from auth.login import Login
from auth.signup import Signup

class Student:
    def __init__(self, firstName, lastName, idNumber, gradYear, email, address) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.gradYear = gradYear
        self.email = email
        self.address = address
        self.login = Login(self)
        self.signup = Signup(self)

    