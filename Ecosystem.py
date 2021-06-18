import json
import random


class Properties():
    json_open = open('properties.json', 'r')
    json_read = json.load(json_open)

    @staticmethod
    def get_width_aquarium():
        return Properties.json_read['aqua_width']

    @staticmethod
    def get_height_aquarium():
        return Properties.json_read['aqua_height']

    @staticmethod
    def get_algae():
        return Properties.json_read['algae']

    @staticmethod
    def get_predator_fish():
        return Properties.json_read['predator_fish']

    @staticmethod
    def get_prey_fish():
        return Properties.json_read['prey_fish']


class Aquarium():
    @staticmethod
    def create_aquarium():
        w = Properties.get_width_aquarium()
        h = Properties.get_height_aquarium()
        len_aquarium = int(w) * int(h)
        aquarium = []
        i = 0
        while i < len_aquarium:
            aquarium.append('')
            i += 1
        return aquarium

    @staticmethod
    def create_algae():
        return 'Algae'

    @staticmethod
    def set_algae():
        global aquarium
        static_g = Properties.get_algae()
        set_com = int(len(aquarium) / int(static_g) - 1)
        a = set_com
        i = 0
        while i < int(static_g):
            aquarium[set_com] = Aquarium.create_algae()
            i += 1
            set_com = set_com + a
        return aquarium

    @staticmethod
    def create_prey_fish():
        return random.choice(['HM119', 'HF119'])

    @staticmethod
    def set_prey_fish():
        global aquarium
        static_pf = Properties.get_prey_fish()
        set_com = int(len(aquarium) / int(static_pf) - 1)
        a = set_com
        i = 0
        while i < int(static_pf):
            if aquarium[set_com] == '':
                aquarium[set_com] = Aquarium.create_prey_fish()
                set_com = set_com + a
            else:
                aquarium[set_com + 1] = Aquarium.create_prey_fish()
            i += 1
        return aquarium

    @staticmethod
    def create_predator_fish():
        return random.choice(['PM119', 'PF119'])

    @staticmethod
    def set_predator_fish():
        global aquarium
        static_pf = Properties.get_predator_fish()
        set_com = int(len(aquarium) / int(static_pf) - 1)
        a = set_com
        i = 0
        while i < int(static_pf):
            if aquarium[set_com] == '':
                aquarium[set_com] = Aquarium.create_predator_fish()
                set_com = set_com + a
            else:
                aquarium[set_com + 1] = Aquarium.create_predator_fish()
                set_com = set_com + a
            i += 1

        return aquarium


aquarium = Aquarium.create_aquarium()
Aquarium.set_algae()
Aquarium.set_predator_fish()
Aquarium.set_prey_fish()


def decrease_energy(fish):
    global aquarium
    a = []
    for i in fish:
        a.append(i)
    new_energy = int(a[4]) - 1
    if new_energy > 0:
        a[4] = str(new_energy)
        new_fish = ''.join(a)
        return new_fish
    else:
        energy_low = ''
        return energy_low


def increase_energy(fish):
    global aquarium
    a = []
    new_fish = fish
    for i in fish:
        a.append(i)
    new_energy = int(a[4]) + 2
    if new_energy > 9:
        pass
    else:
        a[4] = str(new_energy)
        new_fish = ''.join(a)
    return new_fish


def increase_fish_old(fish):
    global aquarium
    a = []
    for i in fish:
        a.append(i)
    new_old = int(a[2]) + 1
    a[2] = str(new_old)

    if int(a[2]) <= 3:
        a[3] = '1'
    elif int(a[2]) >= 3 and int(a[2]) <= 6:
        a[3] = '2'
    elif int(a[2]) >= 6 and int(a[2]) <= 9:
        a[3] = '3'
    else:
        empty = ''

        return empty

    new_fish = ''.join(a)

    return new_fish


def data():
    new_aquarium = []
    i = 0
    l_aq = len(aquarium)
    while i < l_aq:
        new_aquarium.append('')
        i += 1
    return new_aquarium


new_aquarium = data()


def movement():
    global aquarium
    global new_aquarium
    i = 0
    len_arr = len(aquarium)

    while i < len_arr:
        if aquarium[-i] == '':
            pass

        elif aquarium[-i].startswith('PF') or aquarium[-i].startswith('PM'):
            new_old_fish = increase_fish_old(aquarium[-i])
            aquarium[-i] = new_old_fish
            stat_num = -i + 3
            if aquarium[-i] != '':
                if aquarium[stat_num].startswith('HM') or aquarium[stat_num].startswith('HF'):
                    new_energy_plus = increase_energy(aquarium[-i])
                    aquarium[-i] = new_energy_plus
                else:
                    new_energy = decrease_energy(aquarium[-i])
                    aquarium[-i] = new_energy

            new_aquarium[stat_num] = aquarium[-i]
            new_aquarium[-i] = ''

        elif aquarium[-i].startswith('HM') or aquarium[-i].startswith('HF'):
            new_old_fish2 = increase_fish_old(aquarium[-i])
            aquarium[-i] = new_old_fish2
            new_energy = decrease_energy(aquarium[-i])
            aquarium[-i] = new_energy
            stat_num2 = -i + 2
            if aquarium[stat_num2] == 'Algae':
                new_energy_plus2 = increase_energy(aquarium[-i])
                aquarium[-i] = new_energy_plus2
            new_aquarium[stat_num2] = aquarium[-i]
            new_aquarium[-i] = ''

        elif aquarium[-i] == 'Algae':

            new_aquarium[-i] = 'Algae'
        i += 1
    aquarium.clear()
    aquarium = new_aquarium.copy()
    return new_aquarium

def print_table(color, message):
    print('|' + '  ' + color + message.ljust(7) + Colors.BLACK, end='')

def output_to_console():
    i = movement()
    len_aquarium = len(i)
    j = 0
    k = 0
    print("-------------------------------------------------------------------------------------------------------")
    while j < len_aquarium:
        if k == int(Properties.get_width_aquarium()):
            print('')
            k = 0
        k += 1
        if str(i[j]).startswith('HM') or str(i[j]).startswith('HF'):

            print_table(Colors.GREEN, str(i[j]))
        elif str(i[j]).startswith('PM') or str(i[j]).startswith('PF'):
            print_table(Colors.RED, str(i[j]))
        else:
            print_table(Colors.BLUE, str(i[j]))

        j += 1
    print('')
    print('-------------------------------------------------------------------------------------------------------')


class Colors:
    BLACK = '\033[30m\033[1m'
    RED = '\033[31m\033[1m'
    GREEN = '\033[32m\033[1m'
    BLUE = '\033[34m\033[1m'


while True:
    output_to_console()
    pause = input('\nНажміть Enter щоб продовжити або 0 щоб закінчити')
    if pause == '0':
        exit(0)
    else:
        pass
