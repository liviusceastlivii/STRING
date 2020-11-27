n1=str(input("Dati cuvintul:"))
n2=str(input("Dati cuvintul:"))
n3=str(input("Dati cuvintul:"))
n4=str(input("Dati cuvintul:"))
cuvint=""
if (len(n1)>2 and len(n2)>2 and len(n3)>2 and len(n4)>2):
    cuvint+=n1[0:2]+n2[0]+n3[0:3]+n4[0:len(n4)//2]
else:
    print("Dati un cuvant, ce are mai mult de 2 caractere")
print(cuvint)