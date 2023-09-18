from models.main import Model
from views.main import View

class ResultController:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["result"]
        self._bind()
    
    def _bind(self):
        self.frame.back_btn.config(command=self.changeToSelectView)
    
    def changeToSelectView(self):
        self.view.switch("select")
