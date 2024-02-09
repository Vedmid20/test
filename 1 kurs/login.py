import flet as ft


def main(page: ft.Page):
    page.theme_mode = 'dark'
    t = ft.Text(value='Enter your data', size=30)
    name = ft.TextField(label='Enter name', width=410, height=50)
    month = ft.TextField(label='Month', width=200, height=50)
    year = ft.TextField(label='Year', width=200, height=50)

    page.update()
    page.add(ft.Row([
        t
    ]))
    page.add(ft.Row([
        name
    ]))
    page.add(ft.Row([
        month, year
    ]))


ft.app(target=main)