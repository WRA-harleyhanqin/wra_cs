from student import Student

class Main:
    student  = Student("Harley", "Gu", "10****", "2025", "guh25@wra.net", "Shanghai, China") #Create student profile

    student.signup.updatePassword("Computer") #Set password to "Computer"

    student.login.loginAttempt("123456") #Try to login with password "123456"

    student.login.loginAttempt("Computer") #Try to login with password "Computer"