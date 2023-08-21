import flet
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):
    page.title = "Flet Counter"
    page.vertical_aligment = "Center"

    txt_number = TextField(value = "0", text_align = "right",
    width=100)

    def minus_button(event):
        txt_number.value = int(txt_number.value) - 1 
        page.update()

    def plus_button(event):
        txt_number.value = int(txt_number.value) + 1     
        page.update()

    page.add(
        Row(
            [IconButton(icons.REMOVE, on_click = minus_button),
            txt_number,
            IconButton(icons.ADD, on_click = plus_button)
            ],
            alignment = "center",
        )
    )
    flet.app(target = main)
