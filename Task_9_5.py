class Stationary:
    def __init__(self, title="Draw"):
        self.title = title

    def draw(self):
        print(f'Drawing! {self.title}))')

class Pen(Stationary):
    def draw(self):
        print(f'Drawing with {self.title} pen!')

class Pencil(Stationary):
    def draw(self):
        print(f'Drawing with {self.title} pencil!')

class Handle(Stationary):
    def draw(self):
        print(f'Drawing with {self.title} handle!')

stat = Stationary()
stat.draw()
pen = Pen('Parker')
pen.draw()
pencil = Pencil('Berlingo')
pencil.draw()
handle = Handle('Brauberg')
handle.draw()