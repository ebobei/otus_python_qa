class Page:
    class_attribute = "CLASS_ATTR"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        print("Opened: " + self.browser)

    def open_profile(self):
        print("click " + self.class_attribute)

    def login(self, username, password):
        print(f"Input {username} {password}")

class Browser:
    pass

class Loginpage(Page):
    pass

class MainPage(Page):
    pass

browser = Browser()
main_page = MainPage(browser)
login_page = Loginpage(browser)
