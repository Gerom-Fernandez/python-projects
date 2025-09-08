# CARRO DE COMPRA BASICO

print("Hola buenas que te iteresa comprar")
print("aqui esta nuestra lista de cosas que tenemos")

cosas = ["Tarjeta de video 1, Procesador 2, Placa Madre 3, Ram 4, Disco duro 5, Ssd Unidad de esta solido 6, Fuente de poder 7, Cooler CPU 8, Vetilador 9, Gabinete 10."]
print(cosas)

x = int(input("coloca un numero del 1 al 10 para escojer algo que te interese: "))


if x == 1:
    print("Tarjeta de video")
    tarjeta = int(input("elige la marca que te interese 1 para Nvidia y 2 para Amd: "))
    if tarjeta == "Nvidia":
        print("aqui estan las tarjetsa de Nvidia que tenemos")
        print("MSI N210-MD1G/D3: 30.790")
        print("MSI GT 710 2GD3 LP: 59.990")
        print("Gigabyte GT 1030 Low Profile D4 2G: 79.990")
        print("Gigabyte GT 730: 105.990")
    else:
        print("aqui estan las tarjetsa de AMD que tenemos")
        print("ASUS ROG-STRIX-RX560-4G-V2-GAMING: 95.000")
        print("ASRock Radeon RX 6400 Challenger ITX 4GB: 164.990")
        print("XFX Speedster QICK 210 AMD Radeon RX 6500 XT: 199.990")
        print("Gigabyte Radeon RX 6600 EAGLE 8G: 299.000")
elif x == 2:
    print("Procesador")
    CPU = int(input("elige tu procesador 1 para intel y 2 para AMD"))
    if CPU == 1:
        print("aqui esta los procesadores de Intel que tenemos")
        print("nnn")
    else:
        print("nnn")
elif x == 3:
    print("Placa Madre")
elif x == 4:
    print("Ram")
elif x == 5:
    print("Disco duro")
elif x == 6:
    print("Ssd Unidad de esta solido")
elif x == 7:
    print("Fuente de poder")
elif x == 8:
    print("Cooler CPU")
elif x == 9:
    print("Vetilador")
else:
    print("Gabinete")

    