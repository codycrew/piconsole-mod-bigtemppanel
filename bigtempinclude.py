from kivy.uix.relativelayout import RelativeLayout
from kivy.app         import App

# ==============================================================================
# BigTemp Panel RELATIVE LAYOUT CLASS
# ==============================================================================
class BigTempPanel(RelativeLayout):

    # Initialise 'BigTempPanel' relative layout class
    def __init__(self,**kwargs):
        super(BigTempPanel,self).__init__(**kwargs)
        if not hasattr(App.get_running_app(),'BigTempPanel'):
            App.get_running_app().BigTempPanel = []
            App.get_running_app().BigTempPanel.append(self)
        else:
            App.get_running_app().BigTempPanel.append(self)

class BigTempButton(RelativeLayout):
    pass

