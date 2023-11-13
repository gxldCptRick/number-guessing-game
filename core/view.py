from core.number_guessing_game import NumberGuessingGame


class NumberGuessingGameView:
    def __init__(self, game: NumberGuessingGame, threshold_for_closeness: float) -> None:
        self.game = game
        self.max_distance = round((game._max_value - game._min_value) * threshold_for_closeness)
        
    
    def calculate_turn(self, guess: int) -> str:
        output = []
        
        result = self.game(guess)
        difference = result.difference
        
        if not difference:
            output.append('fuck me i didn\'t think you would get it lol')
            output.append(f'Finished with {result.remaining_guesses} turns remaining')
            return '\n'.join(output)
        
        is_big_difference = abs(difference) > self.max_distance
        if is_big_difference:
            if difference < 0:
                output.append('Way too low bud')
            elif difference > 0:
                output.append('Fuck no that is way too high')
        else:
            if difference < 0:
                output.append('Little to low bud')
            elif difference > 0:
                output.append('Too high bud')
        output.append(f'{result.remaining_guesses} total guesses remaining')
        
        return '\n'.join(output)