import PySimpleGUI as sg    
from json import dumps 

sg.theme("LightGray1")
# print("Distância")
# Distância=int(input("Qual foi a quilometragem?"))
# Metros=(Distância)
# print('Tempo')
# Tempo=int(input("Qual foi o seu tempo?"))
# Velocidade=(Tempo/Distância)
# print("Essa foi a sua velocidade:")
# print(Velocidade," Minutos por quilometro")

layout = [[sg.Text("Qual foi a distância percorrida?")], [sg.InputText(key='km'), sg.Combo(['km','m'], 'km', key='un_dist')],
          [sg.Text("Qual foi seu tempo?")], [sg.InputText(key='tempo'), sg.Combo(['hora(s)','minuto(s)'], 'minuto(s)', key='un_tempo')], 
          [sg.Submit(), sg.Cancel()]]

window = sg.Window("Recordes", layout)    

while True:
    event, values = window.read()

    # if event == sg.WIN_CLOSED or event == "Quit": break
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    # text_input = values[0]
    # sg.popup("You entered", text_input, event, values)
    try:
        km = float(values['km'].replace(',','.'))
        tempo = float(values['tempo'].replace(',','.'))
        calculo = km / tempo
        sg.popup(f"Resultado: {calculo}\n{values['un_dist']} por {values['un_tempo']}",tempo,km)
    except Exception as e:
        sg.popup(f"ERRO: {e}",dumps(values,indent=4))

window.close()