from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

class CursosTequixquiacApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "**", "%"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = GridLayout(cols=1)

        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=50
        )

        main_layout.add_widget(self.solution)


        buttons = [
            ["Carpintería", "Sistemas", "Inglés", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "⌫"], 
            ["+", "^", "√", "%"],
            ["π"]                   
        ]

        for row in buttons:
           
            cols_count = 4 if len(row) == 4 else len(row)
            h_layout = GridLayout(cols=cols_count)

            for label in row:
                button = Button(text=label)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)

            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=",
            font_size=32
        )

        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "⌫": 
            self.solution.text = current[:-1]
        elif button_text == "π":  
            self.solution.text = current + str(math.pi)
        elif button_text == "√":
            try:
                if current:
                    self.solution.text = str(math.sqrt(float(current)))
            except Exception:
                self.solution.text = "Error"
        elif button_text == "^":
            self.solution.text = current + "**"
        else:
            self.solution.text = current + button_text

    def on_solution(self, instance):
        text = self.solution.text
        try:
            if "%" in text:
                text = text.replace("%", "/100")
            
            solution = str(eval(text))
            self.solution.text = solution
        except Exception:
            self.solution.text = "Error"

if __name__ == "__main__":
    CursosTequixquiacApp().run()
