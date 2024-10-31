class Student:
    def __init__(self, firstName, lastName, idNumber, gradYear, email, address) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.gradYear = gradYear
        self.email = email
        self.address = address


    def __str__(self) -> str:
        pass
