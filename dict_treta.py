#Da se kreira programa vo koja korisnikot ke moze da vnese strani na pravoagolnik, 
# da se vnesat vo dictionary, da se presmeta plostina i perimetar koja ke bide zacuvana vo dictinary. 
# Da se proveri dali plostinata ili perimetarot se pogolemi.

pravoagolnik=dict()
pravoagolnik["strana1"]=int(input("Vnesi ja prvata strana na pravoagolnikot"))
pravoagolnik["strana2"]=int(input("Vnesi ja vtorata strana na pravoagolnikot"))
pravoagolnik["ploshtina"]=pravoagolnik["strana1"]*pravoagolnik["strana2"]
pravoagolnik["perimetar"]=2*pravoagolnik["strana1"]+2*pravoagolnik["strana2"]
print(pravoagolnik)
if pravoagolnik["ploshtina"]>pravoagolnik["perimetar"]:
 print("Ploshtinata e pogolema")
else:
    print("Perimetarot e pogolem")
