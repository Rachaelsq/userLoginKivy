#==================
#IMPORTS AND CONNECTIONS
#==================
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
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
            self.manager.current = 'login_screen_success'
#login wrong
        else:
            self.ids.login_wrong.text = "Wrong username or password"

#==================
#LOG IN SCREEN SUCCESS
#==================
class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()

        #get list of file names
        available_feelings = glob.glob("quotes/*txt")

        #list comprehension
        available_feelings = [Path(filename).stem for filename in
                            available_feelings]
        
        #opening a random quote from txt file
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "try another feeling"

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