import wx
class MyEvent_1(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, thread, parent, ID, isOn, isOff):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.ID = ID
        self.SetEventType(self.ID)
        self.isOn = isOn
        self.isOff = isOff
        self.parent = parent
        self.thread = thread
        if self.isOn:
            if self.ID == 0:
                self.parent.t0.SetValue(str(self.thread.count))
            if self.ID == 1:
                self.parent.t1.SetValue(str(self.thread.count))
            if self.ID == 2:
                self.parent.t2.SetValue(str(self.thread.count))
            if self.ID == 3:
                self.parent.t3.SetValue(str(self.thread.count))
        if self.isOff:
            print("Stopped Thread: " + str(self.ID))