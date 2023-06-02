from pygame import *

window = display.set_mode((800, 600))
display.set_caption('button test')
font.init()

clock = time.Clock()
#класс кнопки
class Button(sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        super().__init__()
        self.img = img
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
    
#метод отрисовки
    def draw(self, fill_surface):
        fill_surface.blit(self.image, (self.rect.x, self.rect.y))
        self.x = self.rect.x
    
#метод для получения координат при нажатии
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)

#класс надписи для кнопки
class ButLabel():
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
#изменение/установка текста
    def set_text(self, text, fsize, text_color=(250, 250, 250)):
        self.text = text
        self.image = font.SysFont('Arial Black', fsize).render(text, True, text_color) #можно поставить другой шрифт, например, 'Arial'
#метод отрисовки
    def draw(self, shift_x, shift_y, fill_surface): #shift_x - смещение надписи по x, shift_y - смещение надписи по y
        fill_surface.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


#фон для меню
menu_background = transform.scale(image.load('menu_background.png'), (800, 600))
#создание списков кнопок
buttons = list()#создание списка всех кнопок, нужен для проверки нажатий
menu_buttons = list()#создание списка для кнопок меню, нужен для отрисовки этих кнопок в меню
menu_buttons_labs = list()#создание списка для надписей кнопок меню
...
#создание тестовой кнопки
test_button = Button(500, 70, 250, 80, 'button.png')
test_buttonLab = ButLabel(test_button.rect.x, test_button.rect.y, test_button.width, test_button.height)
test_buttonLab.set_text('тест', 25)
menu_buttons.append(test_button)
menu_buttons_labs.append(test_buttonLab)
buttons.append(test_button)

inMenu = True #при входе в игру открывается главное меню
inGame = False
game = True
while game:
    if inMenu: #отрисовка главного меню
        window.blit(menu_background, (0, 0))
        for i in menu_buttons:
            i.draw(window) #отрисовка кнопок
        for l in menu_buttons_labs:
            l.draw(20, 20, window) #отрисовка надписей кнопок
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1: 
            ex, ey = e.pos
            for i in buttons:
                if i.collidepoint(ex, ey) == 1:#проверка нажатия левой кнопки мыши
                    if inMenu:
                        if i == test_button:
                            inMenu = False
                            inGame = True
                        #elif i == ...
    #if inGame:
        #Игра







    clock.tick(60)
    display.update()