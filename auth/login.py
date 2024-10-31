class Login:

    def __init__(self, student):
        self.student = student

    def setPassword(self, password):
        self.password = password

    def loginAttempt(self, password):
        if password == self.password:
            print("Login successful!")
        else:
            print("Login failed")