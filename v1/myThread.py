import wx, time, threading, pdb
class MyThread(threading.Thread):
    def __init__(self, parent, ID, yLoc):
        threading.Thread.__init__(self)

        self.count = 0
        self.yLoc = yLoc
        self.ID = ID
        self.isOn = False

        ##################################################################
        # Thread labels
        self.label = wx.StaticText(parent, wx.ID_ANY, "Thread " + str(self.ID), (10, self.yLoc))
        self.t = wx.TextCtrl(parent, pos=(120,self.yLoc), size=(70,20))

        self.onBtn = wx.Button(parent, wx.ID_ANY, "Start", (200, self.yLoc))
        self.onBtn.Bind(wx.EVT_BUTTON, self.onToggle)

        self.offBtn = wx.Button(parent, wx.ID_ANY, "Stop", (300, self.yLoc))
        self.offBtn.Bind(wx.EVT_BUTTON, self.offToggle)
        ##################################################################

    def onToggle(self, event):
        print "starting timer..."
        self.isOn = True
        self.onBtn.Disable()
        self.offBtn.Enable()
        
    def offToggle(self, event):
        print "counter reset to 0!"
        self.isOn = False
        self.onBtn.Enable()
        self.offBtn.Disable()
        self.count = 0
        self.t.SetValue(str(self.count))

    def run(self):
        try:
            print("Started Thread: " + str(self.ID))
            while True:
                pass
        except KeyboardInterrupt:
            print("Joining thread")
            self.join()