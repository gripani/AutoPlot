from wx import App, Frame, Panel, BoxSizer, TextCtrl, StaticText, Button, VERTICAL, ALL, EXPAND, CENTER, EVT_BUTTON

def create_text_control(panel, sizer, text_label, label_pos, text_pos, default_value, tool_tip):
    label_obj = StaticText(panel, label=text_label, pos=label_pos)
    sizer.Add(label_obj, 0, ALL|EXPAND, 5)
    text_obj = TextCtrl(panel, pos=text_pos, value=default_value)
    print(text_obj.SetSize(220, 23))
    text_obj.SetToolTip(tool_tip)
    sizer.Add(text_obj, 0, ALL|EXPAND, 5)
    return text_obj

def create_button(panel, sizer, btn_label, btn_pos, btn_effect): 
        btn = Button(panel, label=btn_label, pos=btn_pos)
        btn.Bind(EVT_BUTTON, btn_effect)
        sizer.Add(btn, 0, ALL|CENTER, 5)

class Widget(Frame):

    def __init__(self, parent, title, size, control_run):
        self.control_run = control_run
        super().__init__(parent, title=title, size=size)
        panel = Panel(self)
        sizer = BoxSizer(VERTICAL)

        self.text_fnct = create_text_control(panel, sizer, 'function:', (5,5), (75,5), 'sin(x); cos(x)',
                                            'inline function of x to plot, separate multiple values with semicolumn')
        self.text_x0 = create_text_control(panel, sizer, 'x lower lim:', (5, 35), (75, 35), '-pi', 
                                            'lower limit of x-axis')
        self.text_x1 = create_text_control(panel, sizer, 'w upper lim:', (5, 65), (75, 65), '+pi',
                                            'upper limit of x-axis')
        self.text_style = create_text_control(panel, sizer, 'linestyle:', (5, 95), (75, 95), '-;--', 
                                            'linestyle for plot function, separate multiple values with semicolumn')
        self.text_plt_label = create_text_control(panel, sizer, 'plot label:', (5, 125), (75, 125), 'sin(x); cos(x)', 
                                            'label for plot function, separate multiple values with semicolumn')
        self.text_x_label = create_text_control(panel, sizer, 'x label:', (5, 155), (75, 155), 'x (rad)',
                                            'label for x-axis')
        self.text_y_label = create_text_control(panel, sizer, 'y label:', (5, 185), (75, 185), 'y (au)', 
                                            'label for y-axis')
        self.text_plt_title = create_text_control(panel, sizer, 'plot title:', (5, 215), (75, 215), 'Sin and Cos of x', 
                                            'title of the figure')
        create_button(panel, sizer, 'Plot!', (5, 255), self.on_press)
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
        
    
def mainApp(title, size, control_run):
    app = App(False)
    widget = Widget(None, title, size, control_run)
    app.MainLoop()