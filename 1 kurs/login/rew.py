import flet as ft
import time


def main(page: ft.Page):
    page.theme_mode='dark'
    c1 = ft.Container(
        width=50, height=50, bgcolor="purple", top=300, left=745, animate_position=500, border_radius=40)

    c2 = ft.Container(
        width=50, height=50, bgcolor="blue", top=300, left=700, animate_position=500, border_radius=40
    )

    x = 0
    while x != 5:
        x += 1
        c1.top = 300
        c1.left = 790
        c2.top = 300
        c2.left = 690
        time.sleep(0.4)
        page.update()
        c1.top = 300
        c1.left = 690
        c2.top = 300
        c2.left = 790
        time.sleep(0.4)
        page.update()

        page.add(ft.Row([ft.Stack([c1, c2], height=700)], alignment=ft.MainAxisAlignment.CENTER)
        )

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))
            with open('passwd.txt', 'w', encoding='utf-8') as file:
                file.write(f'{txt_name.value}')

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))


ft.app(target=main)