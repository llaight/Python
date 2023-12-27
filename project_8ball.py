import random
import flet as ft

magic_8ans = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely","You may rely on it",
              "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again","Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don’t count on it","My reply is no","My sources say no","Outlook not so good", "Very doubtful"]

def main (page: ft.Page):
    page.vertical_alignment= "center"
    page.horizontal_alignment= "center"

    icon= ft.Icon(name=ft.icons.FILTER_8_ROUNDED, color=ft.colors.WHITE, size=80)
    txt= ft.Text(value="Welcome to the Magic 8 Ball!", text_align=ft.TextAlign.CENTER, size=25,weight=ft.FontWeight.W_700)
    input= ft.TextField(label="Enter your wishes", width=300, border_color="#E95793")

    def btn(e):
            text.value=f"\n{random.choice(magic_8ans)}"
            page.update()

    button= ft.ElevatedButton("Roll your wish", on_click=btn)
    text= ft.Text()
    row= ft.Row(controls=[icon],alignment=ft.MainAxisAlignment.CENTER)
    row1= ft.Row(controls=[button], alignment=ft.MainAxisAlignment.CENTER)
    page.update()
    page.window_width=400
    page.window_height=400
    page.title = "Magic 8 Ball"
    page.add(row,txt, input, row1, text)

ft.app(target=main)
