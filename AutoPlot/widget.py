from pyforms.gui.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

class Widget(BaseWidget):

    def __init__(self):
        super().__init__('Simple example 1')

        self._firstname  = ControlText('First name', 'Default value')
        self._middlename = ControlText('Middle name')
        self._lastname   = ControlText('Lastname name')
        self._fullname   = ControlText('Full name')
        self._button     = ControlButton('Press this button')