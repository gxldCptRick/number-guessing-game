import uuid

from fastapi import HTTPException
from core.number_guessing_game import NumberGuessingGame

from core.view import NumberGuessingGameView
from entrypoints.web.models import GameStartRequest


class GameManager:
    def __init__(self) -> None:
        self.active_games: dict[uuid.UUID, NumberGuessingGameView | NumberGuessingGame] = {}

    def start_game(self, request: GameStartRequest, with_view: bool = True):
        if with_view:
            game = NumberGuessingGameView(
                NumberGuessingGame(
                    request.min_value,
                    request.max_value,
                    request.max_guesses
                ),
                request.range_threshold
            )
        else:
            game = NumberGuessingGame(
                request.min_value,
                request.max_value,
                request.max_guesses
            )
        id = uuid.uuid4()
        self.active_games[id] = game
        return id

    def get_game_session_by_id(self, id: uuid.UUID) -> NumberGuessingGameView | NumberGuessingGame:
        if id not in self.active_games:
            raise HTTPException(404, 'Game not found')
        return self.active_games[id]

    def remove_session(self, id: uuid.UUID) -> bool:
        return self.active_games.pop(id, None) is not None