import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox

class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

class GerenciadorDeTarefasApp(App):
    def build(self):
        self.tarefas = []

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.titulo_input = TextInput(hint_text='Título da Tarefa', multiline=False)
        self.layout.add_widget(self.titulo_input)

        self.descricao_input = TextInput(hint_text='Descrição da Tarefa', multiline=True)
        self.layout.add_widget(self.descricao_input)

        self.add_button = Button(text='Adicionar Tarefa')
        self.add_button.bind(on_press=self.add_tarefa)
        self.layout.add_widget(self.add_button)

        self.tarefas_label = Label(text='Tarefas:', size_hint_y=None, height=40)
        self.layout.add_widget(self.tarefas_label)

        self.tarefas_display = BoxLayout(orientation='vertical', size_hint_y=None)
        self.layout.add_widget(self.tarefas_display)

        return self.layout

    def add_tarefa(self, instance):
        titulo = self.titulo_input.text
        descricao = self.descricao_input.text

        if titulo and descricao:
            tarefa = Tarefa(titulo, descricao)
            self.tarefas.append(tarefa)
            self.update_display()
            self.titulo_input.text = ''
            self.descricao_input.text = ''
        else:
            self.show_popup('Erro', 'Por favor, preencha todos os campos.')

    def update_display(self):
        self.tarefas_display.clear_widgets()
        for i, tarefa in enumerate(self.tarefas):
            layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            checkbox = CheckBox()
            checkbox.bind(active=self.concluir_tarefa)
            checkbox.tarefa = tarefa
            layout.add_widget(checkbox)
            label = Label(text=f'{tarefa.titulo}: {tarefa.descricao}')
            layout.add_widget(label)
            self.tarefas_display.add_widget(layout)

    def concluir_tarefa(self, instance, value):
        if value:
            instance.tarefa.concluida = True
        else:
            instance.tarefa.concluida = False
        self.update_display()

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 100))
        popup.open()

if __name__ == '__main__':
    GerenciadorDeTarefasApp().run()