from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MPP_Instructions(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment_displayed"] == False:
            return True

    def js_vars(self):
        return dict(
            location=self.participant.vars["location"],
            treatment_displayed=str(self.subsession.this_app_constants()["treatment_displayed"]),
            page="historic",
            treatment=self.participant.vars["treatment"],
        )

class MPP_Decision(Page):
    form_model = "player"
    form_fields = ["Q1",
                   "Q2",
                   "Q3"]

    def before_next_page(self):
        self.player.set_payoff()

    def js_vars(self):
        return dict(
            location=self.participant.vars["location"],
            treatment_displayed=str(self.subsession.this_app_constants()["treatment_displayed"]),
            page="decision",
            treatment=self.participant.vars["treatment"],
        )


class MPP_Revelation(Page):

    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment_displayed"] == True:
            return True

    def js_vars(self):
        return dict(
            page = "revelation",
            location=self.participant.vars["location"],
        )

page_sequence = [MPP_Instructions, MPP_Decision, MPP_Revelation]
