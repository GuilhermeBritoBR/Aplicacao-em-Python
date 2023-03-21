import PySimpleGUI as sg      

sg.theme("LightGray1")
print("Distância")
Distância=int(input("Qual foi a quilometragem?"))
print('Tempo')
Horas=int(input("Quantas horas foi?"))
Minutos=int(input('Quantos minutos?'))
Segundos=int(input('Quantos segundos?'))
Tempo=((Horas*3600)+(Minutos*60)+Segundos)
Velocidade=(Tempo/Distância)
Min,Seg=divmod(Velocidade,60)
mm=round(Min)
ss=round(Seg)
print("Esse foi o seu pace:")
print(mm, ss, sep=":")

layout = [[sg.Text("Qual foi a quilometragem?")], [sg.InputText()]] 

layout = [[sg.Text("Qual foi seu tempo?")], [sg.InputText()], [sg.Submit(), sg.Cancel()]]

window = sg.Window("Recordes", layout)    

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Quit": break
    
    text_input = values[0]
    sg.popup("You entered", text_input)

window.close()