from pydantic import BaseModel


class GameStartRequest(BaseModel):
    min_value: int = 1
    max_value: int = 10
    max_guesses: int = 10
    range_threshold: float = 0.1


class NumberGuessingGameGuess(BaseModel):
    guess: int
