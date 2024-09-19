import tkinter as tk
from tkinter import ttk
from station import * 

class Window:
    def __init__(self, size):
        self.root = tk.Tk()
        self.root.title("Space Trader")
        self.root.geometry(f"{size[0]}x{size[1]}")
        #self.root.resizable(True,True)
        #self.root.minsize(800,600)
        #self.root.maxsize(1920,1080)
        self.root.tk.call('tk','scaling', 2)

        self.station_view = StationView()

        self.running_state = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running_state = True
        while self.running_state == True:
            self.redraw()

    def close(self):
        self.running_state = False

class StationView:
    def __init__(self):
        self.station_view = ttk.Treeview(columns=("Volume","Price","Amount"), style="Treeview")
        self.station_view.column('#0',width=300)
        self.station_view.heading('#0',text="Ware")
        self.station_view.column('Volume',width=120,anchor="e")
        self.station_view.heading('Volume',text="Volume")
        self.station_view.column('Price',width=120,anchor="e")
        self.station_view.heading('Price',text="Price")
        self.station_view.column('Amount',width=120,anchor="e")
        self.station_view.heading('Amount',text="Amount")
        self.station_view.place(x=30,y=30)

        style = ttk.Style()
        style.configure("Treeview", padding=8)

    def new_station(self, station: Station):
        self.station_view.delete()
        self.refresh(station)

    def refresh(self, station: Station):
        for ware in station.stock:
            self.station_view.insert('',tk.END,iid=station.stock.index(ware),text=ware.name,values=(ware.volume,ware.price,ware.amount))