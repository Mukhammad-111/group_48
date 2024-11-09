class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.memory * 2, self.cpu * 2

    def __lt__(self, other):
        return self.memory < other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __str__(self):
        return f'CPU: {self.cpu}, MEMORY: {self.memory}'

class Phone:
    def __init__(self):
        self.__sim_cards_list = ['Beeline', 'Mega']
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if type(sim_card_number) == int and sim_card_number == len(self.sim_cards_list):
            operator = self.sim_cards_list[sim_card_number - 1]
            return f'Идет звонок на номер {call_to_number} с симкарты-{sim_card_number}-{operator}'
        elif type(sim_card_number) == int and sim_card_number == len(self.sim_cards_list):
            operator = self.sim_cards_list[sim_card_number - 1]
            return f'Идет звонок на номер {call_to_number} с симкарты-{sim_card_number}-{operator}'
    def __str__(self):
        return f'SIM_CARDS_LIST: {self.sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        Phone.__init__(self)
        Computer.__init__(self, cpu, memory)

    def use_gps(self, location):
        return f'Вам следует добратся до {location}'


computer = Computer(16,512)
phone = Phone()
smart_phone1 = SmartPhone(8,128)
smart_phone2 = SmartPhone(16,256)

accessories_list = [computer, phone, smart_phone1, smart_phone2]
for access in accessories_list:
    print(access)

print(computer.make_computations())
print(phone.call(2, "+996550525131"))
print(phone.sim_cards_list)
print(smart_phone1.use_gps('Batken'))
print(smart_phone1.memory < smart_phone2.memory)
print(computer.memory >= smart_phone2.memory)
print(smart_phone1.memory == computer.memory)




