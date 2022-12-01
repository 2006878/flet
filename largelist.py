# import flet as ft

# def main(page: ft.Page):
#     for i in range(5000):
#         page.controls.append(ft.Text(f"Line {i}"))
#     page.scroll = "always"
#     page.update()

# ft.app(target=main, view=ft.WEB_BROWSER)

import flet as ft

def main(page: ft.Page):
    lv = ft.ListView(expand=True, spacing=10)
    for i in range(5000):
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)

ft.app(target=main, view=ft.WEB_BROWSER)