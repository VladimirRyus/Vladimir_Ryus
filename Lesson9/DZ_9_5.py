class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Рисование')


class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')


class Pencil(Stationery):
    def draw(self):
        print('Карандашь чертит')


class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')


pen = Pen('Ручка')
pencil = Pencil('Карандашь')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()