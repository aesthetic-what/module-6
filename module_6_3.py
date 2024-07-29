class Horse:
    sound = "Frrr"
    x_distance = 0

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    sound = "I train, eat, sleep, and repeat"
    y_distance = 0

    def fly(self, yx):
        self.y_distance += yx
        return self.y_distance


class Pegasus(Horse, Eagle):

    def move(self, dx, yx):
        super().run(dx)
        super().fly(yx)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(Eagle.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
