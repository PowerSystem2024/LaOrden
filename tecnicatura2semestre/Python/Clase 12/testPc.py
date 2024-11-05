from orden import Orden
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton

teclado1 = Teclado("Keychron", "BT")
teclado2 = Teclado("Logitech", "BT")
raton1 = Raton("HP", "USB")
raton2 = Raton("Razer", "BT")
monitor1 = Monitor("LG", "27")
monitor2 = Monitor("Asus", "32")

computadora1 = Computadora("HP", monitor1, teclado1, raton1)
computadora2 = Computadora("MSI", monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]

orden1 = Orden(computadoras1)

print(orden1)
