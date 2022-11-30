import flet as ft

def main(page):

    page.title = "Lista de tarefas"
    page.vertical_aligment = ft.MainAxisAlignment.CENTER

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="O que tem pra fazer hoje?", width=200)
    page.add(ft.Row([new_task, ft.ElevatedButton("Adicionar", on_click=add_clicked)], alignment=ft.MainAxisAlignment.CENTER))
    

ft.app(target=main)    

