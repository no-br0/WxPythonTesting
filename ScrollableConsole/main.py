import wx
import MainPanel



class Main(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Main, self).__init__(parent, *args, **kwargs)
        self.mainPanel = MainPanel.MainPanel(self)
        
        






app = wx.App()

frame = Main(None, title="My Game")
frame.Show()
app.MainLoop()
