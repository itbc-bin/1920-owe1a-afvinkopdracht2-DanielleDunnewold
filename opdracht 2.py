#variabel erinzetten
Sequentie = input("voer sequentie in zonder enters ")


#bepalen aantal G, C, T en A
AantalG= Sequentie.count("G")
AantalC = Sequentie.count("C")
AantalT = Sequentie.count("T")
AantalA = Sequentie.count("A")

#bepalen hoeveel nucleotiden de sequentie bestaat
nucleotideTotal = AantalG+AantalC+AantalA+AantalT


#berekening om GC uitte rekenen
GC = (AantalG+AantalC)/nucleotideTotal *100

#print uitslagen
print("aantal nucleotiden is "+ str(nucleotideTotal))
print("GC% is " + str(GC))
