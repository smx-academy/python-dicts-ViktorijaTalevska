#Da se kreiara prazen dictionary, korisnikot da vnese 2 broevi koi ke se dodadt vo dictionary.
# Da se izvrsat 4te osnovni matematicki operacii i da se dodadat rezultatite 
#vo dictionary vo razlicni keys


broevi=dict()
operacii=dict()

broevi={
"prv_broj":int(input("Vnesete go prviot broj")),
"vtor_broj":int(input("Vnesete go vtoriot broj"))
}

operacii["zbir"]=broevi["prv_broj"] + broevi["vtor_broj"]
operacii["proizvod"]=broevi['prv_broj']* broevi['vtor_broj']
operacii["razlika"]=broevi["prv_broj"] -broevi["vtor_broj"]
operacii["kolichnik"]=broevi['prv_broj']/ broevi['vtor_broj']
print(operacii)