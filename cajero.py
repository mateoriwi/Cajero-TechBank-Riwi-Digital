from funciones import menu
from funciones import usuario_nuevo
from colores import bienvenido_al_atm
from colores import pregunta_si_es_usuario_nuevo_o_no
from colores import spinner
from colores import limpiar_pantalla
from funciones import espera

bienvenido_al_atm()
espera()
limpiar_pantalla()
spinner()
pregunta_si_es_usuario_nuevo_o_no()
respuesta = input("Si o No: ")

if respuesta == "No":
    print("ingrese su numero de cedula e inserte su numero tarjeta")
    numero_cuenta = input()
    print("ingrese su contraseña")
    contraseña = input()
    print("bienvenido de nuevo")
    print(menu())


if respuesta == "Si":
    print(usuario_nuevo())
    print("bienvenido a su atm de confianza")
    print(menu())


