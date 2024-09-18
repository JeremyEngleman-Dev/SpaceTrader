from ware import *
from ship import *

class Library:
    def __init__(self):
        self.Wares: Ware = [
            Ware("Mechanical Parts",12,120,400,200),
            Ware("Basic Engine",25,1130,3280,20),
            Ware("Food",2,6,16,800),
            Ware("Medical Supplies",4,55,294,200),
            Ware("Raw Metal Ore",40,450,1200,120),
            Ware("Refined Metal",45,1123,2324,100),
            Ware("Electronic Components",8,135,535,450),
            Ware("General Goods",2,5,45,380),
            Ware("Luxury Goods",3,125,689,80),
            Ware("Coal",13,45,520,135),
            Ware("Water",5,3,17,230),
            Ware("Advanced Engine",40,4563,12485,15),
            Ware("Construction Materials",38,110,678,100)
        ]