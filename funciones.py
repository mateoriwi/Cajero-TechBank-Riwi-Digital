


def menu():
    saldo = 1000
    menu1 = int(input(
    "\n¿Qué desea hacer?\n"
    "1. Realizar alguna operación\n"
    "2. Consultar saldo\n"
    "3. Cambiar contraseña\n"
    "Seleccione una opción (1-3): "
))

    if menu1 == 1:
        numero_de_operacion = int(input("Ingrese cuantas veces quiere que se repira el proceso: "))
        for i in range(numero_de_operacion):
            print("¿Qué operación desea realizar?")
            print("1. retirar dinero")
            print("2. depositar dinero")
            menu2 = int(input("Seleccione una opción (1-2): "))
            if menu2 == 1:
                monto_retiro = float(input("Ingrese el monto a retirar: "))
                if monto_retiro <= saldo:
                    saldo -= monto_retiro
                    print(f"Retiro exitoso. Su nuevo saldo es: {saldo}")
                else:
                    while monto_retiro > saldo:
                        print("Saldo insuficiente para realizar el retiro.")
                        monto_retiro = float(input("Ingrese un monto a retirar menor o igual a su saldo: "))
                    saldo -= monto_retiro
                    print(f"Retiro exitoso. Su nuevo saldo es: {saldo}")
            elif menu2 == 2:
                monto_deposito = float(input("Ingrese el monto a depositar: "))
                saldo += monto_deposito
                print(f"Depósito exitoso. Su nuevo saldo es: {saldo}")

        numero_de_operacion -= 1
        
    elif menu1 == 2:
        print(f"Su saldo actual es: {saldo}")
    elif menu1 == 3:
        contraseña_actual = str(input("Ingrese su contraseña actual: "))
        nueva_contraseña = str(input("Ingrese su nueva contraseña: "))               
        confirmación_contraseña = str(input("Confirme su nueva contraseña: "))
        while True:
            if nueva_contraseña != confirmación_contraseña:
                print("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")
            elif len(nueva_contraseña) < 4:
                print("La contraseña debe tener al menos 4 caracteres. Por favor, inténtelo de nuevo.")
            else:
                print("Contraseña cambiada exitosamente.")
            break



def usuario_nuevo():
    import csv
    import os

    # Nombre del archivo CSV
    archivo_csv = "usuarios.csv"

    # Pedir datos al usuario
    nombre = input("Ingrese su primer nombre: ")
    apellido = input("Ingrese su primer apellido: ")
    cedula = input("Ingrese su número de cédula: ")
    while True:
            pin = input("Ingrese un PIN de 4 dígitos: ")

            if len(pin) != 4:
                print("El PIN debe tener exactamente 4 dígitos. Por favor, inténtelo de nuevo.")
            elif not pin.isdigit():
                print("El PIN debe contener solo dígitos. Por favor, inténtelo de nuevo.")
            else:
                print(f"Gracias {nombre} {apellido}, su cuenta ha sido registrada exitosamente.")
                break


    # Verificar si el archivo ya existe
    archivo_existe = os.path.isfile(archivo_csv)

    # Abrir el archivo en modo 'a' (agregar)
    with open(archivo_csv, "a", newline="", encoding="utf-8") as archivo:
            campos = ["Nombre", "Apellido", "Cédula", "PIN"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # Si el archivo no existía, escribir encabezado
            if not archivo_existe:
                escritor.writeheader()
            
            # Escribir los datos del usuario
            escritor.writerow({"Nombre": nombre, "Apellido": apellido, "Cédula": cedula, "PIN": pin })


    

def espera():
    import time
    time.sleep(2)  # Espera 3 segundos
    


def guardar_usuario():
    import csv
    import os

    # Nombre del archivo CSV
    archivo_csv = "usuarios.csv"

    # Pedir datos al usuario
    nombre = input("Ingrese su primer nombre: ")
    apellido = input("Ingrese su primer apellido: ")
    cedula = input("Ingrese su número de cédula: ")

    # Verificar si el archivo ya existe
    archivo_existe = os.path.isfile(archivo_csv)

    # Abrir el archivo en modo 'a' (agregar)
    with open(archivo_csv, "a", newline="", encoding="utf-8") as archivo:
        campos = ["Nombre", "Apellido", "Cédula"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        
        # Si el archivo no existía, escribir encabezado
        if not archivo_existe:
            escritor.writeheader()
        
        # Escribir los datos del usuario
        escritor.writerow({"Nombre": nombre, "Apellido": apellido, "Cédula": cedula})

    print("Datos guardados correctamente en usuarios.csv")