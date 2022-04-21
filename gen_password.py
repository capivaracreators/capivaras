import random
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='chars_total', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        # Declara janela
        self.janela = sg.Window('Password Generator', layout)

        pass

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                new_password = self.gen_password(valores)
                print(new_password)

    def gen_password(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVXXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%'
        chars = random.choices(char_list, k=int(valores['chars_total']))
        new_pass = ''.join(chars)
        return new_pass

    def save_password(self, new_pass, valores):
        with open('senhas.txt', newline='') as arquivo:
            arquivo.write(
                f"site: {valores[site]}, usuário: {valores[usuario]}, nova senha: {new_pass}"
            )

        print('Arquivo salvo')


gen = PassGen()
gen.Iniciar()
