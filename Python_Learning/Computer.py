class Computer():
    """This Class containes sketch of the labtops """
    #class Attribute
    type = "Electronic"
    # instance attribute
    def __init__(self, Color, HardDisk, Memory , Proccesor , VGA , USB,Price):
        self.Color = Color
        self.HardDisk = HardDisk
        self.Memory = Memory
        self.Proccesor = Proccesor
        self.VGA = VGA
        self.USB = USB
        self.Price = Price
    specs = [Color, HardDisk, Memory , Proccesor , VGA , USB, Price]
    LapTop = [Dell,Hp]


    def move(self,Laptop,specs):
        input(Laptop)
        if Laptop == "Dell":
            Dell = Computer("Black",120,"16GB","CoreDue 18Ghz","Nevdia 2GB",None,"5700L.E")


