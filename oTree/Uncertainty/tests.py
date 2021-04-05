from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission
import random


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(pages.Baillon_Decision,
                         dict(review_weather=random.randint(0, 5),
                              review_instructions=random.randint(0, 5),
                              matching_probability=random.randint(0, 100)),
                         check_html=False)