import wx

class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        
        self.console_pnl = wx.Panel(self)
        
        self.text = wx.StaticText(self.console_pnl, label="Hello World")
        font = self.text.GetFont()
        font.PointSize = 10
        font = font.Bold()
        self.text.SetFont(font)
        
        self.button = wx.Button(self.console_pnl, label="Test Button")
        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        sizer.Add(self.button, wx.SizerFlags().Border(wx.LEFT, 25))
        self.console_pnl.SetSizer(sizer)
        
        
        
        
        self.CreateStatusBar()
        self.SetStatusText("This is the Console Window Status Bar")
        
        
if __name__ == '__main__':
    app = wx.App()
    console_window = Window(None, title="Main Window")
    console_window.Show()
    app.MainLoop()