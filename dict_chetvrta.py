#Da se kreira programa koja ke bide za potrebide vo nekoja prodavnica.
# Da se kreira dictionary koj ke ima 2 indexi, produkti, ceni koi kkao podatoci
# ke imaat prazni listi. Koristnikot da moze da vnesuva produkti i ceni na produktite
# se dodeka ne izbere deka poveke ne saka da vnese. Koga ke prestane da vnesuva produkti 
# da se presmeta kolku treba da plati i da se zacuva vo nov index. Da mu se dade opcija na korisnikot 
# da plati, d a se presmeta dali treba da se vrati kusur ili ne.
# Ako treba da se zacuva vo dictionary kolku kusur treba da se vrati.
# Ako ne treba da se zacuva deka smetkata e platena.

programa=dict()
produkti=[]
ceni=[]
while True:
 produkt=input("Vnesi ime na produkt: (izberi plati dokolku sakash da platish)\n")
 if produkt=="plati":
  break
 cena=int(input("Vnesi cena na produkt:\n"))
 programa["produktite"]=produkti.append(produkt)
 programa["cenite"]=ceni.append(cena)
programa["suma"]=sum(ceni)
gotovina=sum(ceni)
vkupno=len(produkti)
kesh=int(input("Vnesete kolku kesh imate"))
if kesh-gotovina>0:
 programa["kusur"]=kesh-gotovina
 print("Za vrakanje imate kusur od:{}\n".format(kesh-gotovina))
elif kesh-gotovina==0:
 print("Vi blagodarime")
else:
 print("Imate greshka")

 print(programa)
