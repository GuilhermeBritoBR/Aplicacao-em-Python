import PySimpleGUI as sg      

sg.theme("LightGray3")
#layout
layout = [
[sg.Text("Quilometros"), sg.Input(key="Quilometros",size=(4,1))],
[sg.Text("Horas"), sg.Input(key="Horas",size=(4,1))],
[sg.Text("Minutos"), sg.Input(key="Minutos",size=(4,1))],
[sg.Text("Segundos"), sg.Input(key="Segundos",size=(4,1))],
[sg.Button('Calcular')],
  [sg.Button('Salvar recorde!')]

]
#format
janela=sg.Window('  Recordes',layout)
#eventos
while True:
    eventos, valores=janela.Read()
if eventos== sg.WINDOW_CLOSED:
  ()
   




   
    
    
