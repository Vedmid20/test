import flet as ft
import random


diya = ['+', '-', '*', '/']
equation = []
def main(page: ft.Page):
    page.window_resizable = False
    page.theme_mode = 'dark'
    page.window_width = 450
    page.window_height = 350
    t = ft.Text('Enter result', size=30, font_family='SimSun')
    page.update()

    def lvl1(e):
        global random_length
        page.clean()
        random_length = random.randint(1, 2)
        x = 0
        while x != random_length:
            x += 1
            random_num = random.randint(1, 200)
            random_diya = random.choice(diya)
            random_num = str(random_num)
            equation.append(random_num)
            equation.append(random_diya)
        print(*equation)
        page.update()
    page.add(ft.Row([

    ]))
    page.add(ft.Row([
        ft.ElevatedButton('Level Easy',on_click = lvl1, width=150, height=45, color='green300', bgcolor='grey900')
    ]))
    page.add(ft.Row([
        ft.ElevatedButton('Level Normal', width=150, height=45, color='yellow200', bgcolor='grey900')
    ]))
    page.add(ft.Row([
        ft.ElevatedButton('Level Hard', width=150, height=45, color='red300', bgcolor='grey900')
    ]))

    page.add(ft.Row([
        t
    ]))


if __name__ == '__main__':
    ft.app(target=main)