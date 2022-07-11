class Page:
    class_attribute = "CLASS_ATTR"

    def __init__(self, name):
        self.name = name

    def open(self):
        print("Opened: " + self.name)

    def show(self):
        print(self.class_attribute)


main_page = Page(name="MainPage")
login_page = Page(name="LoginPage")
contacts_page = Page(name="ContactsPage")

main_page.open()
login_page.open()
contacts_page.open()

main_page.show()
login_page.show()
contacts_page.show()
