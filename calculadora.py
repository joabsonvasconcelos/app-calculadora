
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(
            readonly=True, halign="right", font_size=55, multiline=False
        )
        layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.6))
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "=", "+"
        ]
        for button in buttons:
            button_instance = Button(
                text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
            button_instance.bind(on_press=self.on_button_press)
            layout.add_widget(button_instance)

        equals_button = Button(
            text="=", pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        layout.add_widget(self.result)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = ""
        else:
            new_text = current + button_text
            self.result.text = new_text

    def on_solution(self, instance):
        text = self.result.text
        try:
            # Substituir 'x' por '*' para permitir entrada de '*' para multiplicação
            text = text.replace("x", "*")
            solution = str(eval(text))
            self.result.text = solution
        except Exception:
            self.result.text = "Erro"


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
