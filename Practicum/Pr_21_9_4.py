class Client:
    def __init__(self,name,surname,city,balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def info(self):
        return f'{self.name} {self.surname}. {self.city}.'


client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Денис", "Сидоров", "Казань", 20)
client_3 = Client("Олег", "Николаев", "Кострома", 200)

client_list = [client_1, client_2, client_3]
for client in client_list:
    print(client.info())
