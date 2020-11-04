from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MPP_Instructions(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True

class MPP_Decision(Page):
    form_model = "player"
    form_fields = ["Q1",
                   "Q2",
                   "Q3"]

    def before_next_page(self):
        self.player.set_payoff()

    def js_vars(self):

        treatment_displayed = False
        page = "historic"

        if self.round_number == 2:
            treatment_displayed = True
            page = "forecast"

        return dict(
            location=self.participant.vars["location"],
            treatment_displayed=treatment_displayed,
            page=page,
            treatment=self.participant.vars["treatment"],
        )


class MPP_Revelation(Page):

    def is_displayed(self):
        if self.round_number == 2:
            return True

    def js_vars(self):
        return dict(
            page = "revelation",
            location=self.participant.vars["location"],
        )

page_sequence = [MPP_Instructions, MPP_Decision, MPP_Revelation]
