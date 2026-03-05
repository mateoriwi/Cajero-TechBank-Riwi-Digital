
def bienvenido_al_atm():
    from rich.console import Console
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.align import Align

    console = Console()

    # Texto con colores ANSI
    titulo = "\033[93mBIENVENIDO\033[0m"      # Amarillo brillante
    subtitulo = "\033[92mAL ATM\033[0m"       # Verde brillante

    layout = Layout()

    layout.split_column(
        Layout(name="header", size=7),
        Layout(name="footer", size=3)
    )

    layout["header"].update(
        Panel(
            Align.center(f"{titulo}\n{subtitulo}"),
            border_style="yellow",
            style="bold"
        )
    )

    layout["footer"].update(
        Panel(
            Align.center("\033[92mSistema Bancario Seguro\033[0m"),
            border_style="green"
        )
    )

    console.print(layout)
    
def pregunta_si_es_usuario_nuevo_o_no():
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text

    
    console = Console()

    mensaje = Text("¿Es usuario nuevo?", style="bold orange1")

    
    console.print(
        Panel(
            mensaje,
            title="[bold white]Sistema de Verificación[/bold white]",
            border_style="orange1",
            expand=False,
            padding=(1, 2)
        )
    )
    
    
def spinner():
    import time
    from rich.console import Console
    from rich.spinner import Spinner
    from rich.live import Live

    console = Console()

    spinner = Spinner("dots", text="Cargando datos...", style="cyan")

    with Live(spinner, refresh_per_second=12):
        time.sleep(5)
        
        
def limpiar_pantalla():
     import os
     os.system("cls")  # Windows
     os.system("clear")  # Linux/Mac

def subtitulo_panel(texto):
    from rich.console import Console
    from rich.panel import Panel
    from rich.align import Align

    console = Console()

    console.print(
        Panel(
            Align.center(texto),
            border_style="cyan",
            style="bold white",
            padding=(1, 2)
        )
    )
    
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()


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


def mensaje_advertencia(texto):
    console.print(
        Panel(
            Align.center(texto),
            border_style="yellow",
            style="bold yellow",
            padding=(1, 2)
        )
    )