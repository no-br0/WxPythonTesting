import wx

class StatScreen(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(StatScreen, self).__init__(title='StatScreen', *args, **kwargs)
        self.stat_panel = StatPanel(self)
        self.stat_panel.AddText("Hello World")
        self.stat_panel.AddText("Hello World")
        self.stat_panel.AddText("Hello World")
        
        #self.stat_panel = wx.Panel(self)
        
        #self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        #self.text_1 = wx.StaticText(self.stat_panel, label='Line 1')
        #self.text_2 = wx.StaticText(self.stat_panel, label='Line 2')
        
        #self.sizer.Add(self.text_1)
        #self.sizer.Add(self.text_2)
        
        #self.stat_panel.SetSizer(self.sizer)
        

class StatPanel(wx.Panel):
    def __init__(self, parent):
        super(StatPanel, self).__init__(parent)
        self.text_output: list[wx.StaticText] = [] 
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        
    def AddText(self, text:str) -> None:
        st = wx.StaticText(self, label=text)
        st.SetBackgroundColour(wx.BLACK)
        st.SetBackgroundColour(wx.GREEN)
        self.text_output.append(st)
        self.sizer.Add(st)
        self.sizer.Layout()
        
        
        
        
if __name__ == '__main__':
    app = wx.App()
    stat_screen = StatScreen(None)
    stat_screen.Show()
    app.MainLoop()