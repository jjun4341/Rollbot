import asyncio
from abc import abstractmethod

from Core.helper_functions import message_without_command
from Core.core_game_class import GameCore
from HammerRace.participant import Participant
from HammerRace.race_track import RaceTrack


class HammerRace(GameCore):

    def __init__(self, bot, ctx):
        super().__init__(bot, ctx)
        self.distance_to_finish = 40
        self.winners = []
        self.race_track = RaceTrack(self)
        self.message = message_without_command(ctx.message.content)
        self.join_timer = None

    async def run(self) -> None:
        self.start_game()
        await self.bot.say(self.round_report())

        while self.in_progress:
            await asyncio.sleep(2.0)
            self._next_round()
            await self.bot.say(self.round_report())

        await self.bot.say(self._get_outcome_report())

    def valid_num_players(self) -> bool:
        within_min_players = len(self.players) > 1
        within_max_players = len(self.players) <= 5
        return within_min_players and within_max_players

    def round_report(self) -> str:
        return self.race_track.draw_track()

    @abstractmethod
    def _get_outcome_report(self) -> str:
        raise NotImplementedError

    def _next_round(self) -> None:
        [self._player_turn(player) for player in self.players]
        self._check_race_end()

    def _is_winner(self, player: Participant) -> bool:
        return self._get_steps_left(player.progress) <= 0

    def _init_player(self, short_name: str, name: str):
        player = Participant(short_name, name)
        self.players.append(player)
        return player

    def _player_turn(self, participant: Participant) -> None:
        participant.make_move()
        if self._is_winner(participant):
            self._add_winner(participant)

    def _check_race_end(self) -> None:
        if self.is_race_end():
            self.end_game()

    def _get_steps_left(self, progress: int) -> int:
        character_space = 1
        return self.distance_to_finish - progress - character_space

    def _add_winner(self, participant: Participant) -> None:
        self.winners.append(participant)

    def is_race_end(self) -> bool:
        return len(self.winners) > 0

    def _has_multiple_winners(self) -> bool:
        return len(self.winners) > 1

    def _get_player_names(self) -> str:
        return ', '.join(player.name for player in self.players)

    def _get_winner_names(self) -> str:
        return ', '.join(winner.name for winner in self.winners)
