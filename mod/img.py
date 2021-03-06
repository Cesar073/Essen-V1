'''
HACER:
* Necesito ajustar las funciones de Thumbnail tanto para un archivo como para las listas, con la capacidad tanto de sobreescribir como de guardar en otra carpeta nueva
* Tmb tengo que poder redimiensionar imagenes sin el Thumbnail, ya que recuerdo que ése mantiene la relación de aspecto, mientras que redimensionar estira o estrecha una img.s

    IMPORTANTE:
    * Debe importar el módulo de Navegación. Realiza acciones sobre las rutas de los archivos y también las analiza, por ello es que necesitamos dicho módulo.

    RGB y RGBA:
    RGB es un formato de 3 canales para los colores Red, Green y Blue. 
    RGBA es un formato de 4 canales para los colores Red, Green, Blue y el 4to es el Alpha. Éste último se encarga de determinar una transparencia, que puede ser opaca por
    completo, transparente o alguna tonalidad intermedia de grises.
    Si se desea trabajar con imagenes tipo png, es necesario que se de aviso al sistema para que pueda trabajar con las transparencias como cuando queremos pegar una imagen con
    transparencias dentro de otra jpg.
    Para ello luego de abrir el archivo se realiza una "conversión" para que comprenda los 4 canales con la siguiente sintaxis:
        imagen = Image.open("imagen_original.png")
        nueva_imagen = imagen_original.convert("RGB")
    Si bien pareciera que se convierte el canal Alpha en un color fijo, en realidad al momento de pegar dicha imagen se respetan las transparencias.
'''

from PIL import Image
import mod.nave as nv

# Superpone las imagenes que se hayan enviado y la devuelve para seguir trabajando
    # La imagen queda en memoria, se devuelve el objeto, no se guarda en disco.
    # La función se encarga de reconocer el formato de la imagen y luego realiza la superposición correspondiente.

    # Devuelve 2 valores de return, uno que indica la acción y otro sería el objeto de imagen.
    # El parámetro de acción es una respuesta que puede contener los siguientes valores:
        # Devuelve 0 si la acción se ejecutó sin problemas.
        # Devuelve 1 si uno de los 2 archivos no es formato admitido (png - jpg)
        # Devuelve 2 si lo que se intenta es pegar un jpg dentro de una png. Es una acción que puede relaizarse de ser necearia, pero el archivo debería ser guardado en disco directamente, no podemos devolverlo en un "return". En caso de ser necesario se programará para que primero se pegue la imagen png en un lienzo nuevo del fondo que se desee, y luego sí pegar el jpg encima dando por finalizado un jpg.
        # Devuelve 3 si ocurrió algún error desconocido.
    
    # Hay que comprender que en todas las combinaciones de superposición donde una de las imagenes es formato jpg, se devuelve indeflectiblemente otra jpg.
def Superpone(Im_Fondo, Im_Delantera, ejeX, ejeY):
    Rta = 0
    Resultado = 0
    Form1 = 0
    Form2 = 0
    try:
        Form1 = nv.Dev_Extencion(Im_Fondo)
        Form2 = nv.Dev_Extencion(Im_Delantera)
        if Form1 == "png":
            if Form2 == "png":
                Resultado = Super_png_png( Im_Fondo, Im_Delantera, ejeX, ejeY)
            elif Form2 == "jpg":
                Rta = 2
            else:
                Rta = 1
        elif Form1 == "jpg":
            if Form2 == "png":
                Resultado = Super_png_jpg( Im_Fondo, Im_Delantera, ejeX, ejeY)
            elif Form2 == "jpg":
                Resultado = Super_jpg_jpg( Im_Fondo, Im_Delantera, ejeX, ejeY)
            else:
                Rta = 1
        else:
            Rta = 1
    except:
        Rta = 3
    return Rta, Resultado

def Thumbnail_Lista(Dimension, Lista):
    size = (Dimension,Dimension)
    for i in Lista:
        img = Image.open(i)
        img.thumbnail(size)
        img.save(i)


def Thumbnail_Imagen(Dimension, Lista):
    size = (Dimension,Dimension)
    for i in Lista:
        img = Image.open(i)
        img.thumbnail(size)
        img.save(i)

'''########################################################################################################################################
###########################################################################################################################################
                                FUNCIONES AUXILIARES (Internas utilizadas para ayuda de éste módulo)                                    '''

# Superpone una imagen de formato PNG dentro de una JPG - Devuelve una imagen JPG
    # Parámetros:
    # Path_Imagen_Ppal_jpg: Es la imagen principal en formato jpg.
    # Path_Imagen_superponer_png: Es la imagen secundaria que se va a pegar en la principal, debe tener formato png.
    # ejeX: Ubicación en pixeles del eje X donde se va a colocar la imagen teniendo en cuenta la esquina superior izquierda.
    # ejeY: Ubicación en pixeles del eje Y donde se va a colocar la imagen teniendo en cuenta la esquina superior izquierda.
def Super_png_jpg(Path_Imagen_Ppal_jpg, Path_Imagen_superponer_png, ejeX, ejeY):
    # Abrimos las imagenes
    Imagen1 = Image.open(Path_Imagen_Ppal_jpg)
    Imagen2 = Image.open(Path_Imagen_superponer_png)
    # Solucionamos un posible error con las imagenes del formato PNG (que es RGBA) con el formato RGB, más detalles en la cabecera
    Imagen2 = Imagen2.convert('RGBA')
    # Pegamos la imagen2 en la 1
    Imagen1.paste(Imagen2 ,(ejeX,ejeY), Imagen2)
    # Retornamos la imagen nueva    
    return Imagen1

# Superpone una imagen de formato JPG dentro de una JPG - Devuelve una imagen JPG
    # Parámetros:
    # Path_Imagen_Ppal_jpg: Es la imagen principal.
    # Path_Imagen_superponer_jpg: Es la imagen secundaria que se va a pegar en la principal.
    # ejeX: Ubicación en pixeles del eje X donde se va a colocar la imagen teniendo en cuenta la esquina superior izquierda.
    # ejeY: Ubicación en pixeles del eje Y donde se va a colocar la imagen teniendo en cuenta la esquina superior izquierda.
def Super_jpg_jpg(Path_Imagen_Ppal_jpg, Path_Imagen_superponer_jpg, ejeX, ejeY):
    # Abrimos las imagenes
    Imagen1 = Image.open(Path_Imagen_Ppal_jpg)
    Imagen2 = Image.open(Path_Imagen_superponer_jpg)
    # Pegamos la imagen2 en la 1
    Imagen1.paste(Imagen2,(ejeX,ejeY))
    # Retornamos la imagen nueva    
    return Imagen1

# Superpone una imagen de formato PNG dentro de una PNG - Devuelve otra imagen PNG
    # Parámetros:
    # Path_Imagen_Ppal_png: Es la imagen principal.
    # Path_Imagen_superponer_png: Es la imagen secundaria que se va a pegar en la principal.
    # ejeX: Ubicación en pixeles del eje X donde se va a colocar la imagen teniendo en cuenta la esquina superior izquierda.
    # ejeY: Ubicación en pixeles del eje Y donde se va a colocar la imagen teniendo en cuenta la esquina superior izquierda.
def Super_png_png(Path_Imagen_Ppal_png, Path_Imagen_superponer_png, ejeX, ejeY):
    # Abrimos las imagenes
    Imagen1 = Image.open(Path_Imagen_Ppal_png)
    Imagen2 = Image.open(Path_Imagen_superponer_png)
    # Pegamos la Imagen2 en la 1
    Imagen1.paste(Imagen2 ,(ejeX,ejeY), Imagen2)
    # Retornamos la imagen nueva    
    return Imagen1

# Guarda una imagen jpg en jpg
    # Debe venir una imagen en formato jpg
    # Nota: Se permite guardar de todas formas la imagen aunque venga sin nombre especificado por el parámetro "Nombre", pero para ello debe estar incluído en la "Ruta".
def Guarda_Imagen(Imagen, Ruta, Nombre = ""):
    if Nombre != "":
        Ruta = Ruta + "/" + Nombre
    Imagen.save(Ruta)

# Guardar una imagen png en jpg
    # IMPORTANTE: Quise que devuelva sólo la imagen en formato jpg pero no pude, genera error, así que el "guardado" tiene que estar acá incluído.
    # Debe venir la imagen en formato png
    # Una imagen que viene en png, la guarda en jpg, en la ruta especificada y con el nombre especificado
    # Nota: Se permite guardar de todas formas la imagen aunque venga sin nombre especificado por el parámetro "Nombre", pero para ello debe estar incluído en la "Ruta".
    # Los parámetros R,G y B, responden a la parte transparente de la imagen que viene, que obviamente debe rellenarse con algún color. Si el valor es de 255 (es el que dejamos
    # por defecto), se va a rellenar el color en blanco. Si el valor es 0, se rellena en negro. En caso que se desee otra gama de colores sólo necesitamos cargar esos datos en
    # los parámetros según los ganales por RGB.
def Convierte_Guarda_png_a_jpg(Imagen, Ruta, Nombre = "", R = 255, G = 255, B = 255):
    bg = Image.new("RGB", Imagen.size, (R,G,B))
    bg.paste(Imagen,Imagen)
    if Nombre != "":
        Ruta = Ruta + "/" + Nombre + ".jpg"
    bg.save(Ruta)
