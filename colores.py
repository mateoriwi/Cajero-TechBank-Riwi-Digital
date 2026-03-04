
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

    # Inicializamos la consola de Rich
    console = Console()

    # Definimos el mensaje con formato ANSI (naranja) y estilo Rich
    # El código [rgb(255,165,0)] o [orange1] funciona de maravilla
    mensaje = Text("¿Es usuario nuevo?", style="bold orange1")

    # Creamos y mostramos el panel
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

 