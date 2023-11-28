import wx

class ShipFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(550, 500))

        self.panel = wx.Panel(self, -1)

        self.txt_name = wx.TextCtrl(self.panel, -1, pos=(100, 20), size=(150, -1))
        self.lbl1 = wx.StaticText(self.panel, -1, label="Name", pos=(270, 25))
        self.txt_addr = wx.TextCtrl(self.panel, -1, pos=(100, 50), size=(200, -1))
        self.lbl2 = wx.StaticText(self.panel, -1, label="Address", pos=(320, 55))
        self.txt_csz = wx.TextCtrl(self.panel, -1, pos=(100, 80), size=(170, -1))
        self.lbl3 = wx.StaticText(self.panel, -1, label="City, State, Zip", pos=(290, 85))

        self.weight = wx.StaticText(self.panel, -1, label="Weight", pos=(70, 120))
        self.sm = wx.RadioButton(self.panel, -1, label='0 - 1.9lbs. $5.00', pos=(50, 140), style = wx.RB_GROUP)
        self.md = wx.RadioButton(self.panel, -1, label='2 - 4.9lbs. $8.00', pos=(50, 160))
        self.lg = wx.RadioButton(self.panel, -1, label='5 - 10lbs. $12.25', pos=(50, 180))

        self.spd = wx.StaticText(self.panel, -1, label="Speed", pos=(220, 120))
        self.ol = wx.RadioButton(self.panel, -1, label='Overland $2.75', pos=(200, 140), style = wx.RB_GROUP)
        self.thr = wx.RadioButton(self.panel, -1, label='3-day Air $6.15', pos=(200, 160))
        self.two = wx.RadioButton(self.panel, -1, label='2-day Air $10.70', pos=(200, 180))
        self.ov = wx.RadioButton(self.panel, -1, label='Overnight $15.50', pos=(200, 200))

        self.opt= wx.StaticText(self.panel, -1, label="Options", pos=(370, 120))
        self.exp = wx.CheckBox(self.panel, -1, label='Extra Padding $4', pos=(350, 140))
        self.gift = wx.CheckBox(self.panel, -1, label='Gift Wrapping $6', pos=(350, 160))

        self.btn_total = wx.Button(self.panel, label="Calculate Total", pos=(140, 250))
        self.btn_clear = wx.Button(self.panel, label="Clear Form", pos=(270, 250))

        self.btn_total.Bind(wx.EVT_BUTTON, self.calcTotal)
        self.btn_clear.Bind(wx.EVT_BUTTON, self.clearForm) 

        self.label1 = wx.StaticText(self.panel, label="Shipping Summary", pos=(185, 300))
        self.lbl_nm = wx.StaticText(self.panel, label="Name", pos=(185, 330))
        self.lbl_addr = wx.StaticText(self.panel, label="Address", pos=(185, 350))
        self.lbl_csz = wx.StaticText(self.panel, label="City, State, Zip", pos=(185, 370))
        self.lbl_tot = wx.StaticText(self.panel, label="$ 0", pos=(225, 390))
        
    def calcTotal(self, event):
        cost = 0
        if self.sm.GetValue():
            cost = 5
        elif self.md.GetValue():
            cost = 8
        else:
            cost = 12.25

        if self.ol.GetValue():
            cost += 2.75
        elif self.thr.GetValue():
            cost += 6.15
        elif self.two.GetValue():
            cost += 10.70
        else:
            cost += 15.50

        if self.exp.GetValue():
            cost += 4
        if self.gift.GetValue():
            cost += 6

        nm = self.txt_name.GetValue()
        self.lbl_nm.SetLabel(nm)

        addr = self.txt_addr.GetValue()
        self.lbl_addr.SetLabel(addr)

        csz = self.txt_csz.GetValue()
        self.lbl_csz.SetLabel(csz)

        cost = "$ %2.2f" % cost
        self.lbl_tot.SetLabel(cost)

    def clearForm(self, event):
        self.txt_name.SetValue("")
        self.txt_addr.SetValue("")
        self.txt_csz.SetValue("")
        self.sm.SetValue(1)
        self.ol.SetValue(1)
        self.exp.SetValue(0)
        self.gift.SetValue(0)
        self.lbl_tot.SetLabel('$ 0')
        self.lbl_nm.SetLabel("")
        self.lbl_addr.SetLabel("")
        self.lbl_csz.SetLabel("")

if __name__ == "__main__":
    app = wx.App()
    frame = ShipFrame(None, 'Shipping Calculator')
    frame.Show(True)
    app.MainLoop()

    

    

        

        
