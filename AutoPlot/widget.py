from pyforms.gui.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

from AutoPlot.control import Control 

class Widget(BaseWidget):

    def __init__(self):
        super().__init__('Simple example 1')

        self._fnct  = ControlText('Function',)
        self._x0 = ControlText('x Lower Limit')
        self._x1 = ControlText('x Upper Limit')
        self._style = ControlText('Linestyle')
        self._plt_label = ControlText('Plot Label')
        self._x_label = ControlText('x Label')
        self._y_label = ControlText('y Label')
        self._plt_title = ControlText('Plot Title')
        self._button = ControlButton('Plot!')
    
        self._button.value = self.__buttonAction

    def __buttonAction(self):
        stored_dict_values = { 
            'fnct' : self._fnct.value,  
            'x0' : self._x0.value, 
            'x1' : self._x1.value,
            'style' : self._style.value,  
            'plt_label' : self._plt_label.value,
            'x_label' : self._x_label.value, 
            'y_label' : self._y_label.value, 
            'plt_title': self._plt_title.value 
        }
        cntrl = Control(**stored_dict_values)
        cntrl.run()
        
