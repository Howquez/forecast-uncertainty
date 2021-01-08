from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random



class PlayerBot(Bot):
    def play_round(self):
        yield pages.Domain_Questions_1, dict(Accuracy=random.randint(-2, 2),
                                             Authenticity=random.randint(-2, 2),
                                             Credibility=random.randint(-2, 2))
        yield pages.Domain_Questions_2, dict(Comprehension="yes", Usage=random.randint(0, 5))
        yield pages.CLICCS_Questions, dict(CLICCS1="test1", CLICCS2="test2")
        yield pages.Demographic_Questions, dict(Age=random.randint(18, 100), Gender="diverse", Education="uni",
                                                Income=random.randint(30000, 70000))
