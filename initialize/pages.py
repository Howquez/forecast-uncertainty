from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro_Welcome(Page):
    pass

class Intro_Instructions(Page):
    def js_vars(self):
        return dict(
            page="historic",
            treatment=self.participant.vars["treatment"],
            location=self.participant.vars["location"],
            small=True,
        )


page_sequence = [Intro_Welcome, Intro_Instructions]
