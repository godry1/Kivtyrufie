# напиши модуль для работы с анимацией
from kivy.uix.boxlayout import BoxLayout


class Runner(BoxLayout):
    value = NumericProperty(0)
    fineshed = BooleanProperty(False)

    def __init__(self, total = 10, steptime = 1, autorepeat = True, bcolor = (0.73, 0.15, 0.96, 1)btext_inprogress = 'Приседеания', **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.autorepeat  = autorepeat
        self.btext_inprogress = btext_inprogress
        self.animation = (Animation(pos_hint = {'top':1.0}, background_color = bcolor))
        self.add_widget(self.bnt)
    
        

    def start(self):
        self.value = 0
        self.finished = False
        

    def next(self, widget, step):
        pass