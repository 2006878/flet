import flet as ft

def main(page):

    first_name = ft.TextField(label="Primeiro Nome", autofocus=True)
    last_name = ft.TextField(label="Sobrenome")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Olá, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Diga olá!", on_click=btn_click),
        greetings,
    )

ft.app(target=main)