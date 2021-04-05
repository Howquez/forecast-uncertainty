from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Outro_Belief, dict(Belief=random.randint(0, 35))

        yield pages.Outro_Risk, dict(Risk_General=random.randint(0, 10),
                                     Risk_Weather=random.randint(0, 10))

        yield pages.Domain_Questions_1, dict(Accuracy=random.randint(0, 4),
                                             Credibility=random.randint(0, 4))

        yield pages.Domain_Questions_2, dict(Comprehension="yes",
                                             Usage=random.randint(0, 5),
                                             Temp=random.randint(0, 35))

        yield pages.Demographic_Questions, dict(Age=random.randint(0, 65),
                                                Gender="not specified",
                                                Family="widowed",
                                                Kids=random.randint(0,4),
                                                Education=random.randint(0,8),
                                                Income=random.randint(0,5),
                                                ZIP=20149)
        yield pages.CLICCS_Questions, dict(CLICCS1="lorem ipsum 1",
                                           CLICCS2="lorem ipsum 2")
        yield pages.Results, dict(openText="hello world!")
