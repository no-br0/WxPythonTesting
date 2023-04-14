import wx
import MyUI


class Console(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Console, self).__init__(title='Console', *args, **kwargs)
        self.text_display = TextDisplay(self)
        self.SetMaxSize(wx.Size(700,500))
        self.SetMinSize(wx.Size(700,500))
        self.SetBackgroundColour(wx.Colour(75,75,75))
        self.console_sizer = wx.GridBagSizer()
        self.console_sizer.SetMinSize(wx.Size(700,500))
        #self.console_sizer = wx.Sizer(wx.VERTICAL)
        self.SetSizer(self.console_sizer)
        self.console_sizer.Add(self.text_display, pos=(0,0), span=(3,6), flag=wx.EXPAND)
        
        self.output_button = MyUI.MyButton(self, label="Add Text")
        self.console_sizer.Add(self.output_button, pos=(4,0))
        
        self.clear_button = MyUI.MyButton(self, label='Clear Text')
        self.console_sizer.Add(self.clear_button, pos= (4,1))
        
        
        self.Add_Text("hello World")
        self.Add_Text("Line 2")
        self.Add_Text("Line 2")
        
        self.output_button.Bind(wx.EVT_BUTTON, self.Output_Button)
        self.clear_button.Bind(wx.EVT_BUTTON, self.Clear_Button)
        
        
    def Clear_Button(self, *args):
        self.text_display.Clear()
    
    def Output_Button(self, *args):
        self.Add_Text("Hello World")
        print("Hello World")
        
        
    def Add_Text(self, text:str):
        self.text_display.AddText(text)
        
        
        
        
class TextDisplay(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(TextDisplay, self).__init__(parent, *args, **kwargs)
        self.text_output = []
        self.SetMaxSize(wx.Size(600,400))
        self.SetMinSize(wx.Size(600,400))
        self.SetBackgroundColour(wx.BLACK)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.AddStretchSpacer(1)
        self.SetSizer(self.sizer)
        
        
    def AddText(self, text:str) -> None:
        st = wx.StaticText(self, label=text)
        st.SetBackgroundColour(wx.BLACK)
        st.SetForegroundColour(wx.GREEN)
        self.text_output.append(st)
        self.sizer.Add(st)
        self.sizer.Layout()
        
        
    def Clear(self) -> None:
        if len(self.text_output) > 0:
            for i in self.text_output:
                i.Destroy()
            self.text_output.clear()
            self.sizer.Layout()
            





if __name__ == '__main__':
    app = wx.App()
    console = Console(None)
    console.Show()
    app.MainLoop()