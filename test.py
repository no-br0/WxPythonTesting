import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="My Game", size=(400, 300))
        
        # Create the main panel
        self.panel = wx.Panel(self)

        # Create a sizer to hold the buttons and text output
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a static text widget for output
        self.output_text = wx.StaticText(self.panel, label="Welcome to my game!")
        self.sizer.Add(self.output_text, 0, wx.ALL, 5)

        # Create the buttons
        self.start_button = wx.Button(self.panel, label="Start game")
        self.load_button = wx.Button(self.panel, label="Load game")
        self.quit_button = wx.Button(self.panel, label="Quit")

        # Add the buttons to the sizer
        self.sizer.Add(self.start_button, 0, wx.ALL, 5)
        self.sizer.Add(self.load_button, 0, wx.ALL, 5)
        self.sizer.Add(self.quit_button, 0, wx.ALL, 5)

        # Set the panel sizer
        self.panel.SetSizer(self.sizer)

        # Bind the button events
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start)
        self.load_button.Bind(wx.EVT_BUTTON, self.on_load)
        self.quit_button.Bind(wx.EVT_BUTTON, self.on_quit)

    def on_start(self, event):
        self.output_text.SetLabel("Starting game...")

    def on_load(self, event):
        self.output_text.SetLabel("Loading game...")

    def on_quit(self, event):
        self.output_text.SetLabel("Quitting game...")
        self.Close()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
