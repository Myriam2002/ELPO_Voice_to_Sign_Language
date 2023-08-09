from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

    
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_facecolor('#393939')
        self.canvas.figure.set_facecolor('#393939')
        #self.canvas.figure.set_facecolor('black')
        #self.canvas.axes.set_facecolor('black')
        #self.canvas.axes.set_axiscolor('white')
        self.canvas.axes.spines['left'].set_color('white')  
        self.canvas.axes.spines['right'].set_color('white')        
        self.canvas.axes.spines['top'].set_color('white')  

        self.canvas.axes.spines['bottom'].set_color('white')  
        self.canvas.axes.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
        self.canvas.axes.tick_params(axis='y', colors='white')  #setting up Y-axis tick color to black
        self.setLayout(vertical_layout)