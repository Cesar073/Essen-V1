'''
Variables globales para todo el sistema
'''

# VTNA BUSCAR
# Indica a la ventana Buscar, desde dónde fue llamada, ya que su código de devolución varía según su origen
# 0: En reposo. Cuando no hay que dar ningún tipo de información.
# 1: Indica que se vuelve desde la ventana Buscar. Si una ventana cualquier se abre y la variable vale 1, es porque se viene luego de haber buscado algo.
# 2: Estamos en la ventana "Buscar" y viene desde "Promos"
# 3: Estamos en la ventana "Buscar" y viene desde "Productos"
# 4: Estamos en la ventana "Buscar" y viene desde "Cliente Nuevo" (Es para agregarle un "Deseo al cliente")
ORIGEN_BUSCAR = 0

# VTNA PRODUCTOS
# Indica si se está ejecutando o no el proceso de cargar archivos de Excel
EXCEL = False
# Es un contador para las listas
CONTADOR_ = 0
Lineas = []
Codigos = []
Descripcion = []
Pspv = []
Precio = []
Puntos = []
PuntosMG = []
Filas = []
# Indica el path para ubicar la base de datos que contiene los productos y algunas configuraciones
BaseDeDatos = "./db\\prod.db"

# Estas variables no se deben actualizar sobre el programa, de ser necesario, se debe reiniciar el programa.
# No se porque puse eso arriba, pero ya lo analizaré. Por el momento se quitó la posibilidad de que una de esas 3 clasificaciones se puedan desactivar, van a estar siempre
    # fijas y aún así, se dejó la base de datos intacta para dejar esa columna por si se usa en un futuro.
LINEA = []
TIPO = []
INTERIOR = []
LINEANUM = []
LINEAORDENADA = []

# Lista que carga un elemento buscado, o una serie de ellos dependiendo de quién lo necesite
LISTABUSCADO = []

# Listas de Configuración
LISTA_TIPOS_IMAGENES = []

# Base de datos de Clientes
DB_CLIENTES = "./db\\clie.db"