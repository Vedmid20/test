import flet as ft
import time

calc = ''
def main(page: ft.Page):
    output_text = ft.Text(color='blue800', size=50)
    page.add(output_text)
    page.update()
    def num1(e):
        global calc
        calc += '1'
        output_text.value = calc
        page.update()
    def num2(e):
        global calc
        calc += '2'
        output_text.value = calc
        page.update()
    def num3(e):
        global calc
        calc += '3'
        output_text.value = calc
        page.update()
    def plus(e):
        global calc
        calc += '+'
        output_text.value = calc
        page.update()
    def rez(e):
        global calc
        calc = eval(calc)
        round(calc, 5)
        output_text.value = str(calc)
        page.update()
    def minus(e):
        global calc
        calc += '-'
        output_text.value = calc
        page.update()
    def mnog(e):
        global calc
        calc += '*'
        output_text.value = calc
        page.update()
    def dil(e):
        global calc
        calc += '/'
        output_text.value = calc
        page.update()
    def num4(e):
        global calc
        calc += '4'
        output_text.value = calc
        page.update()
    def num5(e):
        global calc
        calc += '5'
        output_text.value = calc
        page.update()
    def num6(e):
        global calc
        calc += '6'
        output_text.value = calc
        page.update()
    def num7(e):
        global calc
        calc += '7'
        output_text.value = calc
        page.update()
    def num8(e):
        global calc
        calc += '8'
        output_text.value = calc
        page.update()
    def num9(e):
        global calc
        calc += '9'
        output_text.value = calc
        page.update()
    def num0(e):
        global calc
        calc += '0'
        output_text.value = calc
        page.update()
    def clr(e):
        global calc
        calc = ''
        output_text.value = calc
        page.update()
    def krapka(e):
        global calc
        calc += '.'
        output_text.value = calc
        page.update()
    def backspace(e):
        global calc
        calc = calc[:-1]
        output_text.value = calc
        page.update()
    def num_pi(e):
        global calc
        calc += '3.14'
        output_text.value = calc
        page.update()
    def mustFunctional(e):
        page.window_width = 355; page.window_height = 380
        time.sleep(0.1)
        page.update()
    def lowerFunctional(e):
        page.window_width = 290; page.window_height = 340
        time.sleep(0.1)
        page.update()
    def sqrt(e):
        global  calc
        calc = int(calc) ** 0.5
        output_text.value = round(calc,  5)
        page.update()
    def num_e(e):
        global calc
        calc += '2.71'
        output_text.value = calc
        page.update()
    def stepen(e):
        global calc
        calc = int(calc) ** 2
        output_text.value = calc
        page.update()


    page.theme_mode = 'light'
    page.window_width = 290; page.window_height = 340
    page.window_resizable = False

    page.add(ft.Row([
        ft.ElevatedButton('C', on_click=clr, bgcolor='RED300', width=79),
        ft.ElevatedButton('↩', on_click=backspace, bgcolor='RED300', width=79),
        ft.ElevatedButton('↪', on_click=mustFunctional, bgcolor='RED300', width=79),
        ft.ElevatedButton('↩', on_click=lowerFunctional, bgcolor='RED300', width=59),
    ]))
    page.add(ft.Row([
        ft.ElevatedButton('1', on_click=num1, bgcolor='AMBER100'),
        ft.ElevatedButton('2', on_click=num2, bgcolor='AMBER100'),
        ft.ElevatedButton('3', on_click=num3, bgcolor='AMBER100'),
        ft.ElevatedButton('+', on_click=plus, bgcolor='RED300', width=59),
        ft.ElevatedButton('π', on_click=num_pi, bgcolor='AMBER100', width=59)
    ]))
    page.add(ft.Row([
        ft.ElevatedButton('4', on_click=num4, bgcolor='AMBER100'),
        ft.ElevatedButton('5', on_click=num5, bgcolor='AMBER100'),
        ft.ElevatedButton('6', on_click=num6, bgcolor='AMBER100'),
        ft.ElevatedButton('-', on_click=minus, bgcolor='RED300', width=59),
        ft.ElevatedButton('√', on_click=sqrt, bgcolor='AMBER100', width=59)
    ]))
    page.add(ft.Row([
        ft.ElevatedButton('7', on_click=num7, bgcolor='AMBER100'),
        ft.ElevatedButton('8', on_click=num8, bgcolor='AMBER100'),
        ft.ElevatedButton('9', on_click=num9, bgcolor='AMBER100'),
        ft.ElevatedButton('*', on_click=mnog, bgcolor='RED300', width=59),
        ft.ElevatedButton('e', on_click=num_e, bgcolor='AMBER100', width=59)
    ]))
    page.add(ft.Row([
        ft.ElevatedButton('.', on_click=krapka, bgcolor='RED300'),
        ft.ElevatedButton('0', on_click=num0, bgcolor='AMBER100'),
        ft.ElevatedButton('/', on_click=dil, bgcolor='RED300'),
        ft.ElevatedButton('=', on_click=rez, bgcolor='RED300', width=59),
        ft.ElevatedButton('ⁿ', on_click=stepen, bgcolor='AMBER100', width=59)
    ]))

ft.app(target=main)