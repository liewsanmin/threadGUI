import wx, time, myThread_1, pdb, myEvent_1
class Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)  

        ########################################################################################################################
        self.yLoc0 = 10
        self.yLoc1 = self.yLoc0 + 20
        self.yLoc2 = self.yLoc1 + 20
        self.yLoc3 = self.yLoc2 + 20
        self.thd0ID = 0
        self.thd1ID = 1
        self.thd2ID = 2
        self.thd3ID = 3
        ########################################################################################################################

        ########################################################################################################################
        # thread 0 labels 
        self.label0 = wx.StaticText(parent, wx.ID_ANY, "Thread " + str(self.thd0ID), (10, self.yLoc0))
        self.t0 = wx.TextCtrl(parent, pos=(120,self.yLoc0), size=(70,20))
        self.onBtn0 = wx.Button(parent, wx.ID_ANY, "Start", (200, self.yLoc0))
        self.offBtn0 = wx.Button(parent, wx.ID_ANY, "Stop", (300, self.yLoc0))

        # thread 1 labels 
        self.label1 = wx.StaticText(parent, wx.ID_ANY, "Thread " + str(self.thd1ID), (10, self.yLoc1))
        self.t1 = wx.TextCtrl(parent, pos=(120,self.yLoc1), size=(70,20))
        self.onBtn1 = wx.Button(parent, wx.ID_ANY, "Start", (200, self.yLoc1))
        self.offBtn1 = wx.Button(parent, wx.ID_ANY, "Stop", (300, self.yLoc1))

        # thread 2 labels 
        self.label2 = wx.StaticText(parent, wx.ID_ANY, "Thread " + str(self.thd2ID), (10, self.yLoc2))
        self.t2 = wx.TextCtrl(parent, pos=(120,self.yLoc2), size=(70,20))
        self.onBtn2 = wx.Button(parent, wx.ID_ANY, "Start", (200, self.yLoc2))
        self.offBtn2 = wx.Button(parent, wx.ID_ANY, "Stop", (300, self.yLoc2))

        # thread 3 labels 
        self.label3 = wx.StaticText(parent, wx.ID_ANY, "Thread " + str(self.thd3ID), (10, self.yLoc3))
        self.t3 = wx.TextCtrl(parent, pos=(120,self.yLoc3), size=(70,20))
        self.onBtn3 = wx.Button(parent, wx.ID_ANY, "Start", (200, self.yLoc3))
        self.offBtn3 = wx.Button(parent, wx.ID_ANY, "Stop", (300, self.yLoc3))
        ########################################################################################################################

        ########################################################################################################################
        # binds
        self.onBtn0.Bind(wx.EVT_BUTTON, self.onToggle0)
        self.offBtn0.Bind(wx.EVT_BUTTON, self.offToggle0)

        self.onBtn1.Bind(wx.EVT_BUTTON, self.onToggle1)
        self.offBtn1.Bind(wx.EVT_BUTTON, self.offToggle1)

        self.onBtn2.Bind(wx.EVT_BUTTON, self.onToggle2)
        self.offBtn2.Bind(wx.EVT_BUTTON, self.offToggle2)

        self.onBtn3.Bind(wx.EVT_BUTTON, self.onToggle3)
        self.offBtn3.Bind(wx.EVT_BUTTON, self.offToggle3)
        ########################################################################################################################

        # indicate we don't have a worker thread yet
        self.thd0 = None
        self.thd1 = None
        self.thd2 = None
        self.thd3 = None

    # toggle functions
    ########################################################################################################################
    def onToggle0(self, event):
        if not self.thd0:
            self.thd0 = myThread_1.MyThread_1(self, self.thd0ID, 1)
            self.thd0.isOn = True
            self.thd0.isOff = False
            self.onBtn0.Disable()
            self.offBtn0.Enable()
    
    def offToggle0(self, event):
        if self.thd0:
            self.thd0.isOn = False
            self.thd0.isOff = True
            wx.PostEvent(self, myEvent_1.MyEvent_1(self.thd0, self, self.thd0ID, self.thd0.isOn, self.thd0.isOff))
            self.thd0 = None
        self.t0.SetValue(str(0))
        self.onBtn0.Enable()
        self.offBtn0.Disable()
    ########################################################################################################################

    ########################################################################################################################
    def onToggle1(self, event):
        if not self.thd1:
            self.thd1 = myThread_1.MyThread_1(self, self.thd1ID, 2)
            self.thd1.isOn = True
            self.thd1.isOff = False
            self.onBtn1.Disable()
            self.offBtn1.Enable()
    
    def offToggle1(self, event):
        if self.thd1:
            self.thd1.isOn = False
            self.thd1.isOff = True
            wx.PostEvent(self, myEvent_1.MyEvent_1(self.thd1, self, self.thd1ID, self.thd1.isOn, self.thd1.isOff))
            self.thd1 = None
        self.t1.SetValue(str(0))
        self.onBtn1.Enable()
        self.offBtn1.Disable()
    ########################################################################################################################

    ########################################################################################################################
    def onToggle2(self, event):
        if not self.thd2:
            self.thd2 = myThread_1.MyThread_1(self, self.thd2ID, 0.3)
            self.thd2.isOn = True
            self.thd2.isOff = False
            self.onBtn2.Disable()
            self.offBtn2.Enable()
    
    def offToggle2(self, event):
        if self.thd2:
            self.thd2.isOn = False
            self.thd2.isOff = True
            wx.PostEvent(self, myEvent_1.MyEvent_1(self.thd2, self, self.thd2ID, self.thd2.isOn, self.thd2.isOff))
            self.thd2 = None
        self.t2.SetValue(str(0))
        self.onBtn2.Enable()
        self.offBtn2.Disable()
    ########################################################################################################################

    ########################################################################################################################
    def onToggle3(self, event):
        if not self.thd3:
            self.thd3 = myThread_1.MyThread_1(self, self.thd3ID, 0.5)
            self.thd3.isOn = True
            self.thd3.isOff = False
            self.onBtn3.Disable()
            self.offBtn3.Enable()
    
    def offToggle3(self, event):
        if self.thd3:
            self.thd3.isOn = False
            self.thd3.isOff = True
            wx.PostEvent(self, myEvent_1.MyEvent_1(self.thd3, self, self.thd3ID, self.thd3.isOn, self.thd3.isOff))
            self.thd3 = None
        self.t3.SetValue(str(0))
        self.onBtn3.Enable()
        self.offBtn3.Disable()
        ########################################################################################################################