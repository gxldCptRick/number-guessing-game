from random import randint

import click


@click.command()
@click.option('--min-value', default=1)
@click.option('--max-value', default=10)
@click.option('--max-guesses', default=10)
def main(
    min_value, max_value, max_guesses
):
    game = number_guessing_game(min_value, max_value, max_guesses)
    print('Answer for debugging:', game.answer)
    game()

def number_guessing_game(min_val: int, max_val: int, max_guesses: int):
    number_to_guess = randint(min_val, max_val)
    
    def _game():
        prompt = 'Guess a number'
        remaining_guesses = max_guesses
        while remaining_guesses:
            value = get_within_range(prompt, min_val, max_val)
            
            if value == number_to_guess:
                print('fuck me i didn\'t think you would get it lol')
                break
            else:
                remaining_guesses -= 1
                if value < number_to_guess:
                    print('Little to low bud')
                else:
                    print('Too high bud')
                print(f'{remaining_guesses} total guesses remaining')
    _game.answer = number_to_guess
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
