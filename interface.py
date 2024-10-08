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
            style="Treeview",
            selectmode="browse"
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
        self.station_ware_view.bind('<ButtonRelease-1>', lambda e: self.controller.on_station_ware_select(self.station_ware_view.focus()))
        self.fuel_label = ttk.Label(master=self.station_window,text=f"Fuel Price: {0}")
        self.fuel_label.place(x=10,y=300+15,height=40,width=150)

        self.fuel_to_buy = ttk.Entry(master=self.station_window)
        self.fuel_to_buy.insert(0,0)
        self.fuel_to_buy.place(x=180,y=315,width=100,height=40)

        self.ware_to_buy = ttk.Entry(master=self.station_window)
        self.ware_to_buy.insert(0,0)
        self.ware_to_buy.place(x=10,y=550,width=100,height=40)

        self.ware_to_buy_price = ttk.Label(master=self.station_window,text=f"{0} Cr")
        self.ware_to_buy_price.place(x=10,y=500)

        # Ship
        self.ship_label = ttk.Label(master=parent,text="Your Ship")
        self.ship_label.place(x=10 + 800 + 20 + 30,y=10, height=40)

        self.ship_window = ttk.Frame(master=parent,width=800,height=1000,relief="sunken")
        self.ship_window.place(x=10 + 800 + 20,y=60,width=800-40,height=600)

        self.ship_ware_view = ttk.Treeview(
            master=self.ship_window,
            columns=("Volume","Amount"),
            style="Treeview",
            selectmode="browse"
        )
        self.ship_ware_view.column('#0',width=280)
        self.ship_ware_view.heading('#0',text="Ware")
        self.ship_ware_view.column('Volume',width=120,anchor="e")
        self.ship_ware_view.heading('Volume',text="Volume")
        self.ship_ware_view.column('Amount',width=120,anchor="e")
        self.ship_ware_view.heading('Amount',text="Amount")
        self.ship_ware_view.place(x=0,y=0,relwidth=1,height=300)
        self.ship_ware_view.bind('<ButtonRelease-1>', lambda e: self.controller.on_ship_ware_select(self.ship_ware_view.focus()))

        style = ttk.Style()
        style.configure("Horizontal.TProgressbar", background="green")
        style.configure("Treeview",rowheight=28)

        self.ship_stock = ttk.Progressbar(master=self.ship_window, value=20, style="Horizontal.TProgressbar")
        self.ship_stock.place(x=10,y=310,width=400,height=40)
        self.ship_stock_label = ttk.Label(master=self.ship_window,text=f"Cargo: {0}/{0}")
        self.ship_stock_label.place(x=10+400+10,y=310,height=40)

        self.ship_fuel = ttk.Progressbar(master=self.ship_window, value=0, style="Horizontal.TProgressbar")
        self.ship_fuel.place(x=10,y=360,width=400,height=40)
        self.ship_fuel_label = ttk.Label(master=self.ship_window,text=f"Fuel: {0}/{0}")
        self.ship_fuel_label.place(x=10+400+10,y=360,height=40)

        self.player_account = ttk.Label(master=self.ship_window,text=f"Credits: {0}")
        self.player_account.place(x=10,y=410,height=40)

        self.ware_to_sell = ttk.Entry(master=self.ship_window)
        self.ware_to_sell.insert(0,0)
        self.ware_to_sell.place(x=10,y=550,width=100,height=40)

        self.ware_to_sell_price = ttk.Label(master=self.ship_window,text=f"{0} Cr")
        self.ware_to_sell_price.place(x=10,y=500)

        self.refresh_station_window()
        self.refresh_ship_window()

    def set_controller(self, controller):
        self.controller = controller
        self.initialize_controls()
        self.refresh_station_window()
        self.refresh_ship_window()

    def initialize_controls(self):
        self.jump_button = ttk.Button(
            master=self.station_window,
            text="JUMP TO\nNEW\nSTATION",
            command=self.controller.jump_to_new_station
        )
        self.jump_button.place(x=620,y=310,width=150,height=100)

        self.fuel_buy_button = ttk.Button(
            master=self.station_window,
            text="BUY FUEL",
            command=self.controller.buy_fuel
        )
        self.fuel_buy_button.place(x=460,y=310,width=150,height=50)

        self.fuel_to_buy_decrease = ttk.Button(
            master=self.station_window,
            text="-",
            command=self.controller.decrement_fuel_to_buy_amount
        )
        self.fuel_to_buy_decrease.place(x=290,y=315,width=40,height=40)

        self.fuel_to_buy_increase = ttk.Button(
            master=self.station_window,
            text="+",
            command=self.controller.increment_fuel_to_buy_amount
        )
        self.fuel_to_buy_increase.place(x=340,y=315,width=40,height=40)

        self.fuel_to_buy_max = ttk.Button(
            master=self.station_window,
            text="MAX",
            command=self.controller.max_fuel_to_buy_amount
        )
        self.fuel_to_buy_max.place(x=390,y=315,width=60,height=40)

        self.ware_to_buy_decrease = ttk.Button(
            master=self.station_window,
            text="-",
            command=self.controller.decrement_ware_to_buy_amount
        )
        self.ware_to_buy_decrease.place(x=120,y=550,width=40,height=40)

        self.ware_to_buy_increase = ttk.Button(
            master=self.station_window,
            text="+",
            command=self.controller.increment_ware_to_buy_amount
        )
        self.ware_to_buy_increase.place(x=170,y=550,width=40,height=40)

        self.ware_to_buy_max = ttk.Button(
            master=self.station_window,
            text="MAX",
            command=self.controller.max_ware_to_buy_amount
        )
        self.ware_to_buy_max.place(x=220,y=550,width=60,height=40)

        self.ware_buy_button = ttk.Button(
            master=self.station_window,
            text="BUY WARE",
            command=self.controller.buy_ware
        )
        self.ware_buy_button.place(x=620,y=490,width=150,height=100)

        self.ware_to_sell_decrease = ttk.Button(
            master=self.ship_window,
            text="-",
            command=self.controller.decrement_ware_to_sell_amount
        )
        self.ware_to_sell_decrease.place(x=120,y=550,width=40,height=40)

        self.ware_to_sell_increase = ttk.Button(
            master=self.ship_window,
            text="+",
            command=self.controller.increment_ware_to_sell_amount
        )
        self.ware_to_sell_increase.place(x=170,y=550,width=40,height=40)

        self.ware_to_sell_max = ttk.Button(
            master=self.ship_window,
            text="MAX",
            command=self.controller.max_ware_to_sell_amount
        )
        self.ware_to_sell_max.place(x=220,y=550,width=60,height=40)

        self.ware_sell_button = ttk.Button(
            master=self.ship_window,
            text="SELL WARE",
            command=self.controller.sell_ware
        )
        self.ware_sell_button.place(x=600,y=490,width=150,height=100)

    def refresh_fuel_to_buy(self, fuel):
        self.fuel_to_buy.delete(0, tk.END)
        self.fuel_to_buy.insert(0,fuel)

    def refresh_ware_to_buy(self, ware):
        self.ware_to_buy.delete(0, tk.END)
        self.ware_to_buy.insert(0,ware)

    def refresh_ware_to_sell(self, ware):
        self.ware_to_sell.delete(0, tk.END)
        self.ware_to_sell.insert(0,ware)

    def refresh_ware_to_buy_price(self,price):
        self.ware_to_buy_price.configure(text=f"{price} Cr")

    def refresh_ware_to_sell_price(self,price):
        self.ware_to_sell_price.configure(text=f"{price} Cr")

    def refresh_station_window(self):
        if self.controller:
            # Refresh station wares in treeview
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
            # Refresh station ware information
            self.fuel_label.config(text=f"Fuel Price: {station.fuel_price}")
            self.refresh_fuel_to_buy(station.fuel_to_buy_amount)
            self.refresh_ware_to_buy(station.ware_to_buy_amount)

    def refresh_ship_window(self):
        if self.controller:
            # Refresh ship wares in treeview
            for item in self.ship_ware_view.get_children():
                self.ship_ware_view.delete(item)
            ship = self.controller.get_current_ship()
            player = self.controller.get_player()
            ship_cargo_volume = 0
            for ware in ship.cargo:
                self.ship_ware_view.insert(
                    '',
                    tk.END,
                    iid=ship.cargo.index(ware),
                    text=ware.name,
                    values=(ware.volume,ware.amount)
                )
                ship_cargo_volume += ware.amount * ware.volume
            # Refresh ship ware information
            self.ship_stock["maximum"] = ship.cargo_capacity
            self.ship_stock["value"] = ship_cargo_volume
            self.ship_stock_label.config(text=f"Cargo: {ship_cargo_volume}/{ship.cargo_capacity}")
            self.ship_fuel["maximum"] = ship.fuel_capacity
            self.ship_fuel["value"] = ship.fuel_current
            self.ship_fuel_label.config(text=f"Fuel: {ship.fuel_current}/{ship.fuel_capacity}")
            self.player_account.config(text=f"Credits: {player.account}")
            self.refresh_ware_to_sell(ship.ware_to_sell_amount)