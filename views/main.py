from typing import TypedDict

from .root import Root
from .select import SelectView
from .result import ResultView

class Frames(TypedDict):
    select: SelectView
    result: ResultView

class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}

        self._add_frame(ResultView, "result")
        self._add_frame(SelectView, "select")
    
    def _add_frame(self, Frame, name: str):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")
    
    def switch(self, name: str):
        frame = self.frames[name]
        frame.tkraise()
    
    def start_mainloop(self):
        self.root.mainloop()