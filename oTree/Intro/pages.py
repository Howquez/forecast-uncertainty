from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro_Welcome(Page):
    form_model = "player"
    form_fields = ["window_width", "window_height", "browser"]

class Intro_Instructions(Page):
    form_model = "player"
    form_fields = ["CQ_1", "CQ_2"]

    def js_vars(self):
        return dict(
            template="instructions",
            event_decision="E2",
            ticks=[0, 8, 14, 22],
            treatment=self.participant.vars["treatment"],
            location=self.participant.vars["location"],

        )

page_sequence = [Intro_Welcome, Intro_Instructions]