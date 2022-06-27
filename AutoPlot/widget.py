from wx import Frame, Panel, BoxSizer, TextCtrl, StaticText, Button, VERTICAL, ALL, EXPAND, CENTER, EVT_BUTTON

class Widget(Frame):

    def __init__(self, parent, title, size, control_run):
        self.control_run = control_run
        super().__init__(parent, title=title, size=size)
        panel = Panel(self)
        sizer = BoxSizer(VERTICAL)

        label_fnct = StaticText(panel, label='function:', pos=(5, 5))
        sizer.Add(label_fnct, 0, ALL|EXPAND, 5)
        self.text_fnct = TextCtrl(panel, pos=(75, 5), value='sin(x); cos(x)')
        self.text_fnct.SetToolTip('inline function of x to plot, separate multiple values with semicolumn')
        sizer.Add(self.text_fnct, 0, ALL|EXPAND, 5)

        label_x0 = StaticText(panel, label='x lower lim:', pos=(5, 35))
        sizer.Add(label_x0, 0, ALL|EXPAND, 5)
        self.text_x0 = TextCtrl(panel, pos=(75, 35), value='-pi')
        self.text_x0.SetToolTip('lower limit of x-axis')
        sizer.Add(self.text_x0, 0, ALL|EXPAND, 5)

        label_x1 = StaticText(panel, label='x upper lim:', pos=(5, 65))
        sizer.Add(label_x1, 0, ALL|EXPAND, 5)
        self.text_x1 = TextCtrl(panel, pos=(75, 65), value='+pi')
        self.text_x0.SetToolTip('upper limit of x-axis')
        sizer.Add(self.text_x1, 0, ALL|EXPAND, 5)

        label_style = StaticText(panel, label='linestyle:', pos=(5, 95))
        sizer.Add(label_style, 0, ALL|EXPAND, 5)
        self.text_style = TextCtrl(panel, pos=(75, 95), value='-; --')
        self.text_style.SetToolTip('linestyle for plot function, separate multiple values with semicolumn')
        sizer.Add(self.text_style, 0, ALL|EXPAND, 5)

        label_plt_label = StaticText(panel, label='plot label:', pos=(5, 125))
        sizer.Add(label_plt_label, 0, ALL|EXPAND, 5)
        self.text_plt_label = TextCtrl(panel, pos=(75, 125), value='sin(x); cos(x)')
        self.text_plt_label.SetToolTip('label for plot function, separate multiple values with semicolumn')
        sizer.Add(self.text_plt_label, 0, ALL|EXPAND, 5)

        label_x_label = StaticText(panel, label='x label:', pos=(5, 155))
        sizer.Add(label_x_label, 0, ALL|EXPAND, 5)
        self.text_x_label = TextCtrl(panel, pos=(75, 155), value='x (rad)')
        self.text_x_label.SetToolTip('label for x-axis')
        sizer.Add(self.text_x_label, 0, ALL|EXPAND, 5)

        label_y_label = StaticText(panel, label='y label:', pos=(5, 185))
        sizer.Add(label_y_label, 0, ALL|EXPAND, 5)
        self.text_y_label = TextCtrl(panel, pos=(75, 185), value='y (au)')
        self.text_y_label.SetToolTip('label for y-axis')
        sizer.Add(self.text_y_label, 0, ALL|EXPAND, 5)

        label_plt_title = StaticText(panel, label='plot title:', pos=(5, 215))
        sizer.Add(label_plt_title, 0, ALL|EXPAND, 5)
        self.text_plt_title = TextCtrl(panel, pos=(75, 215), value='Sin and Cos of x')
        self.text_plt_title.SetToolTip('title of the figure')
        sizer.Add(self.text_plt_title, 0, ALL|EXPAND, 5)

        btn = Button(panel, label='Plot!', pos=(5, 255))
        btn.Bind(EVT_BUTTON, self.on_press)
        sizer.Add(btn, 0, ALL|CENTER, 5)

        self.Show()

    def on_press(self, event):
        dict_values = {}
        dict_values['fnct'] = self.text_fnct.GetValue()
        dict_values['x0'] = self.text_x0.GetValue() 
        dict_values['x1'] = self.text_x1.GetValue() 
        dict_values['style'] = self.text_style.GetValue() 
        dict_values['plt_label'] = self.text_plt_label.GetValue() 
        dict_values['x_label'] = self.text_x_label.GetValue() 
        dict_values['y_label'] = self.text_y_label.GetValue() 
        dict_values['plt_title'] = self.text_plt_title.GetValue() 
        self.control_run(**dict_values)
        
    
