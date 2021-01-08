from otree.api import Currency as c, currency_range
from Baillon import pages
from ._builtin import Bot
from .models import Constants
import random



class PlayerBot(Bot):
    def play_round(self):
        yield pages.Baillon_Decision, dict(window_width=16, window_height=9, browser="Chrome Test",
                                           review_weather=random.randint(1, 2),
                                           review_instructions=0,
                                           baillon_equivalent=random.randint(1, 100))
        if self.round_number == Constants.num_rounds:
            yield pages.Baillon_Direct
