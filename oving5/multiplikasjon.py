print("a)")



def mul(tol):
    prod = 1
    count = 1
    change = prod =(1+(1/(count)**2) - prod)
    while change > tol:
        old_prod = prod
        prod *= (1 + 1/((count)**2))
        count += 1
        change = prod - old_prod
    return prod, count-1

print("Produktet ble %.2f etter %.d iterasjoner"%(mul(0.01)))
