import os
import pygame
import game


def load_image(name, colorkey=None):
    name = os.path.join("img", name)
    if not os.path.isfile(name):
        exit()

    image = pygame.image.load(name)
    if colorkey is not None:
        image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image.convert_alpha()

    return image


# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)


class Game:
    def __init__(self, fps: int):
        self.__fps = fps  # fps
        pygame.init()
        # defining a font
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)  # отрисовка рабочего окна=
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.clock = pygame.time.Clock()  # fps
        pygame.display.set_caption('Проект - 3d игра')
        self.background = load_image("background-menu.jpg")

    def menu(self):
        font = pygame.font.Font('font\\font.ttf', 35)
        mouse_pos = pygame.mouse.get_pos()
        if self.width / 2 - 105 <= mouse_pos[0] <= self.width / 2 + 105 and \
                self.height / 2 - 70 <= mouse_pos[1] <= self.height / 2 - 10:
            pygame.draw.rect(self.screen, "white", [self.width / 2 - 105, self.height / 2 - 70, 200, 60],
                             border_radius=10)
            start = font.render('Start', True, (0, 0, 0))
        else:
            pygame.draw.rect(self.screen, "black", [self.width / 2 - 105, self.height / 2 - 70, 200, 60],
                             border_radius=10)
            start = font.render('Start', True, (255, 255, 255))
        if self.width / 2 - 105 <= mouse_pos[0] <= self.width / 2 + 105 and \
                self.height / 2 + 40 <= mouse_pos[1] <= self.height / 2 + 100:
            pygame.draw.rect(self.screen, "white", [self.width / 2 - 105, self.height / 2 + 40, 200, 60],
                             border_radius=10)
            quit_ex = font.render('Quit', True, (0, 0, 0))
        else:
            pygame.draw.rect(self.screen, "black", [self.width / 2 - 105, self.height / 2 + 40, 200, 60],
                             border_radius=10)
            quit_ex = font.render('Quit', True, (255, 255, 255))
        self.screen.blit(start, (self.width / 2 - 50, self.height / 2 - 75))
        self.screen.blit(quit_ex, (self.width / 2 - 45, self.height / 2 + 35))

    def check_click(self):
        mouse = pygame.mouse.get_pos()
        if self.width / 2 - 105 <= mouse[0] <= self.width / 2 + 105 and \
                self.height / 2 - 70 <= mouse[1] <= self.height / 2 - 10:
            game.start(self.width, self.height)
        elif self.width / 2 - 105 <= mouse[0] <= self.width / 2 + 105 and \
                self.height / 2 + 40 <= mouse[1] <= self.height / 2 + 100:
            exit()

    def run(self) -> None:
        """
        Основной цикл игры
        :return: None
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                # checks if a mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the mouse is clicked on the
                    # button the game is terminated
                    self.check_click()

            self.screen.fill('black')
            self.screen.blit(self.background, (0, 0))
            self.menu()
            pygame.display.flip()
            self.clock.tick(self.__fps)


start = Game(60)
start.run()
