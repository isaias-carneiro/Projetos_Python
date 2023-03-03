import PySimpleGUI as sg
# criar janela e estilo do layout
def janela_login():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('login', layout=layout, finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer pedido')],
        [sg.Checkbox('Queijo', key='q'), sg.Checkbox('frango', key='f')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar pedido', layout=layout, finalize=True)

janela1, janela2 = janela_login(), None
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        var = janela2 == janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        # noinspection PyUnresolvedReferences
        janela2.hide()
        janela1.un_hide()
