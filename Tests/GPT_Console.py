import wx

count = 0

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 300))

        # Create a TextCtrl for console output
        self.console = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        # Disable the horizontal scrollbar
        #self.console.SetScrollbar(wx.HORIZONTAL, 0, 0, 0)
        self.console.SetScrollbar(wx.VERTICAL, 0, 0, 0)

        # Create a button to add text to the console
        self.button = wx.Button(self, label="Add Text")
        self.button.Bind(wx.EVT_BUTTON, self.on_button)

        # Add the widgets to a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.console, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(self.button, 0, wx.ALIGN_RIGHT|wx.ALL, 5)

        self.SetSizer(sizer)

        # Set the insertion point at the end of the text control
        #self.console.SetInsertionPointEnd()
        self.console.SetDefaultStyle(wx.TextAttr(wx.RED))

        self.Show()

    def on_button(self, event):
        global count
        # Append the new text to the console
        if count % 2 == 0:
            self.console.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        else:
            self.console.SetDefaultStyle(wx.TextAttr(wx.RED))
            
        
        
        #self.console.SetInsertionPointEnd()
        self.console.AppendText(f"This is some console output: {count}\n")
        self.console.SetScrollbar(wx.VERTICAL, 0, 0, 0)
        #self.console.ShowPosition(self.console.GetLastPosition())
        count += 1
        # Set the insertion point at the end of the text control

app = wx.App()
frame = MyFrame(None, title="Console Example")
app.MainLoop()
