from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

def subtitulo_panel(texto):
    console.print(
        Panel(
            Align.center(texto),
            border_style="cyan",
            style="bold white",
            padding=(1, 2)
        )
    )

def mensaje_error(texto):
    console.print(
        Panel(
            Align.center(texto),
            border_style="red",
            style="bold red",
            padding=(1, 2)
        )
    )

def mensaje_exito(texto):
    console.print(
        Panel(
            Align.center(texto),
            border_style="green",
            style="bold green",
            padding=(1, 2)
        )
    )

def mensaje_info(texto):
    console.print(
        Panel(
            Align.center(texto),
            border_style="white",
            style="bold white",
            padding=(1, 2)
        )
    )

def color_pagina_principal(texto):
    console.print(
        Panel(
            Align.center(texto),
            border_style="white",
            style="bold white",
            padding=(1, 2)
        )
    )

def color_opcion(texto):
    console.print(
        Panel(
            Align.center(texto),
            border_style="yellow",
            style="bold white",
            padding=(1, 2)
        )
    )