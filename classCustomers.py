class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f"{self.name+self.surname}.{self.city}.Balance: {self.balance} pounds"
    def get_guest(self):
        return f'{self.name+self.surname} from {self.city}'

client1 = Clients("John ", "Smith", "London", 50)
client2 = Clients("Peter ", "Parker", "New York", 100)
client3 = Clients("Steve ", "Rogers", "New York", 150)
client4 = Clients("Bruce ", "Banner", "New York", 300)

guest_list = [client1, client2, client3, client4]

for guest in guest_list:
    print(guest.get_guest())

