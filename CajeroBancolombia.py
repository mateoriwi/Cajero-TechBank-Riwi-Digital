def menu_cajero():
    from colores import subtitulo_panel
    from colores import mensaje_error, mensaje_exito, mensaje_info

    saldo_inicial = 1000

    while True:

        print("Página principal:")
        print("Opción 1 → Consultar saldo")
        print("Opción 2 → Retirar saldo")
        print("Opción 3 → Depositar saldo")
        print("Opción 4 → Cerrar sesión")

        opcion = int(input("Seleccione una opción: 1, 2, 3 o 4\n"))

        if opcion == 1:
            subtitulo_panel(f"El monto actual es: {saldo_inicial}" )
            monto = float(input("→ "))

        elif opcion == 2:
            while True:
                subtitulo_panel("¿Cuánto dinero desea retirar?")
                monto = float(input("→ "))

                if monto > saldo_inicial:
                    mensaje_error("No puede retirar más de su saldo actual")
                    break

                elif monto <= 0:
                    mensaje_error("Monto inválido")
                    continue

                else:
                    saldo_inicial -= monto
                    mensaje_exito(f"Saldo restante: {saldo_inicial}")
                    break

        elif opcion == 3:
            while True:
                subtitulo_panel("¿Cuánto dinero desea depositar?")
                monto = float(input("→ "))

                if monto <= 0:
                    mensaje_error("Monto inválido")
                    continue
                else:
                    saldo_inicial += monto
                    mensaje_exito(f"Saldo restante: {saldo_inicial}")
                    break

        elif opcion == 4:
            mensaje_exito("Gracias por usar el cajero")
            break

        else:
            mensaje_error("Opción inválida")