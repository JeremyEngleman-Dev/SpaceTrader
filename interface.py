import tkinter as tk
from tkinter import ttk
from station import * 
from controller import *

class Window(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller: Controller = None

        # Station
        self.station_label = ttk.Label(master=parent,text="The Station")
        self.station_label.place(x=30,y=10,height=40)

        self.station_window = ttk.Frame(master=parent,width=800,height=1000,relief="sunken")
        self.station_window.place(x=10,y=60,width=800-20,height=600)

        self.station_ware_view = ttk.Treeview(
            master=self.station_window,
            columns=("Volume","Price","Amount"),
            style="Treeview"
        )
        self.station_ware_view.column('#0',width=280)
        self.station_ware_view.heading('#0',text="Ware")
        self.station_ware_view.column('Volume',width=120,anchor="e")
        self.station_ware_view.heading('Volume',text="Volume")
        self.station_ware_view.column('Price',width=120,anchor="e")
        self.station_ware_view.heading('Price',text="Price")
        self.station_ware_view.column('Amount',width=120,anchor="e")
        self.station_ware_view.heading('Amount',text="Amount")
        self.station_ware_view.place(x=0,y=0,relwidth=1,height=300)

        self.fuel_label = ttk.Label(master=self.station_window,text=f"Fuel Price: {0}")
        self.fuel_label.place(x=30,y=300+10,height=40)

        # Ship
        self.ship_label = ttk.Label(master=parent,text="Your Ship")
        self.ship_label.place(x=10 + 800 + 20 + 30,y=10, height=40)

        self.ship_window = ttk.Frame(master=parent,width=800,height=1000,relief="sunken")
        self.ship_window.place(x=10 + 800 + 20,y=60,width=800-40,height=600)

        self.ship_ware_view = ttk.Treeview(
            master=self.ship_window,
            columns=("Volume","Amount"),
            style="Treeview"
        )
        self.ship_ware_view.column('#0',width=280)
        self.ship_ware_view.heading('#0',text="Ware")
        self.ship_ware_view.column('Volume',width=120,anchor="e")
        self.ship_ware_view.heading('Volume',text="Volume")
        self.ship_ware_view.column('Amount',width=120,anchor="e")
        self.ship_ware_view.heading('Amount',text="Amount")
        self.ship_ware_view.place(x=0,y=0,relwidth=1,height=300)

        style = ttk.Style()
        style.configure("Treeview", padding=4)

    def set_controller(self, controller):
        self.controller = controller
        self.initialize_jump_button()

    def initialize_jump_button(self):
        self.jump_button = ttk.Button(
            master=self.station_window,
            text="JUMP",
            command=self.controller.jump_to_new_station
        )
        self.jump_button.place(x=800-150-30,y=310,width=150,height=100)

    def refresh_station_window(self):
        if self.controller:
            for item in self.station_ware_view.get_children():
                self.station_ware_view.delete(item)
            station = self.controller.get_current_station()
            for ware in station.stock:
                self.station_ware_view.insert(
                    '',
                    tk.END,
                    iid=station.stock.index(ware),
                    text=ware.name,
                    values=(ware.volume,ware.price,ware.amount)
                )
            self.fuel_label.config(text=f"Fuel Price: {station.fuel_price}")

    def refresh_ship_window(self):
        if self.controller:
            ship = self.controller.get_current_ship()
            self.ship_ware_view.delete()
            for ware in ship.cargo:
                self.ship_ware_view.insert(
                    '',
                    tk.END,
                    iid=ship.cargo.index(ware),
                    text=ware.name,
                    values=(ware.volume,ware.amount)
                )