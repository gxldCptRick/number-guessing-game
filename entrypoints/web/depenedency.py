from functools import cache

from entrypoints.web.game_manager import GameManager


@cache
def get_manager() -> GameManager:
    return GameManager()