c = int(input()) # quilometros por litro
d = int(input()) # distancia até o aeroporto
l = int(input()) # número de litros de combustível no tanque

quilometros = c*l # quantos quilômetros ele pode rodar

if quilometros > d :
    print(0)
else:
    print(f"{(d-quilometros)/c :.1f}")