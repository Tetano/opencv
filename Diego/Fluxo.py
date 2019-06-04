Fechados = [1,2,9, 3, 5, 6, 7, 8]
Fechados.sort()
Abertos = [1, 2, 9]
Abertos.sort()
Totais = []
FechadosU = []
auxiliar = 0;
def funcionar():
    while(len(Fechados)<=10):
        auxiliar = input("Digite Valores\n")
        Fechados.append(auxiliar)
    while(len(Abertos)<=10):
        auxiliar = input("Digite Valores\n")
        Abertos.append(auxiliar)
TotalId = len(Fechados) + len(Abertos)
#print(TotalId)
for x in range(0,len(Fechados)):
    if Fechados[x] not in Abertos:
        print(Fechados[x], " Não pertence")
        Totais.append(Fechados[x])
    else:
        print(Fechados[x], "Pertence")
        Totais.append(Fechados[x])
#######################################
print("---------------VALIDANDO OS ABERTOS-----------------")
for x in range(0,len(Abertos)):
    if Abertos[x] not in Fechados:
        print(Abertos[x], " Não pertence")
        Totais.append(Abertos[x])
    else:
        print(Abertos[x], "Pertence")

Totais.sort()
print("ID's De todos Chamados",Totais)


