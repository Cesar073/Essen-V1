self.ui.line_Codigo.setText(Datos[2])
self.ui.comboBox_Linea.setCurrentIndex(Datos[3])
self.ui.comboBox_Tipo.setCurrentIndex(Datos[4])
self.ui.comboBox_Interior.setCurrentIndex(Datos[5])
self.ui.line_Bazar.setText(Datos[6])
self.ui.line_Ayudavta.setText(Datos[7])
self.ui.line_Tamanio.setText(Datos[8])
self.ui.line_Litros.setText(Datos[9])
self.ui.line_Pcio_Costo.setText(Datos[10])
self.ui.line_Costo10.setText(Datos[11])
self.ui.line_PSPV.setText(Datos[12])
self.ui.line_Pcio_Lista.setText(Datos[13])
self.ui.line_Puntos.setText(Datos[14])
self.ui.line_Puntos_MG.setText(Datos[15])
self.ui.textEdit_Comentarios.setText(Datos[16])
self.Carga_Img(Datos[2])
self.ui.label_InfoMes.setText(Datos[18])

self.ui.checkBox_Activo.setChecked(False)
self.ui.comboBox_Linea.setCurrentIndex(0)
self.ui.line_Bazar.setText('')
self.ui.line_Ayudavta.setText('')
self.ui.comboBox_Tipo.setCurrentIndex(0)
self.ui.comboBox_Interior.setCurrentIndex(0)
self.ui.line_Tamanio.setText('')
self.ui.line_Litros.setText('')
self.ui.line_Pcio_Costo.setText('')
self.ui.line_Costo10.setText('')
self.ui.line_PSPV.setText('')
self.ui.line_Pcio_Lista.setText('')
self.ui.line_Puntos.setText('')
self.ui.line_Puntos_MG.setText('')
self.ui.textEdit_Comentarios.setText('')
self.ui.label_Imagen1.setText("SIN IMAGEN")
self.ui.label_InfoMes.setText('')




# Toma una lista y la convierte en un registro nuevo de la bd
def V_T_Guarda_Producto_Nuevo(self, Datos):
    global TOTAL
    Activo = Datos[1]
    Codigo = Datos[2]
    Linea = Datos[3]
    Tipo = Datos[4]
    Interior = Datos[5]
    ConceptoBazar = Datos[6]
    ConceptoAyVta = Datos[7]
    Tamanio = Datos[8]
    Litros = Datos[9]
    PcioCosto = Datos[10]
    Costo10 = Datos[11]
    PSPV = Datos[12]
    PcioLista = Datos[13]
    Puntos = Datos[14]
    PuntosMG = Datos[15]
    # Ajustes que se hacen si se están tratando archivos de Excel
    if EXCEL == True:
        Comentarios = ''
        self.Devuelve_Fondos()
    else:
        Comentarios = Datos[16]
    Imagen = Datos[17]
    Actualizado = Datos[18]
    TOTAL += 1
    MBD.Reg_Add(BaseDeDatos, Activo, Codigo, Linea, Tipo, Interior, ConceptoBazar, ConceptoAyVta, Tamanio, Litros, PcioCosto, Costo10, PSPV, PcioLista, Puntos, PuntosMG, Comentarios, Imagen, Actualizado)
    MBD.Act_Reg_Cant(BaseDeDatos, TOTAL, 'Productos')