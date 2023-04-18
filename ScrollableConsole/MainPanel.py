import wx
import random
import Console
import ButtonPanel


class MainPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(MainPanel, self).__init__(parent, *args, **kwargs)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.console = Console.Console(self)
        self.buttonPanel = ButtonPanel.ButtonPanel(self)
        self.BackgroundColour = (115,110,178)
        #print(random.randint(0,255))
        self.SetSizer(self.sizer)
        self.sizer.Add(self.console)
        self.sizer.Add(self.buttonPanel)