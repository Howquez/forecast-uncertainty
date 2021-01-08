from otree.api import Currency as c, currency_range
from MPP import pages
from ._builtin import Bot
from .models import Constants
import random



class PlayerBot(Bot):
    def play_round(self):
        temp = random.randint(8, 16)
        yield pages.MPP_Decision, dict(window_width=16, window_height=9, browser="Chrome Test",
                                       review_weather=random.randint(1, 2),
                                       review_instructions=0,
                                       lower_bound=temp - random.randint(1, 3),
                                       best_guess=temp,
                                       upper_bound=temp + random.randint(1, 3))
        yield pages.MPP_Direct
