class Phone:
    def __init__(self, sim_cards_list: list):  # Исправлено __init__
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number: int, call_to_number: str):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {self.__sim_cards_list[sim_card_number - 1]}")
        else:
            print("Неверный номер сим-карты")

# Предположим, что класс Computer должен быть определен, например:
class Computer:
    def __init__(self, cpu_cores: int, ram_gb: int):
        self.cpu_cores = cpu_cores
        self.ram_gb = ram_gb

    def make_computations(self):
        # Пример простой "вычислительной" логики
        return f"Результат вычислений: {self.cpu_cores * self.ram_gb}"


# Тестирование
comp = Computer(4, 16)
print(comp.make_computations())

phone = Phone(["Beeline", "Megacom", "O! Mobile"])
phone.call(1, "+996 777 99 88 11")
phone.call(2, "+996 555 11 22 33")
phone.call(3, "+996 707 44 55 66")
