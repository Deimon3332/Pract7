import random
import game_data

def get_limits():
    return game_data.lower_limit, game_data.upper_limit

def initialize_game(lower_limit, upper_limit):
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    return secret_number, attempts
