import click

from core.number_guessing_game import NumberGuessingGame
from core.view import NumberGuessingGameView


@click.command()
@click.option('--min-value', default=1)
@click.option('--max-value', default=10)
@click.option('--max-guesses', default=10)
@click.option('--close-threshold', default=.1)
def main(
    min_value, max_value, max_guesses, close_threshold
):
    game = number_guessing_game(min_value, max_value, max_guesses, threshold=close_threshold)
    print('Answer for debugging:', game.answer)
    game()

def number_guessing_game(min_val: int, max_val: int, max_guesses: int, threshold: float):
    _instance = NumberGuessingGame(min_val, max_val, max_guesses)
    _view = NumberGuessingGameView(_instance, threshold)
    def _game():
        prompt = 'Guess a number'
        while _instance.is_still_active:
            value = get_within_range(prompt, min_val, max_val)
            output = _view.calculate_turn(value)
            print(output)
    _game.answer = _instance.answer
    return _game


def get_within_range(prompt: str, min_val: int, max_val: int) -> int:
    formatted  = f'{prompt}({min_val}-{max_val}): '
    value = _try_get_int(formatted)
    while value is None or value < min_val or value > max_val:
        value = _try_get_int(formatted)
    return value


def _try_get_int(prompt):
    value = input(prompt)
    
    try:
        return int(value)
    except ValueError:
        return None

if __name__ == '__main__':
    main()
