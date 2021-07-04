#==================
#IMPORTS AND CONNECTIONS
#==================
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
Builder.load_file('design.kv')


#==================
# LOG IN SCREEN
#==================
#LoginScreen has Screen as a parameter, it is the Screen imported from Kivy
class LoginScreen(Screen):
    #signup button
    def sign_up(self):
        self.manager.current = "sign_up_screen"

#checking to make sure the uname and pword are correct/in the database
    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname] ['password'] == pword:
            self.manager.current = 'LoginScreenSuccess'


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


#==================
#SIGN UP SCREEN
#==================
class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open ("users.json") as file:
            users = json.load(file)
        print(users)

        users[uname] = {'username': uname,
        'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        
        with open("users.json", 'w') as file:
            json.dump(users, file)
            self.manager.current = "sign_up_screen_success"

#on signup page, go back to login page
class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen"
        self.manager.transition.direction = 'right'

#==================
#ROOT WIDGET
#==================

class RootWidget(ScreenManager):
    pass

""" class MainApp(App):
    def build(self):
        return super().build() """
class MainApp(App):
    def build(self):
        return RootWidget()


#==================
#
#==================
if __name__ == "__main__":
    MainApp().run()














#==================
#
#==================




#==================
#
#==================