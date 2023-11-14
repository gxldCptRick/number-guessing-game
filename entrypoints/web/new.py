from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from core.number_guessing_game import GameOverException, NumberGuessingGame
from entrypoints.web.depenedency import get_manager

from entrypoints.web.game_manager import GameManager
from entrypoints.web.models import GameStartRequest, NumberGuessingGameGuess


router = APIRouter()


@router.get('/game/{game_id}')
def get_game_status(game_id: UUID, manager: GameManager = Depends(get_manager)):
    game = manager.get_game_session_by_id(game_id)
    if not isinstance(game, NumberGuessingGame):
        game = game.game
    
    return {
        "isWon": game.game_won,
        "turnsRemaining": game.remaining_turns,
        "previousGuesses": [
            {
                'guess': guess.guess,
                'difference': guess.difference,
            } for guess in game.previous_guesses
        ]
    }


@router.post('/game/{game_id}')
def guess_a_number(game_id: UUID, guess: NumberGuessingGameGuess,  manager: GameManager = Depends(get_manager)):
    game = manager.get_game_session_by_id(game_id)
    if not isinstance(game, NumberGuessingGame):
        game = game.game
    min_val, max_val  = game._min_value, game._max_value
    value = guess.guess
    
    if value < min_val or value > max_val:
        raise HTTPException(400, detail=f'Number must be in range: ({min_val}-{max_val})')
    
    try:
        result = game(guess.guess)
        return {
            'guess': result.guess,
            'difference': result.difference,
            'turnsRemaining': result.remaining_guesses
        }
    except GameOverException:
        raise HTTPException(400, detail='Cannot play game that is already over.')


@router.post('/game')
def start_game(request: GameStartRequest,  manager: GameManager = Depends(get_manager)):
    return {
        'id': manager.start_game(request, with_view=False)
    }
