from Console import Console
from StatScreen import StatScreen
import wx

app = wx.App()

stat_screen = StatScreen(None)
stat_screen.Show()

console_screen = Console(None)
console_screen.Show()

app.MainLoop()