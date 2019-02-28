import sys
sys.path.insert(0, '../bomberman')


def nodevalue(world, player):
    value = 0
    actions = world.events

    # exit found or character lost?
    for a in actions:
        if a.tpe == a.CHARACTER_FOUND_EXIT:
            return 11111
        elif a.tpe == a.BOMB_HIT_CHARACTER or a.tpe == a.CHARACTER_KILLED_BY_MONSTER:
            return -11111
        else:
            value += 2

    # current coordinates of the character in the world
    x = player.x
    y = player.y
    # WOULD THIS WORK????
    # x = world.me().x
    # y = world.me().y

    # are there monsters, bombs, or walls near the character?
    if y-3 >= 0:
        ylower = y-3
    elif y-2 >= 0:
        ylower = y-2
    elif y-1 >= 0:
        ylower = y-1
    else:
        ylower = 0
    if y+3 < world.width():
        yupper = y+3
    elif y+2 < world.width():
        yupper = y+2
    elif y+1 < world.width():
        yupper = y+1
    else:
        yupper = world.width()
    if x-3 >= 0:
        xlower = x-3
    elif x-2 >= 0:
        xlower = x-2
    elif x-1 >= 0:
        xlower = x-1
    else:
        xlower = 0
    if x+3 < world.height():
        xupper = x+3
    elif x+2 < world.height():
        xupper = x+2
    elif x+1 < world.height():
        xupper = x+1
    else:
        xupper = world.height()

    for n in range(ylower, yupper):
        for m in range(xlower, xupper):
            if world.empty_at(m, n):
                value += 5
            else:
                if world.monsters_at(m, n) or world.bomb_at(m, n):
                    value -= 20
                elif world.exit_at(m, n):
                    value += 50
                else:  # wall, other character, explosion
                    value -= 3

    # for m in world.monsters:
    #     for b in world.bombs:
    #         if y-2 >= 0:
    #             if m.y != y-2:
    #                 value += 5
    #             else:
    #                 if x-2 >= 0:
    #                     if m.x != x-2:
    #                         value += 5
    #                     else:
    #                         value -= 2 * m.x
    #                 if x+2 < world.height():
    #                     if m.x != x+2:
    #                         value += 5
    #                     else:
    #                         value -= 2 * m.x
    #             if b.y != y-2:
    #                 value += 5
    #             else:
    #                 if x-2 >= 0:
    #                     if b.x != x-2:
    #                         value += 5
    #                     else:
    #                         value -= 2 * b.x
    #                 if x+2 < world.height():
    #                     if b.x != x+2:
    #                         value += 5
    #                     else:
    #                         value -= 2 * b.x
    #             if world.exit_at(x, y-2) or world.exit_at(x-2, y-2) or world.exit_at(x+2, y-2):
    #                 value += 7
    #         if y+2 < world.width():
    #             if m.y != y+2:
    #                 value += 5
    #             else:
    #                 if x-2 >= 0:
    #                     if m.x != x-2:
    #                         value += 5
    #                     else:
    #                         value -= 2 * m.x
    #                 if x+2 < world.height():
    #                     if m.x != x+2:
    #                         value += 5
    #                     else:
    #                         value -= 2 * m.x
    #             if b.y != y+2:
    #                 value += 5
    #             else:
    #                 if x-2 >= 0:
    #                     if b.x != x-2:
    #                         value += 5
    #                     else:
    #                         value -= 2 * b.x
    #                 if x+2 < world.height():
    #                     if b.x != x+2:
    #                         value += 5
    #                     else:
    #                         value -= 2 * b.x
    #             if world.exit_at(x, y+2) or world.exit_at(x-2, y+2) or world.exit_at(x+2, y+2):
    #                 value += 7

    # is the character cornered?
    if x == 0 or x == world.width():
        if y == 0 or y == world.height():
            value -= 20

    return value
