from Slots.symbols import *
from Slots.slot_machine import SlotMachine
import random


class BigSlots(SlotMachine):
    def __init__(self):
        super().__init__()
        self.num_columns = 5
        self.payout_multiplier = 2
        self.reel_size = self.num_columns * 2

    def get_bias_options(self):
        first_row = 0
        last_row = self.num_columns - 1
        random_index = random.randint(first_row, last_row)
        return [random_index, random_index, first_row, last_row]


class GiantSlots(BigSlots):
    def __init__(self):
        super().__init__()
        self.num_columns = 7
        self.payout_multiplier = 5


class ClassicSlots(SlotMachine):
    def __init__(self):
        super().__init__()
        self.default_outcomes = [cherry, cherry,
                                 strawberry, strawberry,
                                 pear, pear,
                                 pineapple,
                                 grapes,
                                 butt,
                                 meat,
                                 bar, bar,
                                 hammer,
                                 cake,
                                 seven]

    @staticmethod
    def get_win_message(matches, winning_stats, payout) -> str:
        linebreak = '\n'
        return linebreak.join([f'Rolled {matches}!',
                               f'{winning_stats}',
                               f':dollar: Payout is {payout} gold. :dollar:'])


class BigClassicSlots(BigSlots, ClassicSlots):
    def __init__(self):
        super().__init__()


class GiantClassicSlots(GiantSlots, ClassicSlots):
    def __init__(self):
        super().__init__()


class MapleSlots(SlotMachine):
    def __init__(self):
        super().__init__()
        self.default_outcomes = [bubbling, bubbling,
                                 warbow, warbow,
                                 mushroom, mushroom,
                                 slime, slime,
                                 kumbi, kumbi,
                                 pinky,
                                 octopus,
                                 pepe,
                                 mesocoin,
                                 steely,
                                 mesobag,
                                 panlid]

    @staticmethod
    def get_win_message(matches, winning_stats, payout) -> str:
        linebreak = '\n'
        mesowad = '<:mesowad:246852286993793025>'
        return linebreak.join([f'Rolled {matches}!',
                               f'{winning_stats}',
                               f'{mesowad} Payout is {payout} mesos. {mesowad}'])


class BigMapleSlots(BigSlots, MapleSlots):
    def __init__(self):
        super().__init__()


class GiantMapleSlots(GiantSlots, MapleSlots):
    def __init__(self):
        super().__init__()