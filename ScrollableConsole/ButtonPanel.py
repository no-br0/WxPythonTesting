import wx
import MyUI

class ButtonPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(ButtonPanel, self).__init__(parent, *args, **kwargs)
        
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        
        self.buttons: list[MyUI.MyButton] = []
        self.AddButton(MyUI.MyButton(self, "Test"), self.TestOutput_Handler)
        
    def AddButton(self, button:wx.Button, func):
        self.buttons.append(button)
        self.sizer.Add(button)
        button.Bind(wx.EVT_BUTTON, handler=func)
        
        
    def TestOutput_Handler(self, event) -> None:
        #will need to handle output into the 
        print("hello world")
        