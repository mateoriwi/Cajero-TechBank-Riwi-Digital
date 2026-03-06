def menu_cajero():
    from colores import subtitulo_panel
    from colores import mensaje_error, mensaje_exito, mensaje_info
    from colores import color_pagina_principal
    from colores import color_opcion

    saldo_inicial = 1000

    while True:

        color_pagina_principal("Página principal:")
        subtitulo_panel("Opción 1 → Consultar saldo")
        subtitulo_panel("Opción 2 → Retirar saldo")
        subtitulo_panel("Opción 3 → Depositar saldo")
        subtitulo_panel("Opción 4 → Cerrar sesión")

        try:
            color_opcion("Seleccione una opción: 1, 2, 3 o 4")
            opcion = int(input("→ "))

        except ValueError:
            mensaje_error("Debe ingresar un número válido, intente nuevamente")
            continue 

        if opcion == 1:
            mensaje_exito(f"El monto actual es: {saldo_inicial}")

        elif opcion == 2:
            while True:
                subtitulo_panel("¿Cuánto dinero desea retirar?")

                try:
                    monto = float(input("→ "))
                except ValueError:
                    mensaje_error("Debe ingresar un número válido, intente nuevamente")
                    continue

                if monto > saldo_inicial:
                    mensaje_error("No puede retirar más de su saldo actual, intente nuevamente")
                    continue

                elif monto <= 0:
                    mensaje_error("Monto inválido, intente nuevamente")
                    continue

                else:
                    saldo_inicial -= monto
                    mensaje_exito(f"Saldo restante: {saldo_inicial}")
                    break

        elif opcion == 3:
            while True:
                subtitulo_panel("¿Cuánto dinero desea depositar?")

                try:
                    monto = float(input("→ "))
                except ValueError:
                    mensaje_error("Debe ingresar un número válido, intente nuevamente")
                    continue

                if monto <= 0:
                    mensaje_error("Monto inválido, intente nuevamente")
                    continue
                else:
                    saldo_inicial += monto
                    mensaje_exito(f"Saldo restante: {saldo_inicial}")
                    break

        elif opcion == 4:
            mensaje_exito("Gracias por usar el cajero Tech Bank Riwi")
            break

        else:
            mensaje_error("Opción inválida")
