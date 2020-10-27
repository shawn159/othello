from bangtal import *
import time

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

game_scene = Scene('Othello', 'Images/background.png')
transparent_screen = Object('Images/transparent_screen.png')

BLANK = -1
BLACK = 0
WHITE = 1

BLACK_POS = 3
WHITE_POS = 4

BASE = 40
LEN = 80

BLK_SCR_BASE_X = 760
BLK_SCR_BASE_Y = 220
WHT_SCR_BASE_X = 1080
WHT_SCR_BASE_Y = 220
SCR_LEN = 65

turn = BLACK
black_can_move = True
white_can_move = True
finish_status = False

blank_img = 'Images/blank.png'
black_pos_img = 'Images/black possible.png'
white_pos_img = 'Images/white possible.png'
black_img = 'Images/black.png'
white_img = 'Images/white.png'

game_data = []
game_img = []
black_score_img = []
white_score_img = []
possible_list = []

for j in range(8):
    row_data = []
    row_img = []
    for i in range(8):
        row_data.append(-1)
        row_img.append(Object(blank_img))
    game_data.append(row_data)
    game_img.append(row_img)

def init_game():
    game_data[3][3] = BLACK
    game_img[3][3] = Object(black_img)
    game_img[3][3].locate(game_scene, BASE + 3 * LEN, BASE + 3 * LEN)
    game_img[3][3].show()
    game_data[4][4] = BLACK
    game_img[4][4] = Object(black_img)
    game_img[4][4].locate(game_scene, BASE + 4 * LEN, BASE + 4 * LEN)
    game_img[4][4].show()
    game_data[4][3] = WHITE
    game_img[4][3] = Object(white_img)
    game_img[4][3].locate(game_scene, BASE + 3 * LEN, BASE + 4 * LEN)
    game_img[4][3].show()
    game_data[3][4] = WHITE
    game_img[3][4] = Object(white_img)
    game_img[3][4].locate(game_scene, BASE + 4 * LEN, BASE + 3 * LEN)
    game_img[3][4].show()

    show_score()

def change_state(x, y, state):
    if state == BLACK:
        game_data[y][x] = BLACK
        game_img[y][x].hide()
        game_img[y][x] = Object((black_img))
        game_img[y][x].locate(game_scene, BASE + x * LEN, BASE + y * LEN)
        game_img[y][x].show()
    elif state == WHITE:
        game_data[y][x] = WHITE
        game_img[y][x].hide()
        game_img[y][x] = Object((white_img))
        game_img[y][x].locate(game_scene, BASE + x * LEN, BASE + y * LEN)
        game_img[y][x].show()
    elif state == BLANK:
        game_data[y][x] = BLANK
        game_img[y][x].hide()
        game_img[y][x] = Object((blank_img))
        game_img[y][x].locate(game_scene, BASE + x * LEN, BASE + y * LEN)
        game_img[y][x].show()
    elif state == BLACK_POS:
        game_data[y][x] = BLACK_POS
        game_img[y][x].hide()
        game_img[y][x] = Object((black_pos_img))
        game_img[y][x].locate(game_scene, BASE + x * LEN, BASE + y * LEN)
        game_img[y][x].show()
    elif state == WHITE_POS:
        game_data[y][x] = WHITE_POS
        game_img[y][x].hide()
        game_img[y][x] = Object((white_pos_img))
        game_img[y][x].locate(game_scene, BASE + x * LEN, BASE + y * LEN)
        game_img[y][x].show()
    else:
        pass

def possible_move_check():
    global possible_list
    global turn
    global black_can_move
    global white_can_move

    possible_list = []
    for j in range(8):
        for i in range(8):
            if game_data[j][i] == turn:
                other_color_check = False
                x = i + 1
                y = j
                while x < 8:
                    if game_data[y][x] == turn:
                        break
                    elif game_data[y][x] == BLANK:
                        if other_color_check:
                            possible_list.append(y * 8 + x)
                        break
                    else:
                        other_color_check = True
                        x += 1
                other_color_check = False
                x = i + 1
                y = j + 1
                while x < 8 and y < 8:
                    if game_data[y][x] == turn:
                        break
                    elif game_data[y][x] == BLANK:
                        if other_color_check:
                            possible_list.append(y * 8 + x)
                        break
                    else:
                        other_color_check = True
                        x += 1
                        y += 1
                other_color_check = False
                x = i
                y = j + 1
                while y < 8:
                    if game_data[y][x] == turn:
                        break
                    elif game_data[y][x] == BLANK:
                        if other_color_check:
                            possible_list.append(y * 8 + x)
                        break
                    else:
                        other_color_check = True
                        y += 1
                other_color_check = False
                x = i - 1
                y = j + 1
                while x >= 0 and y < 8:
                    if game_data[y][x] == turn:
                        break
                    elif game_data[y][x] == BLANK:
                        if other_color_check:
                            possible_list.append(y * 8 + x)
                        break
                    else:
                        other_color_check = True
                        x -= 1
                        y += 1
                other_color_check = False
                x = i - 1
                y = j
                while x >= 0:
                    if game_data[y][x] == turn:
                        break
                    elif game_data[y][x] == BLANK:
                        if other_color_check:
                            possible_list.append(y * 8 + x)
                        break
                    else:
                        other_color_check = True
                        x -= 1
                other_color_check = False
                x = i - 1
                y = j - 1
                while x >= 0 and y >= 0:
                    if game_data[y][x] == turn:
                        break
                    elif game_data[y][x] == BLANK:
                        if other_color_check:
                            possible_list.append(y * 8 + x)
                        break
                    else:
                        other_color_check = True
                        x -= 1
                        y -= 1
                other_color_check = False
                x = i
                y = j - 1
                while y >= 0:
                    if game_data[y][x] == turn:
                        break
                    elif game_data[y][x] == BLANK:
                        if other_color_check:
                            possible_list.append(y * 8 + x)
                        break
                    else:
                        other_color_check = True
                        y -= 1
                other_color_check = False
                x = i + 1
                y = j - 1
                while x < 8 and y >= 0:
                    if game_data[y][x] == turn:
                        break
                    elif game_data[y][x] == BLANK:
                        if other_color_check:
                            possible_list.append(y * 8 + x)
                        break
                    else:
                        other_color_check = True
                        x += 1
                        y -= 1

    if not possible_list:
        finish_control()
    else:
        for idx in possible_list:
            x = idx % 8
            y = idx // 8
            if turn == BLACK:
                black_can_move = True
                change_state(x, y, BLACK_POS)
            else :
                white_can_move = True
                change_state(x, y, WHITE_POS)


def flip_stone(i, j):
    global turn
    global possible_list

    for idx in possible_list:
        x = idx % 8
        y = idx // 8
        change_state(x, y, BLANK)

    target_list = []
    temp = []
    x = i + 1
    y = j
    while x < 8:
        if game_data[y][x] == turn:
            target_list += temp
            break
        elif game_data[y][x] == BLANK:
            break
        else:
            temp.append(y * 8 + x)
            x += 1
    temp = []
    x = i + 1
    y = j + 1
    while x < 8 and y < 8:
        if game_data[y][x] == turn:
            target_list += temp
            break
        elif game_data[y][x] == BLANK:
            break
        else:
            temp.append(y * 8 + x)
            x += 1
            y += 1
    temp = []
    x = i
    y = j + 1
    while y < 8:
        if game_data[y][x] == turn:
            target_list += temp
            break
        elif game_data[y][x] == BLANK:
            break
        else:
            temp.append(y * 8 + x)
            y += 1
    temp = []
    x = i - 1
    y = j + 1
    while x >= 0 and y < 8:
        if game_data[y][x] == turn:
            target_list += temp
            break
        elif game_data[y][x] == BLANK:
            break
        else:
            temp.append(y * 8 + x)
            x -= 1
            y += 1
    temp = []
    x = i - 1
    y = j
    while x >= 0:
        if game_data[y][x] == turn:
            target_list += temp
            break
        elif game_data[y][x] == BLANK:
            break
        else:
            temp.append(y * 8 + x)
            x -= 1
    temp = []
    x = i - 1
    y = j - 1
    while x >= 0 and y >= 0:
        if game_data[y][x] == turn:
            target_list += temp
            break
        elif game_data[y][x] == BLANK:
            break
        else:
            temp.append(y * 8 + x)
            x -= 1
            y -= 1
    temp = []
    x = i
    y = j - 1
    while y >= 0:
        if game_data[y][x] == turn:
            target_list += temp
            break
        elif game_data[y][x] == BLANK:
            break
        else:
            temp.append(y * 8 + x)
            y -= 1
    temp = []
    x = i + 1
    y = j - 1
    while x < 8 and y >= 0:
        if game_data[y][x] == turn:
            target_list += temp
            break
        elif game_data[y][x] == BLANK:
            break
        else:
            temp.append(y * 8 + x)
            x += 1
            y -= 1

    target_list.append(i + j * 8)

    for idx in target_list:
        x = idx % 8
        y = idx // 8
        change_state(x, y, turn)

def score_check():
    black_score = 0
    white_score = 0
    for j in range(8):
        for i in range(8):
            if game_data[j][i] == BLACK:
                black_score += 1
            elif game_data[j][i] == WHITE:
                white_score += 1
            else:
                pass
    return black_score, white_score

def show_score():
    global black_score_img
    global white_score_img

    for img in black_score_img:
        img.hide()
    for img in white_score_img:
        img.hide()
    black_score_img = []
    white_score_img = []

    black_score, white_score = score_check()

    for idx, num in enumerate(str(black_score)[::1]):
        file_name = 'Images/L' + num + '.png'
        number = Object(file_name)
        number.locate(game_scene, BLK_SCR_BASE_X + idx * SCR_LEN, BLK_SCR_BASE_Y)
        number.show()
        black_score_img.append(number)

    for idx, num in enumerate(str(white_score)[::1]):
        file_name = 'Images/L' + num + '.png'
        number = Object(file_name)
        number.locate(game_scene, WHT_SCR_BASE_X + idx * SCR_LEN, WHT_SCR_BASE_Y)
        number.show()
        black_score_img.append(number)

def finish_control():
    global turn
    global black_can_move
    global white_can_move
    global transparent_screen
    global finish_status
    if turn == BLACK:
        black_can_move = False
        if white_can_move:
            turn = WHITE
            possible_move_check()
    else:
        white_can_move = False
        if black_can_move:
            turn = BLACK
            possible_move_check()
    if not black_can_move and not white_can_move:
        black_score, white_score = score_check()
        if black_score > white_score:
            showMessage('검은색이 승리했습니다!!')
        elif black_score < white_score:
            showMessage('희색이 승리했습니다!!')
        else:
            showMessage('비겼습니다!!')
        finish_status = True

def ai_location_select():
    global turn
    global possible_list

    flip_stone_count = []
    for idx in possible_list:
        i = idx % 8
        j = idx // 8
        target_list = []
        temp = []
        x = i + 1
        y = j
        while x < 8:
            if game_data[y][x] == turn:
                target_list += temp
                break
            elif game_data[y][x] == BLANK:
                break
            else:
                temp.append(y * 8 + x)
                x += 1
        temp = []
        x = i + 1
        y = j + 1
        while x < 8 and y < 8:
            if game_data[y][x] == turn:
                target_list += temp
                break
            elif game_data[y][x] == BLANK:
                break
            else:
                temp.append(y * 8 + x)
                x += 1
                y += 1
        temp = []
        x = i
        y = j + 1
        while y < 8:
            if game_data[y][x] == turn:
                target_list += temp
                break
            elif game_data[y][x] == BLANK:
                break
            else:
                temp.append(y * 8 + x)
                y += 1
        temp = []
        x = i - 1
        y = j + 1
        while x >= 0 and y < 8:
            if game_data[y][x] == turn:
                target_list += temp
                break
            elif game_data[y][x] == BLANK:
                break
            else:
                temp.append(y * 8 + x)
                x -= 1
                y += 1
        temp = []
        x = i - 1
        y = j
        while x >= 0:
            if game_data[y][x] == turn:
                target_list += temp
                break
            elif game_data[y][x] == BLANK:
                break
            else:
                temp.append(y * 8 + x)
                x -= 1
        temp = []
        x = i - 1
        y = j - 1
        while x >= 0 and y >= 0:
            if game_data[y][x] == turn:
                target_list += temp
                break
            elif game_data[y][x] == BLANK:
                break
            else:
                temp.append(y * 8 + x)
                x -= 1
                y -= 1
        temp = []
        x = i
        y = j - 1
        while y >= 0:
            if game_data[y][x] == turn:
                target_list += temp
                break
            elif game_data[y][x] == BLANK:
                break
            else:
                temp.append(y * 8 + x)
                y -= 1
        temp = []
        x = i + 1
        y = j - 1
        while x < 8 and y >= 0:
            if game_data[y][x] == turn:
                target_list += temp
                break
            elif game_data[y][x] == BLANK:
                break
            else:
                temp.append(y * 8 + x)
                x += 1
                y -= 1
    
        target_list.append(i + j * 8)
        flip_stone_count.append(len(target_list))

    return possible_list[flip_stone_count.index(max(flip_stone_count))]

def ai_move():
    location = ai_location_select()
    x = location % 8
    y = location // 8

    game_control(x, y)


def game_control(x, y):
    global possible_list
    global turn
    global finish_status
    global transparent_screen
    index = y * 8 + x
    if index in possible_list:
        flip_stone(x, y)
        if turn == BLACK:
            turn = WHITE
        else:
            turn = BLACK
        possible_move_check()
        show_score()
        if finish_status:
            transparent_screen.hide()
        else:
            reset_transparent_screen()
            ##########
            #If erase this part, you can play without AI
            if turn == WHITE:
                ai_move()
            ##########
    else:
        showMessage('해당 위치는 놓을 수 없습니다')

def reset_transparent_screen():
    global transparent_screen
    transparent_screen.hide()
    del transparent_screen
    transparent_screen = Object('Images/transparent_screen.png')
    transparent_screen.locate(game_scene, 40, 40)
    transparent_screen.show()
    transparent_screen.onMouseAction = transparent_screen_on_click

def transparent_screen_on_click(x, y, action):
    idx_x = x // 80
    idx_y = y // 80
    game_control(idx_x, idx_y)

init_game()
possible_move_check()
reset_transparent_screen()
startGame(game_scene)