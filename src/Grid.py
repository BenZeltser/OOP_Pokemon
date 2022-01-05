'''Heavily Inspired by Shay the Teacher'''

import pygame
from algo import *
import math

pygame.font.init()
pygame.init()
FONT = pygame.font.SysFont('comicsans', 25)
screen = pygame.display.set_mode((800, 600))


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


min_x = min_y = max_x = max_y = 0


def min_max(graph):
    global min_x, min_y, max_x, max_y
    min_x = min(list(graph.nodes.values()), key=lambda n: n.pos[0]).pos[0]
    min_y = min(list(graph.nodes.values()), key=lambda n: n.pos[1]).pos[1]
    max_x = max(list(graph.nodes.values()), key=lambda n: n.pos[0]).pos[0]
    max_y = max(list(graph.nodes.values()), key=lambda n: n.pos[1]).pos[1]


def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


class Button:
    def __init__(self, color, rect: pygame.Rect):
        self.color = color
        self.rect = rect
        self.pressed = False

    def press(self):
        self.pressed = not self.pressed


button = Button(color=(250, 250, 0), rect=pygame.Rect((10, 10), (100, 50)))


def arrow(start, end, d, h, color):
    """
        קרדיט לדביר על הפונקציה
        """
    dx = float(end[0] - start[0])
    dy = float(end[1] - start[1])
    D = float(math.sqrt(dx * dx + dy * dy))
    xm = float(D - d)
    xn = float(xm)
    ym = float(h)
    yn = -h
    sin = dy / D
    cos = dx / D
    x = xm * cos - ym * sin + start[0]
    ym = xm * sin + ym * cos + start[1]
    xm = x
    x = xn * cos - yn * sin + start[0]
    yn = xn * sin + yn * cos + start[1]
    xn = x
    points = [(end[0], end[1]), (int(xm), int(ym)), (int(xn), int(yn))]

    pygame.draw.line(screen, color, start, end, width=4)
    pygame.draw.polygon(screen, color, points)


class Circle:
    def __init__(self, rect: pygame.Rect, id):
        self.circle = rect
        self.id = id


result_algo = []
circles = []


def on_click(algo: Algo):
    global result_algo
    result_algo = algo.my_algo()


def draw(algo: Algo, src=-1):
    if src != -1:
        c_text = FONT.render(str(src), True, (0, 0, 250))
        screen.blit(c_text, (400, 50))
    pygame.draw.rect(screen, button.color, button.rect)
    button_text = FONT.render("Algo", True, (0, 0, 250))
    screen.blit(button_text, (button.rect.x + 20, button.rect.y + 10))
    for src in algo.graph.nodes.values():
        x = my_scale(src.pos[0], x=True)
        y = my_scale(src.pos[1], y=True)
        circles.append(Circle(pygame.Rect((9, 9), (x, y)), src.id))
        src_text = FONT.render(str(src.id), True, (0, 0, 250))
        screen.blit(src_text, (x, y))
        pygame.draw.circle(screen, (227, 77, 148), (x, y), radius=10)
        for dest in algo.graph.edges[src.id]:
            dest = algo.graph.nodes[dest]
            his_x = my_scale(dest.pos[0], x=True)
            his_y = my_scale(dest.pos[1], y=True)
            if (src.id, dest.id) in result_algo:
                arrow((x, y), (his_x, his_y), 15, 5, (250, 0, 0))
            else:
                arrow((x, y), (his_x, his_y), 15, 5, (0, 0, 0))
            # pygame.draw.line(screen,(0,0,0),start_pos=(x,y),end_pos=(his_x,his_y),width=3)


def display(algo: Algo = None):
    min_max(algo.graph)
    run = True
    src = -1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    button.press()
                    if button.pressed:
                        on_click(algo)
                    else:
                        result_algo.clear()

                for c in circles:
                    if c.circle.collidepoint(event.pos):
                        src = c.id
                        break

        screen.fill((34, 189, 173))
        draw(algo, src)

        pygame.display.update()


if __name__ == '__main__':
    g = from_json("graph3.json")
    a = Algo()
    a.init_graph(g)
    display(a)
