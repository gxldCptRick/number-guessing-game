import random
from typing import Callable

from pydantic import BaseModel


class GameOverException(Exception):
    def __init__(self,) -> None:
        super().__init__('Game is already over cannot do any moves.')


class GuessResult(BaseModel):
    guess: int
    difference: int
    remaining_guesses: int


class NumberGuessingGame:
    def __init__(
        self, 
        min_value: int, 
        max_value: int, 
        max_guesses: int, 
        calculate_answer: Callable[[int, int], int] = random.randint
    ) -> None:
        self._min_value = min_value
        self._max_value = max_value
        self._calculate_answer = calculate_answer
        self._max_guesses = max_guesses
        # Game Fields that are used
        self.previous_guesses: list[GuessResult] = []
        self.answer = 0
        self.game_won = True
        self.remaining_turns = 0
        self.reset_game() # this to create the fields we will be using for the rest of the game
        

    def reset_game(self):
        self.previous_guesses = []
        self.answer = self._calculate_answer(self._min_value, self._max_value)
        self.remaining_turns = self._max_guesses
        self.game_won = False

    def __call__(self, guess: int) -> GuessResult:
        if not self.is_still_active:
            raise GameOverException()
        
        self.remaining_turns -= 1
        result = GuessResult(guess=guess, difference=guess - self.answer, remaining_guesses=self.remaining_turns)

        if result.difference == 0:
            self.game_won = True

        self.previous_guesses.append(result)
        return result

    @property
    def is_still_active(self):
        return not self.game_won and self.remaining_turns > 0
