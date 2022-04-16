import pygame
from settings import *
from map import world_map


def ray_casting_horisontical(sc, _pos, _angle):
    x0, y0 = _pos  # позиция игрока
    if _angle - HALF_FOV <= 0:
        cur_angle = math.pi * 2 + _angle - HALF_FOV
    else:
        cur_angle = _angle - HALF_FOV  # вычитаем половину из угла игрока и нормалью, чтобы взять 1 луч

    for ray in range(NUM_RAYS):
        # определяем четверть в которой находится угол альфа
        #  math.pi / 2 - что-то типа 90 градусов
        step_x = 0
        if math.pi / 2 >= cur_angle >= 0:  # нижний правый кусок торта
            step_x = TILE
            x0 = (x0 // TILE + 1) * TILE
        elif math.pi * 2 >= cur_angle >= (math.pi / 2) * 3:  # верхний правый кусок торта
            step_x = TILE
            x0 = (x0 // TILE + 1) * TILE
        elif math.pi / 2 <= cur_angle <= math.pi:  # нижний левый кусок торта
            step_x = -TILE
            x0 = x0 // TILE * TILE
        elif math.pi <= cur_angle <= (math.pi / 2) * 3:  # верхний левый кусок торта
            step_x = -TILE
            x0 = x0 // TILE * TILE

        counted = x0 - _pos[0]
        # идем по горизонтале значит x0 += step_x
        y = y0
        x = _pos[0]
        draw = False
        for _ in range(int(math.fabs(MAX_DEPTH * math.cos(cur_angle) // TILE))):
            if _ == 0:
                y += counted * math.tan(cur_angle)

            if x0 - x == counted:
                x += counted

            if (x // TILE, y // TILE) in world_map:
                pygame.draw.line(sc, "green", _pos, (x // TILE * TILE, y), 2)
                draw = True
                break
            elif (x // TILE - 1, y // TILE) in world_map and step_x < 0:
                pygame.draw.line(sc, "green", _pos, (x // TILE * TILE, y), 2)
                draw = True
                break
            else:
                y = y0
                x = _pos[0]

            counted += step_x
            x += counted
            y += counted * math.tan(cur_angle)

        if not draw:
            pygame.draw.line(sc, "green", _pos, ((x + counted) // TILE * TILE, y + counted * math.tan(cur_angle)), 2)

        if cur_angle + DELTA_ANGLE > math.pi * 2:
            cur_angle = cur_angle + DELTA_ANGLE - math.pi * 2
        else:
            cur_angle += DELTA_ANGLE  # изменяем луч на след.

        x0, y0 = _pos  # позиция игрока


def ray_casting_vertical(sc, _pos, _angle):
    x0, y0 = _pos  # позиция игрока
    if _angle - HALF_FOV <= 0:
        cur_angle = math.pi * 2 + _angle - HALF_FOV
    else:
        cur_angle = _angle - HALF_FOV  # вычитаем половину из угла игрока и нормалью, чтобы взять 1 луч

    for ray in range(NUM_RAYS):
        step_y = 0
        angle = 0
        if math.pi / 2 >= cur_angle >= 0:  # нижний правый кусок торта
            step_y = TILE
            y0 = (y0 // TILE + 1) * TILE
        elif math.pi * 2 >= cur_angle >= (math.pi / 2) * 3:  # верхний правый кусок торта
            step_y = -TILE
            y0 = y0 // TILE * TILE
        elif math.pi / 2 <= cur_angle <= math.pi:  # нижний левый кусок торта
            step_y = TILE
            y0 = (y0 // TILE + 1) * TILE
        elif math.pi <= cur_angle <= (math.pi / 2) * 3:  # верхний левый кусок торта
            step_y = -TILE
            y0 = y0 // TILE * TILE

        counted = y0 - _pos[1]
        x = x0
        y = _pos[1]
        draw = False
        for _ in range(int(math.fabs(MAX_DEPTH * math.sin(cur_angle) // TILE))):
            if _ == 0:
                x += counted / math.tan(cur_angle)

            if y0 - y == counted:
                y += counted

            if (x // TILE, y // TILE) in world_map:
                pygame.draw.line(sc, "green", _pos, (x, y // TILE * TILE), 2)
                draw = True
                break
            elif (x // TILE, y // TILE - 1) in world_map and step_y < 0:
                pygame.draw.line(sc, "green", _pos, (x, y // TILE * TILE), 2)
                draw = True
                break
            else:
                x = x0
                y = _pos[1]

            counted += step_y
            y += counted
            x += counted / math.tan(cur_angle)

        if not draw:
            pygame.draw.line(sc, "green", _pos, (x + counted / math.tan(cur_angle), y + counted // TILE * TILE), 2)

        if cur_angle + DELTA_ANGLE > math.pi * 2:
            cur_angle = cur_angle + DELTA_ANGLE - math.pi * 2
        else:
            cur_angle += DELTA_ANGLE  # изменяем луч на след.

        x0, y0 = _pos  # позиция игрока


def ray_casting(sc, _pos, _angle):
    x0, y0 = _pos  # позиция игрока
    if _angle - HALF_FOV <= 0:
        cur_angle = math.pi * 2 + _angle - HALF_FOV
    else:
        cur_angle = _angle - HALF_FOV  # вычитаем половину из угла игрока и нормалью, чтобы взять 1 луч

    # print(world_map)
    for ray in range(NUM_RAYS):
        # определяем четверть в которой находится угол альфа
        #  math.pi / 2 - что-то типа 90 градусов
        step_x = 0
        if math.pi / 2 >= cur_angle >= 0:  # нижний правый кусок торта
            step_x = TILE
            x0 = (x0 // TILE + 1) * TILE
        elif math.pi * 2 >= cur_angle >= (math.pi / 2) * 3:  # верхний правый кусок торта
            step_x = TILE
            x0 = (x0 // TILE + 1) * TILE
        elif math.pi / 2 <= cur_angle <= math.pi:  # нижний левый кусок торта
            step_x = -TILE
            x0 = x0 // TILE * TILE
        elif math.pi <= cur_angle <= (math.pi / 2) * 3:  # верхний левый кусок торта
            step_x = -TILE
            x0 = x0 // TILE * TILE

        counted = x0 - _pos[0]
        # идем по горизонтале значит x0 += step_x
        y = y0
        x = _pos[0]
        draw = False
        pos = list()
        for _ in range(int(math.fabs(MAX_DEPTH * math.cos(cur_angle) // TILE))):
            if _ == 0:
                y += counted * math.tan(cur_angle)

            if x0 - x == counted:
                x += counted

            if (x // TILE, y // TILE) in world_map:
                draw = True
                pos.append((x // TILE * TILE, y))
                break
            elif (x // TILE - 1, y // TILE) in world_map and step_x < 0:
                draw = True
                pos.append((x // TILE * TILE, y))
                break
            else:
                y = y0
                x = _pos[0]

            counted += step_x
            x += counted
            y += counted * math.tan(cur_angle)

        if not draw:
            pos.append(((x + counted) // TILE * TILE, y + counted * math.tan(cur_angle)))

        if cur_angle + DELTA_ANGLE > math.pi * 2:
            cur_angle = cur_angle + DELTA_ANGLE - math.pi * 2
        else:
            cur_angle += DELTA_ANGLE  # изменяем луч на след.

        x0, y0 = _pos  # позиция игрока

        step_y = 0
        if math.pi / 2 >= cur_angle >= 0:  # нижний правый кусок торта
            step_y = TILE
            y0 = (y0 // TILE + 1) * TILE
        elif math.pi * 2 >= cur_angle >= (math.pi / 2) * 3:  # верхний правый кусок торта
            step_y = -TILE
            y0 = y0 // TILE * TILE
        elif math.pi / 2 <= cur_angle <= math.pi:  # нижний левый кусок торта
            step_y = TILE
            y0 = (y0 // TILE + 1) * TILE
        elif math.pi <= cur_angle <= (math.pi / 2) * 3:  # верхний левый кусок торта
            step_y = -TILE
            y0 = y0 // TILE * TILE

        counted = y0 - _pos[1]
        x = x0
        y = _pos[1]
        draw = False
        for _ in range(int(math.fabs(MAX_DEPTH * math.sin(cur_angle) // TILE))):
            if _ == 0:
                x += counted / math.tan(cur_angle)

            if y0 - y == counted:
                y += counted

            if (x // TILE, y // TILE) in world_map:
                draw = True
                pos.append((x, y // TILE * TILE))
                break
            elif (x // TILE, y // TILE - 1) in world_map and step_y < 0:
                draw = True
                pos.append((x, y // TILE * TILE))
                break
            else:
                x = x0
                y = _pos[1]

            counted += step_y
            y += counted
            x += counted / math.tan(cur_angle)

        if not draw:
            pos.append((x + counted / math.tan(cur_angle), y + counted // TILE * TILE))

        if cur_angle + DELTA_ANGLE > math.pi * 2:
            cur_angle = cur_angle + DELTA_ANGLE - math.pi * 2
        else:
            cur_angle += DELTA_ANGLE  # изменяем луч на след.

        x0, y0 = _pos  # позиция игрока

        if math.sqrt((pos[0][0] - _pos[0]) ** 2 + (pos[0][1] - _pos[1]) ** 2) <\
                math.sqrt((pos[1][0] - _pos[0]) ** 2 + (pos[1][1] - _pos[1]) ** 2):
            pygame.draw.line(sc, "green", _pos, pos[0], 2)
        else:
            pygame.draw.line(sc, "green", _pos, pos[1], 2)
