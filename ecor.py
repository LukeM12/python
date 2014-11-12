def pa ():
    i *= .01
    A = float(raw_input("\nEnter the A : \n"))
    i = float(raw_input("\nEnter the I: \n"))
    n = float(raw_input("\nEnter the N:  \n"))
    return (A*( (1+i)**n + 1 ) )/ ( i*(1+i)**n)
   
def PF (F, N, i):
    i *= .01
    return (F * (1.0 )/ ((1.0 + i)**N))


def PA (A, n, i):
    i *= .01
    return (A*( (1+i)**n + 1 ) )/ ( i*(1+i)**n)



