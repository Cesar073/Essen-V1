'''
Cargar todos los datos que se puedan. Por ej, formas de pago sirve porque si es un cliente que paga en efectivo algunos productos generan ganancia directa, si tiene tarjeta
naranja tiene unas promos, si es del hipotecario otras, y así sucesivamente. Intentar implementar las formas de pago con números y una tabla, por ejemplo, 1: efectivo - 2:Visa
3: Visa-Hipotecario, etc... Así puedo tener cientos de formas de pago y en la base de datos del cliente sólo agendo un integer
'''

from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QInputDialog
from PySide2.QtCore import QDir
from vtn.vtn_clie import Ui_Cliente_BD
from vtn.cla_clie_nue import V_ClienteNuevo

import mod.excel as ex
import mod.mdb as mdb
import mod.form as form
import mod.vars as mi_vars

class V_Clientes(QMainWindow):
    def __init__(self, ventanaAnterior):
        super(V_Clientes, self).__init__()
        self.ui = Ui_Cliente_BD()
        self.ui.setupUi(self)
        self.Ant = ventanaAnterior

        self.CLIENTE_BUSCADO = 0

        self.ui.push_Ficha.setEnabled(False)

        # BOTONES
        self.ui.push_Buscar.clicked.connect(self.Buscar_Clientes)
        # push_Nuevo es manejado desde App.py
        # push_Ficha es manejado desde App.py
        self.ui.push_Importar_Contactos.clicked.connect(self.Importar_Contactos)
        self.ui.push_Limpiar.clicked.connect(self.Limpiar)
    
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.Ant.show()

    def Contador_Frecuencia(self, valor, lista):
        cont = 0
        for i in lista:
            if valor == i:
                cont += 1
        return cont

    # Proceso que abarca desde la carga del archivo csv hasta agendar a los clientes
    def Importar_Contactos(self):

        # Informamos lo que vamos a hacer
        Rta = QMessageBox.question(self, "Actualizar Contactos", "A continuación se actualizarán y/o se sincronizarán los contactos con la base de datos de clientes. \n IMPORTANTE: Recuerde que el archivo contacts.csv no debe estar abierto.", QMessageBox.Ok | QMessageBox.Cancel)
        
        # Si desea continuar con la carga, procedemos a pedirle el path del archivo csv
        if Rta == QMessageBox.Ok:
            Ruta, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo de contactos con extensión: .csv', QDir.homePath(), "All Files (*.csv)")

            # Si el archivo existe y está todo en orden, continuamos
            if Ruta != "":

                # Variables para el informe final
                Actualizados = 0
                Controlados = 0
                Agregados = 0

                # Convertimos el archivo csv a un archivo de excel
                ex.Convierte_csv_xlsx_Pandas(Ruta, "./Contactos_Excel.xlsx")

                # Extraemos los datos del excel en diferentes listas
                L_Agendado, L_Apellido, L_Nombre1, L_Nombre2, L_Nombre3, L_Celular, L_Direccion, L_Corporativo = ex.Dev_Listas_Contactos("./Contactos_Excel.xlsx", "Sheet1")

                Controlados = len(L_Agendado)

                # A continuación vamos a tratar los contactos DUPLICADOS y luego los REPETIDOS.
                    # Se considera contacto duplicado aquellos donde se repite el número de celular, y debido a que no pueden haber 2 celulares iguales le pedimos eliminar uno.
                    # Se considera contacto repetido aquel que fue agendado más de una vez con el mismo nombre pero distinos celulares. En éste caso puede ser un error humano
                    # y le permitimos conservarlos modificando el nombre de uno de ellos, o eliminar directamente alguno. De todas formas, si bien pueden haber distintos
                    # contactos con el mismo nombre y distinto celular, para el sistema de búsqueda en wsp web es un problema, por ende vamos a evitarlo al igual que en el caso
                    # de los contactos duplicados.

                # DUPLICADOS
                L_Duplicados = []
                # Bucle que llena la lista de duplicados con los celulares que aparecen más de una vez
                for n in range(len(L_Agendado)):
                    if self.Contador_Frecuencia(L_Celular[n], L_Celular) > 1:
                        if self.Contador_Frecuencia(L_Celular[n], L_Duplicados) == 0:
                            L_Duplicados.append(L_Celular[n])
                # True: Si hay celulares repetidos, entonces le explicamos al usuario que se van a tratar y que se le va a pedir su eliminación
                if len(L_Duplicados) > 0:
                    QMessageBox.question(self, "Contactos Duplicados", "Se han detectado {} contactos duplicados.\nSe consideran contactos duplicados a aquellos que tienen el mismo número de celular sin importar si coinciden o no la forma en que fueron agendados.\nSe le va a pedir que conserve únicamente un contacto por cada celular duplicado.".format(len(L_Duplicados)), QMessageBox.Ok)
                    # Recorremos la lista en busca de todos los contactos que tienen el mismo celular, y se le mostrarán al usuario ennumerados. Luego él deberá elegir cuál de
                    # todos los contactos conservará.
                    for i in L_Duplicados:
                        # Lista para guardar el nombre de los duplicados
                        L_Dup_Nom = []
                        # Texto que se arma para mostrar en mensajes al usuario
                        texto_ = ""
                        cont = 0
                        # Coloco el siguiente bucle en un try, porque si hay contactos duplicados entonces generará un error. Esto se debe a que durante su proceso se van 
                        # eliminando elementos de la lista, entonces se inicia con un Tope pero si se eliminaron elementos llegará al final de la lista y buscará elementos
                        # que no están más.
                        try:
                            for n in range(len(L_Celular)):
                                if i == L_Celular[n]:
                                    cont += 1
                                    texto_ += "\n" + str(cont) + "). {}".format(L_Agendado[n])
                                    # Guardamos los índices de los duplicados
                                    L_Dup_Nom.append(n)
                        except:
                            pass
                        eleccion = False
                        while eleccion == False:
                            valor, ok = QInputDialog.getInt(self, "Contacto duplicado", "El celular {} se encuentra duplicado {} veces.\nSe muestran enlistados los nombres de dichos contactos, de los cuáles deberá elegir alguno de ellos colocando un número utilizando su índice mostrado en la lista.\nEl resto de contactos serán eliminados y deberá realizar la misma acción manualmente en su celular.{}".format(i, str(cont), texto_))
                            if ok == True and valor > 0 and valor <= len(L_Dup_Nom):
                                eleccion = True
                                borrado = 0
                                for j in range(len(L_Dup_Nom)):
                                    if valor == j + 1:
                                        pass
                                    else:
                                        # Ahora, quitamos de las listas de todos los datos de contactos, al valor duplicado. Adicionalmente los imprimimos por consola para 
                                            # controlar que estemos realizandolo bien
                                        print(L_Agendado.pop(L_Dup_Nom[j - borrado]))
                                        print(L_Apellido.pop(L_Dup_Nom[j - borrado]))
                                        print(L_Nombre1.pop(L_Dup_Nom[j - borrado]))
                                        print(L_Nombre2.pop(L_Dup_Nom[j - borrado]))
                                        print(L_Nombre3.pop(L_Dup_Nom[j - borrado]))
                                        print(L_Celular.pop(L_Dup_Nom[j - borrado]))
                                        print(L_Direccion.pop(L_Dup_Nom[j - borrado]))
                                        print(L_Corporativo.pop(L_Dup_Nom[j - borrado]))
                                        borrado += 1
                            else:
                                if ok == False:
                                    eleccion = True




                # REPETIDOS
                L_Repetidos = []
                # Bucle que llena la lista de repetidos con los contactos que aparecen más de una vez
                for n in range(len(L_Agendado)):
                    if self.Contador_Frecuencia(L_Agendado[n], L_Agendado) > 1:
                        if self.Contador_Frecuencia(L_Agendado[n], L_Repetidos) == 0:
                            L_Repetidos.append(L_Agendado[n])
                # True: Si hay contactos repetidos, entonces le explicamos al usuario que se van a tratar, si son duplicados se elimina alguno, y sino se le pedirá editar
                    # el nombre con el que fue agendado.
                if len(L_Repetidos) > 0:
                    QMessageBox.question(self, "Contactos Repetidos", "Se han detectado {} contactos repetidos.\nSe consideran contactos repetidos a aquellos que fueron agendados con el mismo APELLIDO y NOMBRE sin importar si coinciden o no sus números de celular.\nSe le va a pedir que genere un contacto para cada número de celular para así no perder sus datos.".format(len(L_Repetidos)), QMessageBox.Ok)

                    # Recorremos la lista en busca de todos los contactos iguales, y se le mostrarán al usuario ennumerados. Luego él deberá elegir cuál de
                    # todos los celulares conservará.
                    for i in L_Repetidos:
                        # Lista para guardar el nombre de los duplicados
                        L_Dup_Cel = []
                        # Texto que se arma para mostrar en mensajes al usuario
                        texto_ = ""
                        cont = 0
                        # Coloco el siguiente bucle en un try, porque si hay contactos duplicados entonces generará un error. Esto se debe a que durante su proceso se van 
                        # eliminando elementos de la lista, entonces se inicia con un Tope pero si se eliminaron elementos llegará al final de la lista y buscará elementos
                        # que no están más.
                        try:
                            for n in range(len(L_Agendado)):
                                if i == L_Agendado[n]:
                                    cont += 1
                                    texto_ += "\n" + str(cont) + "). {}".format(L_Celular[n])
                                    # Guardamos los índices de los duplicados
                                    L_Dup_Cel.append(n)
                        except:
                            pass

                        QMessageBox.question(self, "Contacto repetido", "El contacto {} se encuentra repetido {} veces.\nSe muestran enlistados los celulares asociados a ese contacto.\nA continuación se le irán pidiendo nombres para ser agendados de nuevo por cada celular salvo el último que quedará con el nombre original.{}".format(i, len(L_Dup_Cel), texto_), QMessageBox.Ok)
                        for g in range(len(L_Dup_Cel)-1):
                            aux = False
                            while aux == False:
                                texto, ok = QInputDialog.getText(self, "Ingrese nombre para: {}".format(i), "Ingrese el nombre que desea colocarle al contacto con el siguiente número de celular: {}\nRecuerde que en su celular debe agendar de igual forma a sus contactos.".format( L_Celular[L_Dup_Cel[g]]))
                                if ok == True and texto!= "":
                                    if self.Contador_Frecuencia(texto, L_Agendado) == 0:
                                        aux = True
                                        L_Agendado[L_Dup_Cel[g]] = texto
                                        L_Nombre1[L_Dup_Cel[g]] = texto
                                    else:
                                        QMessageBox.question(self, "Ya existe", "El contacto nuevo que quiere crear ya existe, elija otro nombre.", QMessageBox.Ok)


                # Debido a que se pueden agregar clientes manualmente sin exigir todos los datos, y luego puede que se carguen sus datos de manera autom., lo que hacemos es 
                    # controlar si ya está o no el contacto. Ej: Puede ser que se haya agendado al cliente Pg2589 y que además se necesite crearle un recordatorio. Se puede
                    # crear nuevo cliente en la App pero sólo con su nombre y sus recordatorios. Luego cuando se carga éste csv, controlamos si un nombre (Pg2589) ya existe,
                    # en ese caso entonces intentamos unificar datos con la bd.
                # Primero buscamos si ya está agendado con algún nombre
                for pos in range(len(L_Agendado)):

                    # Obtenemos el ID de un contacto si es que ya está agendado con ese nombre
                    Id_ = mdb.Dev_ID_ClienteTexto("Contacto", "Agendado_Cel", L_Agendado[pos])

                    # True: Contacto existente. False: Contacto nuevo
                    if Id_ > -1:
                        
                        # Bandera que indica que se va a actualizar un contacto
                        actualiza = False
                        
                        # Variables que se utilizarían en caso de tener que actualizar un contacto
                        # El dato de "L_Corporativo[n]", se agrega en "Comentario"
                        Apellido = ""
                        Nom1 = ""
                        Nom2 = ""
                        Nom3 = ""
                        Celular = ""
                        Direccion = ""
                        Comentario = ""

                        # Si hay algún dato nuevo en el contacto, lo actualizamos de manera directa. Si hay que modificar un dato entonces consultamos de ser necesario.
                            # Vamos corroborando dato por dato a ver si hay algo nuevo, pero en los datos que no hay cambios, igual cargamos en su variable correspondiente 
                            # el dato que debería llevar ya que puede ser que otro dato sea cuál active la actualización.
                            # Por ej, a pesar de que el CELULAR no cambie, le colocamos a la variable "Celular" el valor que hay en base de datos, porque tal vez la
                            # dirección es nueva y vamos a actualizar todos los datos, no vamos a hacer un llamado por cada dato nuevo, sino que al final se actualizan 
                            # todos por igual.
                        
                        # Como los datos están distribuídos en 2 tablas, lo hago por partes
                        reg_Contacto = mdb.Reg_Un_param_Int("./db\\clie.db", "Contacto", "ID", Id_)
                        for i in reg_Contacto:

                            # Celular
                            dato_viejo = i[3]
                            dato_nuevo = L_Celular[pos]
                            final = ""
                            aux = "Celular"
                            if dato_viejo != dato_nuevo:
                                
                                if dato_viejo == "":
                                    actualiza = True
                                    final = dato_nuevo
                                else:
                                    Rta = QMessageBox.question(self, "Actualizar Contactos", "Hay diferencias en el {} del contacto: {}. \n\nDato viejo: {}\nDato nuevo: {}\n\nSi desea actualizar al nuevo dato presione OK, de lo contrario se conservará el dato anterior.".format( aux, L_Agendado[pos], dato_viejo, dato_nuevo), QMessageBox.Ok | QMessageBox.Cancel)
                                    if Rta == QMessageBox.Ok:
                                        actualiza = True
                                        final = dato_nuevo
                                    else:
                                        final = dato_viejo
                            else:
                                final = dato_viejo
                            Celular = final

                            # Direccion
                            dato_viejo = i[5]
                            dato_nuevo = L_Direccion[pos]
                            final = ""
                            aux = "Dirección"
                            if dato_viejo != dato_nuevo:

                                if dato_viejo == "":
                                    actualiza = True
                                    final = dato_nuevo
                                else:
                                    Rta = QMessageBox.question(self, "Actualizar Contactos", "Hay diferencias en el {} del contacto: {}. \n\nDato viejo: {}\nDato nuevo: {}\n\nSi desea actualizar al nuevo dato presione OK, de lo contrario se conservará el dato anterior.".format( aux, L_Agendado[pos], dato_viejo, dato_nuevo), QMessageBox.Ok | QMessageBox.Cancel)
                                    if Rta == QMessageBox.Ok:
                                        actualiza = True
                                        final = dato_nuevo
                                    else:
                                        final = dato_viejo
                            else:
                                final = dato_viejo
                            Direccion = final
                            
                        reg_Contacto = mdb.Reg_Un_param_Int("./db\\clie.db", "DatosPersonales", "ID", Id_)
                        for i in reg_Contacto:

                            # Apellido
                            dato_viejo = i[1]
                            dato_nuevo = L_Apellido[pos]
                            final = ""
                            aux = "Apellido"
                            if dato_viejo != dato_nuevo:

                                if dato_viejo == "":
                                    actualiza = True
                                    final = dato_nuevo
                                else:
                                    Rta = QMessageBox.question(self, "Actualizar Contactos", "Hay diferencias en el {} del contacto: {}. \n\nDato viejo: {}\nDato nuevo: {}\n\nSi desea actualizar al nuevo dato presione OK, de lo contrario se conservará el dato anterior.".format( aux, L_Agendado[pos], dato_viejo, dato_nuevo), QMessageBox.Ok | QMessageBox.Cancel)
                                    if Rta == QMessageBox.Ok:
                                        actualiza = True
                                        final = dato_nuevo
                                    else:
                                        final = dato_viejo
                            else:
                                final = dato_viejo
                            Apellido = final

                            # Nom1
                            dato_viejo = i[3]
                            dato_nuevo = L_Nombre1[pos]
                            final = ""
                            aux = "1er Nombre"
                            if dato_viejo != dato_nuevo:

                                if dato_viejo == "":
                                    actualiza = True
                                    final = dato_nuevo
                                else:
                                    Rta = QMessageBox.question(self, "Actualizar Contactos", "Hay diferencias en el {} del contacto: {}. \n\nDato viejo: {}\nDato nuevo: {}\n\nSi desea actualizar al nuevo dato presione OK, de lo contrario se conservará el dato anterior.".format( aux, L_Agendado[pos], dato_viejo, dato_nuevo), QMessageBox.Ok | QMessageBox.Cancel)
                                    if Rta == QMessageBox.Ok:
                                        actualiza = True
                                        final = dato_nuevo
                                    else:
                                        final = dato_viejo
                            else:
                                final = dato_viejo
                            Nom1 = final
                            
                            # Nom2
                            dato_viejo = i[4]
                            dato_nuevo = L_Nombre2[pos]
                            final = ""
                            aux = "2do Nombre"
                            if dato_viejo != dato_nuevo:

                                if dato_viejo == "":
                                    actualiza = True
                                    final = dato_nuevo
                                else:
                                    Rta = QMessageBox.question(self, "Actualizar Contactos", "Hay diferencias en el {} del contacto: {}. \n\nDato viejo: {}\nDato nuevo: {}\n\nSi desea actualizar al nuevo dato presione OK, de lo contrario se conservará el dato anterior.".format( aux, L_Agendado[pos], dato_viejo, dato_nuevo), QMessageBox.Ok | QMessageBox.Cancel)
                                    if Rta == QMessageBox.Ok:
                                        actualiza = True
                                        final = dato_nuevo
                                    else:
                                        final = dato_viejo
                            else:
                                final = dato_viejo
                            Nom2 = final
                            
                            # Nom3
                            dato_viejo = i[5]
                            dato_nuevo = L_Nombre3[pos]
                            final = ""
                            aux = "3er Nombre"
                            if dato_viejo != dato_nuevo:

                                if dato_viejo == "":
                                    actualiza = True
                                    final = dato_nuevo
                                else:
                                    Rta = QMessageBox.question(self, "Actualizar Contactos", "Hay diferencias en el {} del contacto: {}. \n\nDato viejo: {}\nDato nuevo: {}\n\nSi desea actualizar al nuevo dato presione OK, de lo contrario se conservará el dato anterior.".format( aux, L_Agendado[pos], dato_viejo, dato_nuevo), QMessageBox.Ok | QMessageBox.Cancel)
                                    if Rta == QMessageBox.Ok:
                                        actualiza = True
                                        final = dato_nuevo
                                    else:
                                        final = dato_viejo
                            else:
                                final = dato_viejo
                            Nom3 = final

                            # Comentario
                            if actualiza == True:
                                if L_Corporativo[pos] != "":
                                    if L_Corporativo[pos] != i[8]:
                                        Comentario = "Editado autom. {}. {}. Se agrega sus datos de Whatsapp Bussines: {}".format(form.R_T_Dev_Fecha_Act(), i[8], L_Corporativo[pos])
                                else:
                                    Comentario = "Editado autom. {}. {}".format(form.R_T_Dev_Fecha_Act(), i[8])

                        # Una vez que tenemos los valores ajustados, procedemos a actualizar los datos
                        if actualiza == True:
                            mdb.Act_Cliente_csv(i[0], Celular, Apellido, Nom1, Nom2, Nom3, Direccion, Comentario)
                            Actualizados += 1

                    else:
                        # Armamos la lista que necesita la función que luego crea un nuevo cliente
                        Lista = []
                        # Tabla: Datos Personales
                        Lista.append(L_Apellido[pos])
                        Lista.append("")
                        Lista.append(L_Nombre1[pos])
                        Lista.append(L_Nombre2[pos])
                        Lista.append(L_Nombre3[pos])
                        Lista.append("")
                        Lista.append(0)
                        Lista.append("Agregado automáticamente por sistema. {}".format(form.R_T_Dev_Fecha_Act()))

                        # Tabla: Forma de pago
                        Lista.append(0)
                        Lista.append(0)
                        Lista.append(0)
                        Lista.append(0)
                        Lista.append(0)

                        # Tabla: Sus productos
                        Lista.append("")
                        Lista.append("")
                        Lista.append("")
                        Lista.append("")
                        Lista.append("")

                        # Tabla: Contacto
                        Lista.append(L_Agendado[pos])
                        Lista.append("")
                        Lista.append(L_Celular[pos])
                        Lista.append("")
                        Lista.append(L_Direccion[pos])
                        Lista.append("")
                        Lista.append("")
                        Lista.append("")
                        Lista.append("")
                        if L_Corporativo[pos] != "":
                            Lista.append("Wsp bussines: " + L_Corporativo[pos])
                        else:
                            Lista.append("")
                        Lista.append("")
                        Lista.append("")
                        Lista.append(6)
                        mdb.Add_Cliente_Nuevo(Lista)
                        Agregados += 1

                QMessageBox.question(self, "Resumen", "Se han controlado: {} contactos.\nSe actualizaron: {} contactos.\nSe agregaron: {} contactos.".format(Controlados, Actualizados, Agregados), QMessageBox.Ok)




                #HAY QUE ELIMINAR EL ARCHIVO DE EXCEL CREADO
                


            else:
                self.MuestraMsjOK("No se ha podido cargar la RUTA del archivo especificado. Error desconocido [1557]", "Error al intentar cargar Ruta")

    # Menú rápido para buscar clientes y cargarlos en ventana o en la ficha
    def Buscar_Clientes(self):

        # Extendemos un simple menú para que elija la manera de buscar clientes
        num, ok = QInputDialog.getInt(self, "Buscar Cliente", "Seleccione el parámetro para buscar clientes:\n0: Cancelar\n1: Manera en que fue agendado\n2: Apellido\n3:Primer nombre\n4: Cualquier nombre que coincida\n5: Número de Celular (No es necesario colocar correctamente el signo + o los espacios.", 0, 0, 5, 1) # QMessageBox.Ok | QMessageBox.Cancel)
        
        # True: Seleccionó una búsqueda correcta, de lo contrario se cancela la búsqueda automáticamente
        if ok == True and num > 0 and num < 6:
            Consulta = ""
            if num == 1:
                Consulta = "Ingrese el nombre o manera en que fue AGENDADO:"
            elif num == 2:
                Consulta = "Ingrese APELLIDO:"
            elif num == 3:
                Consulta = "Ingrese el PRIMER NOMBRE:"
            elif num == 4:
                Consulta = "Ingrese un NOMBRE:"
            elif num == 5:
                Consulta = "Ingrese un NÚMERO DE CELULAR:\nNota: No es necesario colocar el signo + o los espacios en blanco."

            valor, ok = QInputDialog.getText(self, "Buscar", Consulta)

            if ok == True and valor != "":
                Lista_ID_Res = []
                Lista_Nom_Re = []
                aux = form.Normalize(valor)
                # AGENDADO
                if num == 1:
                    # Primero buscamos coincidencia exacta
                    Tabla = mdb.Dev_Tabla_Clie("Contacto")
                    for reg in Tabla:
                        if aux == form.Normalize(reg[1]):
                            agend = reg[1]
                            Lista_ID_Res.append(reg[0])
                            lista = mdb.Dev_Lista_Registro_Int(mi_vars.DB_CLIENTES, "DatosPersonales", "ID", Lista_ID_Res[-1])
                            Lista_Nom_Re.append(agend + " /// " + lista[1] + " " + lista[2] + ", " + lista[3] + " " + lista[4] + " " + lista[5])
                    # Ahora cargamos todos los que comiencen con la misma frase
                    largo = len(aux)
                    Tabla = mdb.Dev_Tabla_Clie("Contacto")
                    for reg in Tabla:
                        if aux == form.Normalize(reg[1][0:largo]):
                            agend = reg[1]
                            if reg[0] in Lista_ID_Res:
                                pass
                            else:
                                Lista_ID_Res.append(reg[0])
                                lista = mdb.Dev_Lista_Registro_Int(mi_vars.DB_CLIENTES, "DatosPersonales", "ID", Lista_ID_Res[-1])
                                Lista_Nom_Re.append(agend + " /// " + lista[1] + " " + lista[2] + ", " + lista[3] + " " + lista[4] + " " + lista[5])
                # APELLIDO
                elif num == 2:
                    # Primero buscamos coincidencia exacta
                    Tabla = mdb.Dev_Tabla_Clie("DatosPersonales")
                    for reg in Tabla:
                        if aux == form.Normalize(reg[1]):
                            Lista_ID_Res.append(reg[0])
                            Lista_Nom_Re.append(reg[1] + " " + reg[2] + ", " + reg[3] + " " + reg[4] + " " + reg[5])
                    # Ahora cargamos todos los que comiencen con la misma frase
                    largo = len(aux)
                    Tabla = mdb.Dev_Tabla_Clie("DatosPersonales")
                    for reg in Tabla:
                        if aux == form.Normalize(reg[1][0:largo]):
                            if reg[0] in Lista_ID_Res:
                                pass
                            else:
                                Lista_ID_Res.append(reg[0])
                                Lista_Nom_Re.append(reg[1] + " " + reg[2] + ", " + reg[3] + " " + reg[4] + " " + reg[5])
                # PRIMER NOMBRE
                elif num == 3:
                    # Primero buscamos coincidencia exacta
                    Tabla = mdb.Dev_Tabla_Clie("DatosPersonales")
                    for reg in Tabla:
                        if aux == form.Normalize(reg[3]):
                            Lista_ID_Res.append(reg[0])
                            Lista_Nom_Re.append(reg[3] + " /// " + reg[1] + " " + reg[2] + ", " + reg[3] + " " + reg[4] + " " + reg[5])
                    # Ahora cargamos todos los que comiencen con la misma frase
                    largo = len(aux)
                    Tabla = mdb.Dev_Tabla_Clie("DatosPersonales")
                    for reg in Tabla:
                        if aux == form.Normalize(reg[3][0:largo]):
                            if reg[0] in Lista_ID_Res:
                                pass
                            else:
                                Lista_ID_Res.append(reg[0])
                                Lista_Nom_Re.append(reg[3] + " /// " + reg[1] + " " + reg[2] + ", " + reg[3] + " " + reg[4] + " " + reg[5])
                # CUALQUIER NOMBRE
                elif num == 4:
                    Consulta = "Ingrese un NOMBRE"
                # NUM CELULAR
                elif num == 5:
                    Consulta = "Ingr"

                Id_seleccionado = 0
                largo = len(Lista_ID_Res)

                # Si no se encontraron contactos se da aviso
                if largo == 0:
                    QMessageBox.question(self, "Aviso", "No se encontraron resultados.", QMessageBox.Ok)

                # Si se encontró uno sólo, se cargan sus datos
                elif largo == 1:
                    Id_seleccionado = Lista_ID_Res[0]
                
                # Si se encontraron más de un contacto, le damos para que seleccione cuál desea cargar
                else:

                    # Bucle que se deja de ejecutar sólo cuando se selecciona correctamente un contacto o cuando se cancela la búsqueda
                    seleccion = False
                    largo = len(Lista_Nom_Re)
                    msj_inicio = "Seleccione un contacto de {} resultados encontrados. Se mostrarán un máximo de 10 contactos por página.\n0: Para cancelar la búsqueda\n+ o Enter: Para buscar en la siguiente página\n-: Para buscar en la página anterior\nCon algún número ENTERO que figure en la lista mostrada, lo selecciona.\n\n".format(str(largo))
                    mensaje = ""
                    error = ""
                    cont_pag = 1
                    while seleccion == False:
                        aux = ""
                        for i in range(10):
                            if cont_pag - 1 + i == largo: break
                            aux += str(cont_pag + i) + ") {}\n".format(Lista_Nom_Re[cont_pag - 1 + i])
                        mensaje = error + msj_inicio + aux
                        error = ""
                        texto, ok = QInputDialog.getText(self, "Seleccione contacto", mensaje)
                        if ok == True:
                            if texto == "0":
                                seleccion = True
                            elif texto == "+" or texto == "":
                                if largo > 10:
                                    if cont_pag + 10 > largo:
                                        cont_pag = 1
                                    else:
                                        cont_pag += 10
                            elif texto == "-":
                                if largo > 10:
                                    if (cont_pag - 10) > 0:
                                        cont_pag = int(cont_pag - 10)
                                    else:
                                        if (cont_pag - 10) > (-9):
                                            cont_pag = 1
                                        else:
                                            cont_pag = largo - 9
                            else:
                                if form.Es_Numero_Int(texto) == True:
                                    valor = int(texto)
                                    if valor > 0 and valor <= largo:
                                        Id_seleccionado = Lista_ID_Res[valor - 1]
                                        seleccion = True
                                    else:
                                        error = "ERROR AL SELECCIONAR ÍNDICE DE CONTACTO, SELECCIONE DE NUEVO\n"
                                else:
                                    error = "NO HA SELECCIONADO UNA OPCIÓN VÁLIDA, O NO HA CARGADO UN NÚMERO ENTERO DE MANERA CORRECTA\n"
                        else:
                            seleccion = True
                
                if Id_seleccionado > 0:
                    self.Carga_Cliente(Id_seleccionado)

    def Carga_Cliente(self, ID):
        Contacto, Personales, SusProductos = mdb.Dev_Datos_Cliente(ID)

        # Agendamos en la variable local, el ID del cliente buscado
        self.CLIENTE_BUSCADO = ID
        self.ui.push_Ficha.setEnabled(True)

        # Rellenamos los Line_Edit
        aux = Personales[1]
        if Personales[2] != "":
            aux = aux + " " + Personales[2]
        aux = aux + ", " + Personales[3] + " " + Personales[4] + " " + Personales[5]
        self.ui.line_Ape_Nomb.setText(aux)
        self.ui.line_Celular.setText(Contacto[3])
        self.ui.line_Facebook.setText(Contacto[6])
        self.ui.line_Insta.setText(Contacto[7])
        self.ui.line_Contacto.setText(Contacto[10])
        reg = mdb.Dev_Reg_Segun_Tabla("ConfigConocimiento", "ID", Contacto[13])
        for i in reg:
            self.ui.line_Conexion.setText(i[2])
        
        # Rellenamos los textos que enlistan los productos de clientes
        auxm = ""
        auxs = ""
        # COMPRADO
        for caracter in SusProductos[1]:
            if caracter == "-":
                listaaux = mdb.Dev_Lista_Registro_Int(mi_vars.BaseDeDatos, "Productos", "ID", int(auxs))
                if listaaux[3] > 0:
                    linea = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Linea", "ID", listaaux[3], 3) + " "
                    tipo = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Tipo", "ID", listaaux[4], 3) + " "
                    interior = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Interior", "ID", listaaux[5], 3) + "\n"
                    auxm = auxm + linea + tipo + interior
                else:
                    for i in range(6,11):
                        if listaaux[i] != "":
                            auxm += listaaux[6] + "\n"
                            break
        self.ui.text_Comprado.setPlainText(auxm)

        # EN PROCESO
        for caracter in SusProductos[2]:
            if caracter == "-":
                listaaux = mdb.Dev_Lista_Registro_Int(mi_vars.BaseDeDatos, "Productos", "ID", int(auxs))
                if listaaux[3] > 0:
                    linea = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Linea", "ID", listaaux[3], 3) + " "
                    tipo = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Tipo", "ID", listaaux[4], 3) + " "
                    interior = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Interior", "ID", listaaux[5], 3) + "\n"
                    auxm = auxm + linea + tipo + interior
                else:
                    for i in range(6,11):
                        if listaaux[i] != "":
                            auxm += listaaux[6] + "\n"
                            break
        self.ui.text_EnProceso.setPlainText(auxm)

        # DESEOS
        for caracter in SusProductos[3]:
            if caracter == "-":
                listaaux = mdb.Dev_Lista_Registro_Int(mi_vars.BaseDeDatos, "Productos", "ID", int(auxs))
                if listaaux[3] > 0:
                    linea = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Linea", "ID", listaaux[3], 3) + " "
                    tipo = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Tipo", "ID", listaaux[4], 3) + " "
                    interior = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Interior", "ID", listaaux[5], 3) + " "
                    tamanio = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Productos", "ID", int(auxs), 11) + "cm "
                    litros = mdb.Dev_Dato_Int(mi_vars.BaseDeDatos, "Productos", "ID", int(auxs), 12) + "lts \n"
                    auxm = auxm + tipo + linea + interior + tamanio + litros
                else:
                    for i in range(6,13):
                        if listaaux[i] != "":
                            auxm += listaaux[i]
                            if listaaux[11] != "":
                                auxm += " " + listaaux[11] + "cm "
                            if listaaux[12] != "":
                                auxm += " " + listaaux[12] + "lts "
                            auxm += "\n"
                            auxs = ""
                            break
                auxs = ""
            else:
                auxs += caracter
        self.ui.text_Deseos.setPlainText(auxm)

    # Borra toda la info
    def Limpiar(self):
        self.CLIENTE_BUSCADO = 0
        self.ui.line_Ape_Nomb.clear()
        self.ui.line_Celular.clear()
        self.ui.line_Facebook.clear()
        self.ui.line_Insta.clear()
        self.ui.line_Contacto.clear()
        self.ui.line_Conexion.clear()
        self.ui.text_Deseos.clear()
        self.ui.text_Comprado.clear()
        self.ui.text_EnProceso.clear()
        self.ui.line_Ape_Nomb.setFocus()






