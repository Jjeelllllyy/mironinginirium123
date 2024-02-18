class Button:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count = self.count + 1

    def click_count(self):
        return self.count

    def reset(self):
        self.count = 0

button = Button()
print('Кол-во нажатий: ')
print(button.click_count())
button.click()
print('Кол-во нажатий: ')
print(button.click_count())