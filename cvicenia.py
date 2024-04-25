#vypise hviezdicky tri rady do dvoch stlpcoch
rows = 3
columns = 2
while rows < 6:
    print ("**", end ="\n")
    rows += 1

 #vypise vysledok syntaxu ((5 + 2) - 3))
def addition (a,b,c):
    result = ((a + b) - c)
    return result

solusion = addition (a =5,b=2,c=3)
final = solusion 
print(final)

# pomocou datoveho typu tuple, syntax prikladu 4 + 1 a 4 - 1  
def pack_tuple (cislo1, cislo2):
    x = cislo1 + cislo2
    y = cislo1 - cislo2
    return x, y
z = pack_tuple(4,1)
print(z)

