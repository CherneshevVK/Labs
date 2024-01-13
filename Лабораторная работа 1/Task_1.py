list_enigma=[1,2,6,4,2,8,4,8,'l',4,6,21,4,68,7]
for i in range(len(list_enigma)):
    if not type(list_enigma[i])==int:
        b=i
list_enigma[b]=0
summa=sum(list_enigma)
dlina=len(list_enigma)
average=summa/dlina
list_enigma[b]=average
print(list_enigma)
