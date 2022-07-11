class Page:
    name = "PAGE"

    def open(self):
        print("Opened")

    def new_method(self):
        print("Method")


new_page = Page()
login_page = Page()

new_page.open()
print(login_page.name)
print(new_page.name)
login_page.open()
login_page.new_method()

print(new_page, login_page)
