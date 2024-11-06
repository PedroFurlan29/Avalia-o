import kivy
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

class TuningMenu(BoxLayout):
    def __init__(self, **kwargs):  
        super(TuningMenu, self).__init__(**kwargs)  
        self.orientation = 'vertical'
        
        # Layout para entrada de informações do carro
        self.car_info_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
        
        self.brand_input = MDTextField(hint_text='Marca do Carro', font_size=24, size_hint_y=None, height=40)
        self.model_input = MDTextField(hint_text='Modelo do Carro', font_size=24, size_hint_y=None, height=40)
        self.engine_type_input = MDTextField(hint_text='Tipo de Motor', font_size=24, size_hint_y=None, height=40)

        self.car_info_layout.add_widget(self.brand_input)
        self.car_info_layout.add_widget(self.model_input)
        self.car_info_layout.add_widget(self.engine_type_input)
        
        self.add_widget(self.car_info_layout)

        # Botão para mostrar opções de tuning
        self.show_tuning_button = MDRaisedButton(text='Mostrar Opções de Tuning', font_size=25, size_hint_y=None, height=50)
        self.show_tuning_button.bind(on_press=self.show_tuning_options)
        self.add_widget(self.show_tuning_button)

        # Layout para os botões de tuning (Stage 1, 2, 3, 4)
        self.button_grid = GridLayout(cols=2, spacing=10, padding=10, size_hint_y=None, height=200)
        self.add_widget(self.button_grid)

        # Botões do stage (inicialmente invisíveis)
        self.stage1_button = MDRaisedButton(
            text='Stage 1', 
            font_size=25, 
            size_hint=(None, None), 
            size=(150, 50),
            pos_hint={'center_x': 0.5},  # Centraliza o botão
            md_bg_color=(1, 0, 0, 1),  # Cor vermelha
            elevation=10,  # Efeito de sombra
            opacity=0  # Inicialmente invisível
        )
        self.stage1_button.bind(on_press=self.stage1_selected)
        self.button_grid.add_widget(self.stage1_button)

        self.stage2_button = MDRaisedButton(
            text='Stage 2', 
            font_size=25, 
            size_hint=(None, None), 
            size=(150, 50),
            pos_hint={'center_x': 0.5},  # Centraliza o botão
            md_bg_color=(1, 0, 0, 1),  # Cor vermelha
            elevation=10,
            opacity=0  # Inicialmente invisível
        )
        self.stage2_button.bind(on_press=self.stage2_selected)
        self.button_grid.add_widget(self.stage2_button)

        self.stage3_button = MDRaisedButton(
            text='Stage 3', 
            font_size=25, 
            size_hint=(None, None), 
            size=(150, 50),
            pos_hint={'center_x': 0.5},  # Centraliza o botão
            md_bg_color=(1, 0, 0, 1),  # Cor vermelha
            elevation=10,
            opacity=0  # Inicialmente invisível
        )
        self.stage3_button.bind(on_press=self.stage3_selected)
        self.button_grid.add_widget(self.stage3_button)

        self.stage4_button = MDRaisedButton(
            text='Stage 4', 
            font_size=25, 
            size_hint=(None, None), 
            size=(150, 50),
            pos_hint={'center_x': 0.5},  # Centraliza o botão
            md_bg_color=(1, 0, 0, 1),  # Cor vermelha
            elevation=10,
            opacity=0  # Inicialmente invisível
        )
        self.stage4_button.bind(on_press=self.stage4_selected)
        self.button_grid.add_widget(self.stage4_button)

        # Labels para exibir as informações de tuning
        self.peças_label = MDLabel(text='', font_size=20)
        self.add_widget(self.peças_label)
     
        self.power_label = MDLabel(text='', font_size=20)
        self.add_widget(self.power_label)

        self.valor_label = MDLabel(text='', font_size=20)
        self.add_widget(self.valor_label)

    def show_tuning_options(self, instance):
        # Oculta as informações do carro e o botão de mostrar opções
        self.car_info_layout.opacity = 0
        self.show_tuning_button.opacity = 0

        # Exibe as informações do carro nas labels
        brand = self.brand_input.text
        model = self.model_input.text
        engine_type = self.engine_type_input.text

        self.peças_label.text = f'Veículo: {brand} {model} - Tipo de Motor: {engine_type}'
        self.power_label.text = ''
        self.valor_label.text = ''

        # Torna os botões de Stage visíveis
        self.stage1_button.opacity = 1
        self.stage2_button.opacity = 1
        self.stage3_button.opacity = 1
        self.stage4_button.opacity = 1

    def stage1_selected(self, instance):
        self.peças_label.text = f'Veículo: {self.brand_input.text} {self.model_input.text} - Tipo de Motor: {self.engine_type_input.text}\nInstalações:  Remapeamento da ECU (Unidade de Controle Eletrônico)'
        self.valor_label.text = 'Valor para a instalação:  R$ 2.000 a R$ 5.000'
        self.power_label.text = 'Potência adicionada:  30 CV + 17 Nm (torque)' 
        print('Stage 1')

    def stage2_selected(self, instance):
        self.peças_label.text = f'Veículo: {self.brand_input.text} {self.model_input.text} - Tipo de Motor: {self.engine_type_input.text}\nInstalações:  Filtro de ar esportivo + Escape esportivo \n + Sistema de injeção de combustível aprimorado'
        self.valor_label.text = 'Valor para a instalação:  R$ 5.000 a R$ 15.000'
        self.power_label.text = 'Potência adicionada:  50 CV + 30 Nm (torque)'
        print('Stage 2')

    def stage3_selected(self, instance):
        self.peças_label.text = f'Veículo: {self.brand_input.text} {self.model_input.text} - Tipo de Motor: {self.engine_type_input.text}\nInstalações:  Intercooler de alto desempenho + Filtro de ar esportivo \n+ Escape esportivo + Turbo esportivo'
        self.valor_label.text = 'Valor para a instalação:  R$ 15.000 a R$ 40.000'
        self.power_label.text = 'Potência adicionada:  100 CV + 52 Nm (torque)'
        print('Stage 3')

    def stage4_selected(self, instance):
        self.peças_label.text = f'Veículo: {self.brand_input.text} {self.model_input.text} - Tipo de Motor: {self.engine_type_input.text}\nInstalações:  Aplicações do Stage 3 + Transmissão reforçada + \nEixo de Comando, Válvulas e Pistões esportivos'
        self.valor_label.text = 'Valor para a instalação:  Acima de R$ 40.000'
        self.power_label.text = 'Potência adicionada:  180 CV + 75 Nm (torque)'
        print('Stage 4')

class MeuApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"  # Cor primária para o tema
        self.theme_cls.theme_style = "Dark"  # Tema escuro
        return TuningMenu()

if __name__ == "__main__":
    MeuApp().run()
