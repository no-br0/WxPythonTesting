import wx

class MyButton(wx.Button):
    def __init__(self, parent, label:str, *args, **kwargs):
        super(MyButton, self).__init__(parent, style=wx.BORDER_NONE, *args, **kwargs)
        self.BackgroundColour = wx.Colour(100,100,100)
        self.ForegroundColour = wx.Colour(120,120,120)
        self.text = wx.StaticText(self, label=label)
        self.text.Center(wx.BOTH)
        self.text.SetForegroundColour(wx.BLUE)
        self.text.SetBackgroundColour(wx.BLACK)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        
    def on_paint(self, event):
        #print("On Paint")
        dc = wx.BufferedPaintDC(self)
        gc = wx.GraphicsContext.Create(dc)
        
        
        #Create a transparent Rectangle
        gc.SetBrush(wx.TRANSPARENT_BRUSH)
        gc.DrawRectangle(0,0, self.GetSize().GetWidth(), self.GetSize().GetHeight())
        
        
        #Create border
        pen = wx.Pen(wx.Colour(255,0,0), width=2)
        gc.SetPen(pen)
        gc.DrawRectangle(0,0, self.GetSize().GetWidth(), self.GetSize().GetHeight())