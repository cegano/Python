import wx
import sqlite3 as db

class MyDialog(wx.Dialog):

    def __init__(self):

        wx.Dialog.__init__(self, None, title="Dialog", size=(450, 350))

        lbl = wx.StaticText(self, label='Enter New Speeding Ticket', pos=(150, -1))

        self.tid = wx.TextCtrl(self, -1, '', pos=(95, 50))
        wx.StaticText(self, -1, 'Ticket ID:', pos=(20, 50))

        self.date = wx.TextCtrl(self, -1, '', pos=(95, 90))
        wx.StaticText(self, -1, 'Date:', pos=(20, 90))

        self.time = wx.TextCtrl(self, -1, '', pos=(95, 130))
        wx.StaticText(self, -1, 'Time:', pos=(20, 130))

        self.aspd = wx.TextCtrl(self, -1, '', pos=(95, 170))
        wx.StaticText(self, -1, 'Actual Speed:', pos=(20, 170))

        self.pspd = wx.TextCtrl(self, -1, '', pos=(300, 50))
        wx.StaticText(self, -1, 'Posted Speed:', pos=(220, 50))

        self.mph = wx.TextCtrl(self, -1, '', pos=(300, 90))
        wx.StaticText(self, -1, 'MPH Over:', pos=(220, 90))

        self.age = wx.TextCtrl(self, -1, '', pos=(300, 130))
        wx.StaticText(self, -1, 'Age:', pos=(220, 130))

        self.sex = wx.TextCtrl(self, -1, '', pos=(300, 170))
        wx.StaticText(self, -1, 'Sex:', pos=(220, 170))

        okbtn = wx.Button(self, id=wx.ID_OK, pos=(180, 250))

class DataList(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(700, 600))
        panel = wx.Panel(self, -1)

        self.tbl_name = wx.StaticText(panel, -1, 'Ticket Data', pos=(300, 10))
        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT, pos=(40, 50), size=(600, 370))

        self.list.InsertColumn(0, 'tid', width=40)
        self.list.InsertColumn(1, 'stop_date', width=80)
        self.list.InsertColumn(2, 'stop_time', width=80)
        self.list.InsertColumn(3, 'actual_speed', width=80)
        self.list.InsertColumn(4, 'posted_speed', width=100)
        self.list.InsertColumn(5, 'mph_over', width=80)
        self.list.InsertColumn(6, 'age', width=40)
        self.list.InsertColumn(7, 'violator_sex', width=80)

        display = wx.Button(panel, -1, 'Display', size=(-1, 50), pos=(100, 450))
        insert = wx.Button(panel, -1, 'Insert Ticket', size=(-1, 50), pos=(300, 450))
        cancel = wx.Button(panel, -1, 'Cancel', size=(-1, 50), pos=(500, 450))

        display.Bind(wx.EVT_BUTTON, self.OnDisplay)
        insert.Bind(wx.EVT_BUTTON, self.OnAdd)
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)

        self.Centre()

    def getAllData(self):
        self.list.DeleteAllItems()
        con = db.connect('speeding_tickets.db')
        cur = con.cursor()

        cur.execute('SELECT * FROM tickets')
        results = cur.fetchall()
        for row in results:
            self.list.Append(row)

        cur.close()
        con.close()

    def OnDisplay(self, event):
        try:
            self.getAllData()

        except lite.Error as error:
            dlg = wx.MessageDialog(self, str(error), 'Error occured')
            dlg.ShowModal()

    def OnAdd(self, event):
        dlg = MyDialog()
        btnID = dlg.ShowModal()
        if btnID == wx.ID_OK:
            date = dlg.date.GetValue()
            time = dlg.time.GetValue()
            aspd = dlg.aspd.GetValue()
            pspd = dlg.pspd.GetValue()
            mph = dlg.mph.GetValue()
            age = dlg.age.GetValue()
            sex = dlg.sex.GetValue()

        if date != "" and time!= "" and aspd != "" and pspd != "" and mph != "" and age != "" and sex != "":
            try:
                con = db.connect('speeding_tickets.db')
                cur = con.cursor()

                sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

                cur.execute(sql, (None, date, time, aspd, pspd, mph, age, sex))
                con.commit()

                self.getAllData()

            except lite.Error as error:
                dlg = wx.MessageDialog(self, str(error), 'Error occured')
                dlg.ShowModal()

        dlg.Destroy()



    def OnCancel(self, event):
        self.Close()

app = wx.App()
dl = DataList(None, -1, 'Traffic Tickets')
dl.Show()
app.MainLoop()
                    
            
