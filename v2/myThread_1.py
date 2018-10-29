import wx, time, threading, pdb, myEvent_1
class MyThread_1(threading.Thread):
    def __init__(self, parent, ID, freq):
        threading.Thread.__init__(self)

        self.count = 0
        self.ID = ID
        self.isOn = False
        self.isOff = False
        self.freq = freq
        self.parent = parent
        self.start()

    def run(self):
        try:
            print("Started Thread: " + str(self.ID))
            while True:
                time.sleep(self.freq)
                if self.isOn:
                    wx.PostEvent(self.parent, myEvent_1.MyEvent_1(self, self.parent, self.ID, self.isOn, self.isOff))
                    self.count += 1
        except KeyboardInterrupt:
            print("Joining thread")
            self.join()