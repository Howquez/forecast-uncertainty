from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro_Instructions(Page):
    pass

class Intro_Welcome(Page):
    pass


page_sequence = [Intro_Welcome]
