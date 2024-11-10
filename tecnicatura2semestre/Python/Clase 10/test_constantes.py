from Constantes import *
# Aca es donde podemos cambiarle de nombre a lo importado, para que su uso sea mas facil
from Constantes import Matematicas as Mate

print(MI_CONSTANTE)

# Esto no se deberia hacer
MI_CONSTANTE = "Aqui esta el nuevo valor de la constante"
print(MI_CONSTANTE)

print(Matematicas)
print(Mate)
