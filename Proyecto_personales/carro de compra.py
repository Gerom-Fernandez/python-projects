# Simulación de CARRO DE COMPRA BASICO

print("Hola buenas, bienvenido a la tienda")
carrito = []  # Aquí se guardarán los productos elegidos (nombre, precio)

while True:
    print("\nAquí está nuestra lista de productos:")
    cosas = [
        "1. Tarjeta de video",
        "2. Procesador",
        "3. Placa Madre",
        "4. Memoria RAM",
        "5. Disco duro",
        "6. SSD (Unidad de estado sólido)",
        "7. Fuente de poder",
        "8. Cooler CPU",
        "9. Ventilador",
        "10. Gabinete",
        "0. Finalizar compra"
    ]
    for c in cosas:
        print(c)

    x = int(input("\nColoca un número del 0 al 10 para escoger algo que te interese: "))

    if x == 0:
        break  # salir del bucle para finalizar la compra

    # ---------------- TARJETA DE VIDEO ----------------
    elif x == 1:
        print("\nTarjeta de video")
        tarjeta = int(input("Elige la marca (1 para Nvidia, 2 para AMD): "))
        if tarjeta == 1:
            opciones = [
                ("MSI N210-MD1G/D3", 30790),
                ("MSI GT 710 2GD3 LP", 59990),
                ("Gigabyte GT 1030 Low Profile D4 2G", 79990),
                ("Gigabyte GT 730", 105990)
            ]
        else:
            opciones = [
                ("ASUS ROG-STRIX-RX560-4G-V2-GAMING", 95000),
                ("ASRock Radeon RX 6400 Challenger ITX 4GB", 164990),
                ("XFX Speedster QICK 210 AMD Radeon RX 6500 XT", 199990),
                ("Gigabyte Radeon RX 6600 EAGLE 8G", 299000)
            ]

        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- PROCESADOR ----------------
    elif x == 2:
        print("\nProcesador")
        CPU = int(input("Elige tu procesador (1 para Intel, 2 para AMD): "))
        if CPU == 1:
            opciones = [
                ("Intel Core i3-10100F", 85000),
                ("Intel Core i5-11400F", 160000),
                ("Intel Core i7-11700K", 320000)
            ]
        else:
            opciones = [
                ("AMD Ryzen 3 4100", 95000),
                ("AMD Ryzen 5 5600", 160000),
                ("AMD Ryzen 7 5800X", 280000)
            ]

        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- PLACA MADRE ----------------
    elif x == 3:
        print("\nPlaca Madre")
        placa = int(input("Elige la marca (1 para ASUS, 2 para Gigabyte): "))
        if placa == 1:
            opciones = [
                ("ASUS PRIME B450M-A", 85000),
                ("ASUS TUF Gaming B550-PLUS", 160000)
            ]
        else:
            opciones = [
                ("Gigabyte B450M DS3H", 80000),
                ("Gigabyte X570 AORUS Elite", 200000)
            ]

        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- RAM ----------------
    elif x == 4:
        opciones = [
            ("Kingston Fury Beast DDR4 8GB 3200MHz", 25000),
            ("Corsair Vengeance LPX DDR4 16GB 3200MHz", 55000),
            ("G.Skill Trident Z RGB DDR4 32GB 3600MHz", 120000)
        ]
        print("\nMemoria RAM disponibles:")
        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- DISCO DURO ----------------
    elif x == 5:
        opciones = [
            ("Seagate Barracuda 1TB 7200RPM", 35000),
            ("WD Blue 2TB 7200RPM", 55000),
            ("Seagate IronWolf NAS 4TB", 110000)
        ]
        print("\nDiscos duros disponibles:")
        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- SSD ----------------
    elif x == 6:
        opciones = [
            ("Kingston A400 240GB SATA", 20000),
            ("Crucial MX500 500GB SATA", 45000),
            ("Samsung 970 EVO Plus 1TB NVMe", 120000)
        ]
        print("\nSSD disponibles:")
        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- FUENTE DE PODER ----------------
    elif x == 7:
        opciones = [
            ("EVGA 500W 80+ White", 35000),
            ("Corsair CV650 650W 80+ Bronze", 55000),
            ("Seasonic Focus GX-750W 80+ Gold", 95000)
        ]
        print("\nFuentes de poder disponibles:")
        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- COOLER CPU ----------------
    elif x == 8:
        opciones = [
            ("Cooler Master Hyper 212 Black Edition", 35000),
            ("Noctua NH-U12S Redux", 55000),
            ("be quiet! Dark Rock Pro 4", 95000)
        ]
        print("\nCoolers CPU disponibles:")
        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- VENTILADOR ----------------
    elif x == 9:
        opciones = [
            ("Cooler Master SickleFlow 120mm", 10000),
            ("Noctua NF-P12 Redux 120mm", 15000),
            ("Corsair iCUE SP120 RGB", 20000)
        ]
        print("\nVentiladores disponibles:")
        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

    # ---------------- GABINETE ----------------
    elif x == 10:
        opciones = [
            ("NZXT H510", 70000),
            ("Cooler Master MasterBox Q300L", 45000),
            ("Corsair 4000D Airflow", 90000)
        ]
        print("\nGabinetes disponibles:")
        for i, (nombre, precio) in enumerate(opciones, start=1):
            print(f"{i}. {nombre}: ${precio}")

        eleccion = int(input("Elige el número del producto que quieres agregar al carrito: "))
        carrito.append(opciones[eleccion - 1])

# ---------------- FINALIZAR COMPRA ----------------
print("\n🛒 Resumen de tu compra:")
total = 0
for nombre, precio in carrito:
    print(f"- {nombre}: ${precio}")
    total += precio

print(f"\nTOTAL A PAGAR: ${total}")
print("¡Gracias por tu compra! 😊")
