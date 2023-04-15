import wx
import MyUI


class ConsoleWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ConsoleWindow, self).__init__(title='Console', *args, **kwargs)
        self.console = Console(self)
        self.SetMaxSize(wx.Size(700,500))
        self.SetMinSize(wx.Size(700,500))
        self.SetBackgroundColour(wx.Colour(75,75,75))
        self.console_sizer = wx.GridBagSizer()
        self.console_sizer.SetMinSize(wx.Size(700,500))
        #self.console_sizer = wx.Sizer(wx.VERTICAL)
        self.SetSizer(self.console_sizer)
        self.console_sizer.Add(self.console, pos=(0,0), span=(10,10), flag=wx.EXPAND)
        
        self.output_button = MyUI.MyButton(self, label="Add Text")
        self.console_sizer.Add(self.output_button, pos=(11,0))
        
        self.clear_button = MyUI.MyButton(self, label='Clear Text')
        self.console_sizer.Add(self.clear_button, pos= (11,1))
        
        
        #self.Add_Text("hello World")
        #self.Add_Text("Line 2")
        #self.Add_Text("Line 2")
        
        self.output_button.Bind(wx.EVT_BUTTON, lambda event: self.Output_Button())
        self.clear_button.Bind(wx.EVT_BUTTON, lambda event: self.Clear_Button())
        
        
    def Clear_Button(self, *args):
        self.console.Clear()
    
    def Output_Button(self, *args):
        self.Add_Text("Hello World")
        #print("Hello World")
        
        
    def Add_Text(self, text:str):
        self.console.AddText(text)
        
        

class Console(wx.ScrolledWindow):
    def __init__(self, parent, *args, **kwargs):
        super(Console, self).__init__(parent, wx.ID_ANY, style=wx.TE_NO_VSCROLL, *args, **kwargs)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.SetScrollRate(1,1)
        
        
        self.panel = TextDisplay(self, size=wx.Size(700,400), style=wx.TE_NO_VSCROLL)
        self.SetVirtualSize(self.panel.GetSize())
        
        self.SetSizer(self.sizer)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.AddText("hello World")
        self.AddText("Line 2")
        self.AddText("Line 2")
        #self.panel.SetMaxSize(wx.Size(700,400))
        #self.panel.SetMinSize(wx.Size(700,400))
        
        self.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        
        
    def OnMouseWheel(self, event):
        current_pos = self.GetViewStart()
        wheel_rotation = event.GetWheelRotation()
        self.Scroll(current_pos[0], current_pos[1] - wheel_rotation)


    def AddText(self, text:str) -> None:
        self.panel.AddText(text)
        
        
    def Clear(self) -> None:
        self.panel.Clear()

        
        
        
class TextDisplay(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(TextDisplay, self).__init__(parent, *args, **kwargs)
        
        self.text_output = []
        #self.SetVirtualSize(wx.Size(700,400))
        #self.SetMinSize(wx.Size(700,400))
        #self.SetMaxSize(wx.Size(700,1000))
        self.SetBackgroundColour(wx.BLACK)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.sizer.AddStretchSpacer(1)
        
        
        
        
    def AddText(self, text:str) -> None:
        print("AddText")
        st = wx.StaticText(self, label=text)
        st.SetBackgroundColour(wx.BLACK)
        st.SetForegroundColour(wx.GREEN)
        self.text_output.append(st)
        self.sizer.Add(st, 1, wx.EXPAND)
        self.sizer.Layout()
        
        
    def Clear(self) -> None:
        print("Clear")
        if len(self.text_output) > 0:
            for i in self.text_output:
                i.Destroy()
            self.text_output.clear()
            self.sizer.Layout()
            





if __name__ == '__main__':
    app = wx.App()
    console = ConsoleWindow(None)
    console.Show()
    app.MainLoop()