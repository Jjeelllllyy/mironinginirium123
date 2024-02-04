class Car:
    def __init__(self, color, mark, max_speed, weight):
        self.color = color
        self.mark = mark
        self.max_speed = max_speed
        self.weight = weight

    def sound(self):
        print('Beep!')

    def long_sound(self):
        print('Beep-Beep!')

bwm = Car('Черный', 'bmw', 150, 1000)
print(bwm.color)
print(bwm.mark)
print(bwm.max_speed)
print(bwm.weight)

mers = Car('Белая', 'mers', 150, 1000)

print(mers.color)
print(mers.mark)
print(mers.max_speed)
print(mers.weight)





bwm.sound()
mers.long_sound()
