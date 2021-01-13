from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random



class PlayerBot(Bot):
    def play_round(self):
        if self.subsession.this_app_constants()["treatment_displayed"] == False and self.round_number == 1:
            yield pages.Baillon_Instructions
            yield pages.Baillon_Confirmation
        yield pages.Baillon_Decision, dict(window_width=16, window_height=9, browser="Chrome Test",
                                           review_weather=random.randint(1, 2),
                                           review_instructions=random.randint(1, 4),
                                           matching_probability=random.randint(1, 100))
        if self.round_number == Constants.num_rounds:
            yield pages.Baillon_Direct
