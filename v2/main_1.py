import wx, pdb, panel_1

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Threads Controlling a GUI",
                                   size=(500,500))
        # Add a panel_1 so it looks the correct on all platforms
        panel_1.Panel(self)
        
def main():
    app = wx.PySimpleApp()
    MyForm().Show()
    app.MainLoop()

# Run the program
if __name__ == "__main__":
    main()