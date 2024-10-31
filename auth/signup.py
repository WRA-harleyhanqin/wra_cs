class Signup:
    def __init__(self, student):
        self.student = student

    def updatePassword(self, password):
        self.student.login.setPassword(password)