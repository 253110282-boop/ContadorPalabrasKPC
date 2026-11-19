import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # carga de nuestra vista
        uic.loadUi("ContadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.contarPalabras)

    def contarPalabras(self):
        # Recupera el texto 
        texto = self.editCaracteres.text()
        
        # Separa las palabras
        textoSeparado = texto.split()
        print(textoSeparado)  

        #contar las palabras 
        cantidadPalabras=len(textoSeparado)
        self.tvPalabras.setText(f"Palabras:{cantidadPalabras}")
        
        # Contar los caracteres 😸
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres+=len(palabra)
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")


        #aqui abajo logica 
        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet("color: #FF0000;")
        else:
            self.tvCaracteres.setStyleSheet("color: #F4F4F4;")

        if cantidadPalabras >= 20:
            self.tvPalabras.setStyleSheet("color: #FF0000;")
        else:
            self.tvPalabras.setStyleSheet("color: #F4F4F4;")


        print("Se ha presionado el botón")
       
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())