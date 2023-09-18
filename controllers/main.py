from models.main import Model
from views.main import View

from .select import SelectController
from .result import ResultController

class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.select_controller = SelectController(model, view)
        self.result_controller = ResultController(model, view)
    
    def start(self):
        self.view.start_mainloop()