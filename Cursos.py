from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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
            font_size=40
        )

        main_layout.add_widget(self.solution)

        buttons = [
            ["Carpintería", "Sistemas", "Inglés", "Borrar"],
            ["Electricidad", "Contabilidad", "Cocina", "Info"],
            ["Mecánica", "Costura", "Belleza", "Atrás"],
            ["Inscribir"]
        ]

        for row in buttons:
            columnas = 1 if len(row) == 1 else 4
            h_layout = GridLayout(cols=columnas)
            for label in row:
                button = Button(text=label)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="Confirmar Selección",
            font_size=25,
            size_hint=(1, 0.2)
        )

        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text.strip() 
        button_text = instance.text

        if button_text == "Borrar":
            self.solution.text = ""
        
        elif button_text == "Atrás": 
            if current and not current.startswith("Registrado") and not current.startswith("Seleccione"):
               
                cursos = current.split()
                cursos.pop()
                self.solution.text = " ".join(cursos)
            else:
                self.solution.text = ""
                
        elif button_text == "Info":  
            self.solution.text = "Información del plantel v1.0"
            
        elif button_text == "Inscribir": 
            self.on_solution(instance)
            
        else:
            
            if current == "Seleccione un curso" or current.startswith("Registrado") or current == "Información del plantel v1.0":
                current = ""
            
            
            if current:
                self.solution.text = current + " " + button_text
            else:
                self.solution.text = button_text

    def on_solution(self, instance):
        text = self.solution.text.strip()
        if text and not text.startswith("Seleccione") and not text.startswith("Información"):
         
            if text.startswith("Registrado en:"):
                self.solution.text = text
            else:
                self.solution.text = "Registrado en: " + text
        else:
            self.solution.text = "Seleccione un curso"

if __name__ == "__main__":
    CursosTequixquiacApp().run()
