import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class TuningApp(App):
    def build(self):
        self.tuning_list = []

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.title_input = TextInput(hint_text='Nome da Peça', multiline=False)
        self.layout.add_widget(self.title_input)

        self.description_input = TextInput(hint_text='Descrição', multiline=True)
        self.layout.add_widget(self.description_input)

        self.add_button = Button(text='Adicionar Tunagem')
        self.add_button.bind(on_press=self.add_tuning)
        self.layout.add_widget(self.add_button)

        self.remove_button = Button(text='Remover Tunagem')
        self.remove_button.bind(on_press=self.remove_tuning)
        self.layout.add_widget(self.remove_button)

        self.tuning_label = Label(text='Tunagens:', size_hint_y=None, height=40)
        self.layout.add_widget(self.tuning_label)

        self.tuning_display = Label(text='', size_hint_y=None)
        self.layout.add_widget(self.tuning_display)

        return self.layout

    def add_tuning(self, instance):
        title = self.title_input.text
        description = self.description_input.text

        if title and description:
            self.tuning_list.append(f'{title}: {description}')
            self.update_display()
            self.title_input.text = ''
            self.description_input.text = ''
        else:
            self.show_popup('Erro', 'Por favor, preencha todos os campos.')

    def remove_tuning(self, instance):
        if self.tuning_list:
            self.tuning_list.pop()
            self.update_display()
        else:
            self.show_popup('Erro', 'Não há tunagens para remover.')

    def update_display(self):
        self.tuning_display.text = '\n'.join(self.tuning_list)

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 100))
        popup.open()

if __name__ == '__main__':
    TuningApp().run()