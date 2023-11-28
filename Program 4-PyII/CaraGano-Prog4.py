import wx
import sqlite3 as db
import requests
import datetime



class DataList(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title='API Data', size=(700, 600))
        panel = wx.Panel(self, -1)

        self.date = wx.StaticText(panel, -1, 'Todays Date: ', pos=(200, 10))
        self.overallGainLoss = wx.StaticText(panel, -1, 'Net Gain/Loss: ', pos=(200, 30))
        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT, pos=(40, 60), size=(600, 370))

        self.list.InsertColumn(0, 'Company', width=120)
        self.list.InsertColumn(1, 'Symbol', width=80)
        self.list.InsertColumn(2, 'Purchase Price', width=100)
        self.list.InsertColumn(3, 'Current Price', width=100)
        self.list.InsertColumn(4, 'Shares', width=80)
        self.list.InsertColumn(5, 'Gain/Loss', width=80)

        display = wx.Button(panel, -1, 'Display Data', size=(-1, 50), pos=(200, 450))
        cancel = wx.Button(panel, -1, 'Cancel', size=(-1, 50), pos=(400, 450))

        display.Bind(wx.EVT_BUTTON, self.OnDisplay)
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)

        self.Centre()
        
        
    def OnDisplay(self, event):
        try:
            self.list.DeleteAllItems()
            con = db.connect('tech_stocks.db')
            cur = con.cursor()

            cur.execute('SELECT * FROM dow_stocks')
            results = cur.fetchall()

            cur.close()
            con.close()

            token = 'cl010fhr01qhjei2tsf0cl010fhr01qhjei2tsfg'

            x = datetime.datetime.now()
            date = x.strftime("%A %B %d, %Y : %H:%M")
            self.date.SetLabel(f"Today's Date: {date}")

            overallGainLoss = 0
                
                        
            for r in results:
                company = r[1]
                symbol = r[3]
                shares = r[4]
                purchase_price = r[5]

                url = 'https://finnhub.io/api/v1/quote?symbol=' + symbol +'&token=' + token
                response = requests.get(url)

                if response.status_code == 200:
                    
                    stkData = response.json()

                    current_price = stkData['c']

                    stkGainLoss = shares * (current_price - purchase_price)
                    stkGainLoss = round(stkGainLoss, 2)
                    overallGainLoss += stkGainLoss
                    overallGainLoss = round(overallGainLoss, 2)
                    #self.list.Append(r)#company, symbol, purchase_price, current_price, shares, stkGainLoss)
                    index = self.list.InsertItem(self.list.GetItemCount(), company)
                    self.list.SetItem(index, 1, symbol)
                    self.list.SetItem(index, 2, str(purchase_price))
                    self.list.SetItem(index, 3, str(current_price))
                    self.list.SetItem(index, 4, str(shares))
                    self.list.SetItem(index, 5, str(stkGainLoss))
                self.overallGainLoss.SetLabel(f'Net Gain/Loss: {overallGainLoss}')

        except db.Error as err:
            dlg = wx.MessageDialog(self, str(err), 'Error occured')
            dlg.ShowModal()

    def OnCancel(self, event):
        self.Close()

app = wx.App()
dl = DataList(None, -1, 'Stock Data')
dl.Show()
app.MainLoop()
