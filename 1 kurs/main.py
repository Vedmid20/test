import flet as ft
import random



sqrt = ' **0.5 '
diyaLVL1 = ['+', '-']
diyaLVL2 = ['+', '-', '*', '/']
diyaLVL3 = ['+', '-', '*', '/', sqrt]
equation = []
eq = ''
res = ''
def main(page: ft.Page):
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   page.window_resizable = False
   page.bgcolor = 'indigo300'
   page.window_width = 450
   page.window_height = 350
   t = ft.Text('Enter result', size=30, font_family='SimSun')
   page.update()

   def lvl1(e):
       global random_length , eq, res
       page.clean()
       random_length = random.randint(2, 4)
       x = 0
       while x != random_length:
           x += 1
           random_num = random.randint(1, 150)
           random_diya = random.choice(diyaLVL1)
           random_num = str(random_num)
           equation.append(random_num)
           equation.append(random_diya)
       for i in equation:
           eq += str(i)
       if eq.endswith('-') or eq.endswith('+'):
           res = eq[:-1]
       eq_text = ft.Text(value=res, size=33, color='white')
       inputResult = ft.TextField(label='Enter result', border_color='white', height=45)
       page.add(ft.Row([
           eq_text

       ], alignment=ft.MainAxisAlignment.CENTER
       ))

       def result(e):
           global res
           if str(inputResult.value) == eval(res):
               inputResult.border_color = 'green'
               inputResult.label = 'Result true'
           else:
               inputResult.border_color = 'red'
               inputResult.label = 'Result not true'
           page.update()

       page.add(ft.Row([
           inputResult,
           ft.ElevatedButton(text='Done', bgcolor='white', color='indigo400', width=100, height=45, on_click=result)
       ]))

       page.update()

   page.add(ft.Row([
       # t
   ]))
   page.add(ft.Row([
       ft.ElevatedButton('Level Easy',on_click = lvl1, width=150, height=45, color='indigo400', bgcolor='white')
   ], alignment=ft.MainAxisAlignment.CENTER))
   page.add(ft.Row([
       ft.ElevatedButton('Level Normal', width=150, height=45, color='indigo400', bgcolor='white')
   ], alignment=ft.MainAxisAlignment.CENTER))
   page.add(ft.Row([
       ft.ElevatedButton('Level Hard', width=150, height=45, color='indigo400', bgcolor='white700')
   ], alignment=ft.MainAxisAlignment.CENTER))


if __name__ == '__main__':
   ft.app(target=main)