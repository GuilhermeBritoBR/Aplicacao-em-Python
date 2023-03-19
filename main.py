import PySimpleGUI as sg      

sg.theme("LightGray1")
print("Distância")
Distância=int(input("Qual foi a quilometragem?"))
Metros=(Distância)
print('Tempo')
Tempo=int(input("Qual foi o seu tempo?"))
Velocidade=(Tempo/Distância)
print("Essa foi a sua velocidade:")
print(Velocidade," Minutos por quilometro")

layout = [[sg.Text("Qual foi a quilometragem?")], [sg.InputText()]] 

layout = [[sg.Text("Qual foi seu tempo?")], [sg.InputText()], [sg.Submit(), sg.Cancel()]]

window = sg.Window("Recordes", layout)    

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Quit": break
    
    text_input = values[0]
    sg.popup("You entered", text_input)

window.close()