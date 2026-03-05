from funciones import usuario_nuevo
from colores import bienvenido_al_atm
from colores import pregunta_si_es_usuario_nuevo_o_no
from colores import spinner
from colores import limpiar_pantalla
from funciones import espera
from CajeroBancolombia import menu_cajero

saldo_inicial = 1000 

bienvenido_al_atm()
espera()
limpiar_pantalla()
spinner()
pregunta_si_es_usuario_nuevo_o_no()
respuesta = input("Si o No: ").strip().lower()

if respuesta == "no":
    print("ingrese su numero de cedula e inserte su numero tarjeta")
    numero_cuenta = input()
    print("ingrese su contraseña")
    contraseña = input()
    print("bienvenido de nuevo")
    menu_cajero()
elif respuesta == "si":
    print(usuario_nuevo())
    print("bienvenido a su atm de confianza")
    menu_cajero()
else:
    print("Entrada inválida")    


