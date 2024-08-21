Primerlista=["Sapo",2,2]
print(Primerlista[0])
Primerlista[0]="ReSapo"
print(Primerlista)
Primerlista.append("iwachu")
print(Primerlista)
Primerlista.extend("Ome")  #Para combinar listas 
print(Primerlista)
Primerlista.append(2/2)
print(Primerlista)
Primerlista.append([[1,2,3],["Rayo"]])
print(Primerlista)
Sapo=Primerlista.pop()
print(Sapo)
del Sapo[1]
print(Sapo)
Primerlista.remove("iwachu")
print(Primerlista)
Nosapo= Primerlista[1:7]
print(Nosapo)
del Primerlista[1:7]  #Una funcion muy util
print(Primerlista)

###############################################################

mitupla= 1,2,3,1,23
a,*b,c,s= mitupla   
print(a,b,c,s) 
print(120 in mitupla)
mitupla + (1,2,3,2,1,321,32,132,132,21,) 

################################################################

midic={"Juego":"lol","Deporte":"Sedentarismo","Money":0,"Deporte":"Sedentarismo"}
print(midic)
midic["Edad"]=21
print(midic)

for yo in midic:
    print(yo)
    
for yo in midic.values():
    print(yo)

for yo,hago in midic.items():
    print("{yo}" + "{hago}")