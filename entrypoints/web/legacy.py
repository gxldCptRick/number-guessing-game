import uuid
from fastapi import APIRouter, HTTPException
from core.number_guessing_game import GameOverException, NumberGuessingGame
from core.view import NumberGuessingGameView

from entrypoints.web.models import GameStartRequest, NumberGuessingGameGuess

router = APIRouter()
_instances: dict[uuid.UUID, NumberGuessingGameView] = {}


@router.post('/game')
def start_game(params: GameStartRequest):
    id = uuid.uuid4()
    game_instance = NumberGuessingGame(
        params.min_value,
        params.max_value,
        params.max_guesses
    )
    
    _instances[id] = NumberGuessingGameView(
        game_instance,
        params.range_threshold
    )
    
    return {
        'id': id
    }


@router.post('/game/{game_id}')
def submit_guess(game_id: uuid.UUID, guess: NumberGuessingGameGuess):
    
    if game_id not in _instances:
        raise HTTPException(404, detail='Game not Found')
    game = _instances.get(game_id)
    min_val, max_val  = game.game._min_value, game.game._max_value
    value = guess.guess
    
    if value < min_val or value > max_val:
        raise HTTPException(400, detail=f'Number must be in range: ({min_val}-{max_val})')
    try:
        result = game.calculate_turn(value)
    except GameOverException:
        raise HTTPException(400, detail='Cannot continue a game that is finished')

    return {'message': result}


@router.get('/game/{game_id}')
def get_game_status(game_id: uuid.UUID):
    if game_id not in _instances:
        raise HTTPException(404, 'Game not found')
    
    game = _instances.get(game_id)
    
    is_won = game.game.game_won
    remaining_turns = game.game.remaining_turns
    
    return {
        'is_won': is_won,
        'remaining_turns': remaining_turns
    }
