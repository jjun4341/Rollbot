import discord, random, asyncio
from RollGames.roll import Roll
from Managers.data_manager import SessionDataManager


class RollGame:
    def __init__(self, bot, data_manager: SessionDataManager, ctx, bet):
        self.bot = bot
        self.data_manager = data_manager
        self.bet = bet
        self.ctx = ctx
        self.users = []
        self.in_progress = False
        self.result = []

    @staticmethod
    async def forced_roll(player: discord.member.Member, max: int):
        """Automatically rolls for a player"""
        roll = random.randint(1, max)
        the_roll = Roll(roll, player, max)
        return the_roll

    @staticmethod
    def get_name(author):
        return author.display_name

    async def add_user(self, player: discord.member.Member):
        self.users.append(player)

    async def wait_for_rolls(self):
        raise NotImplementedError

    async def determine(self):
        raise NotImplementedError

    def play_message(self):
        raise NotImplementedError

    async def add_roll(self, roll):
        raise NotImplementedError
