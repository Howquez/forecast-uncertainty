from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission
import random


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Intro_Welcome
        yield Submission(pages.Intro_Instructions,
                         dict(window_width=1, window_height=1, browser="Chrome Canary",
                              CQ_1=True,
                              CQ_2=True,
                              wrong_answer_1=random.randint(0, 5),
                              wrong_answer_2=random.randint(0, 5)),
                         check_html=False)

