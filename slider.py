from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class slider(QMainWindow):
    def __init__(self):
        super().__init__()

        loader=QUiLoader()
        self.ui=loader.load('slider.ui',None)
        self.ui.show()

        self.ui.slider1.valueChanged.connect(self.valueR)
        self.ui.slider2.valueChanged.connect(self.valueG)
        self.ui.slider3.valueChanged.connect(self.valueB)

      
    

    def valueR(self):
        value_r=str(self.ui.slider1.value())
        self.ui.lbl_r.setText(value_r) 
        self.ui.lbl_color.setStyleSheet(f'background-color:rgb({value_r},{self.ui.slider2.value()},{self.ui.slider3.value()})') 
     
        

    def valueG(self):
        value_g=str(self.ui.slider2.value())
        self.ui.lbl_g.setText(value_g)
        self.ui.lbl_color.setStyleSheet(f'background-color:rgb({self.ui.slider1.value()},{value_g},{self.ui.slider3.value()})') 
        

    def valueB(self):
        value_b=str(self.ui.slider3.value())
        self.ui.lbl_b.setText(value_b) 
        self.ui.lbl_color.setStyleSheet(f'background-color:rgb({self.ui.slider1.value()},{self.ui.slider3.value()},{value_b})')  
        

app=QApplication()
window=slider()        
app.exec_()
