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

