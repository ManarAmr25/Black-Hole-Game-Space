from auth_proxy.sign_up import SignUp
from auth_proxy.sign_in import SignIn


class Facade:

    def __init__(self):

        self.s1 = SignUp()
        self.s2 = SignIn()

    def signup_request(self, name, password, gender):
        print("name: ", name, " type:", type(name))
        print("password: ", password, " type:", type(password))
        print("gender: ", gender, " type:", type(gender))
        return self.s1.sign_up(name, password, gender)  # name,password,gender

    def signin_request(self, name, password):
        return self.s2.sign_in(name, password)  # name,password

    # get a quote from database
    # view achievements
    # save player and achievements to database
