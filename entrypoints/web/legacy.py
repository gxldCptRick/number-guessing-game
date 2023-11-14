import uuid
from fastapi import APIRouter, Depends, HTTPException
from core.number_guessing_game import GameOverException
from core.view import NumberGuessingGameView
from entrypoints.web.depenedency import get_manager
from entrypoints.web.game_manager import GameManager

from entrypoints.web.models import GameStartRequest, NumberGuessingGameGuess

router = APIRouter()

@router.post('/game')
def start_game(params: GameStartRequest, manager: GameManager = Depends(get_manager)):
    
    _id = manager.start_game(params, with_view=True)
    return {
        'id': _id
    }


@router.post('/game/{game_id}')
def submit_guess(game_id: uuid.UUID, guess: NumberGuessingGameGuess, manager: GameManager = Depends(get_manager)):
    game = manager.get_game_session_by_id(game_id)
    
    if not isinstance(game, NumberGuessingGameView):
        game = NumberGuessingGameView(game, 0.1)
    
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
def get_game_status(game_id: uuid.UUID, manager: GameManager = Depends(get_manager)):
    game = manager.get_game_session_by_id(game_id)
    if not isinstance(game, NumberGuessingGameView):
        game = NumberGuessingGameView(game, 0.1)
    is_won = game.game.game_won
    remaining_turns = game.game.remaining_turns
    
    return {
        'is_won': is_won,
        'remaining_turns': remaining_turns
    }
