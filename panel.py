import wx, time, myThread, pdb
class Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)  

        yLoc = 10
        self.thd0 = myThread.MyThread(self, 0, yLoc)
        self.thd1 = myThread.MyThread(self, 1, yLoc + 30)
        self.thd2 = myThread.MyThread(self, 2, yLoc + 60)
        self.thd3 = myThread.MyThread(self, 3, yLoc + 90)

        #start timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(1000)

        self.thd0.start()
        self.thd1.start()
        self.thd2.start()
        self.thd3.start()

    def update(self, event):
        print "\nupdated: ",
        print time.ctime()
        if (self.thd0.isOn):
            self.thd0.t.SetValue(str(self.thd0.count))
            self.thd0.count += 1
        if (self.thd1.isOn):
            self.thd1.t.SetValue(str(self.thd1.count))
            self.thd1.count += 1
        if (self.thd2.isOn):
            self.thd2.t.SetValue(str(self.thd2.count))
            self.thd2.count += 1
        if (self.thd3.isOn):
            self.thd3.t.SetValue(str(self.thd3.count))
            self.thd3.count += 1