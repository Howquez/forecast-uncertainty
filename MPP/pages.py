from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import re


class MPP_Instructions(Page):
    def is_displayed(self):
        if not self.subsession.this_app_constants()["treatment_displayed"]:
            return True

class MPP_Decision(Page):
    form_model = "player"
    form_fields = ["Q1",
                   "Q2",
                   "Q3"]

    def before_next_page(self):
        self.player.prepare_payoffs()
        self.player.set_payoffs()

    def js_vars(self):
        return dict(
            location=self.participant.vars["location"],
            treatment_displayed=str(self.subsession.this_app_constants()["treatment_displayed"]),
            page="decision",
            treatment=self.participant.vars["treatment"],
            small=True,
        )

    def vars_for_template(self):
        return {
            "treatment_displayed" : str(self.subsession.this_app_constants()["treatment_displayed"]),
        }


class MPP_Revelation(Page):

    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment_displayed"]:
            return True

    def js_vars(self):
        return dict(
            page = "revelation",
            location=self.participant.vars["location"],
        )

    def vars_for_template(self):
        return {
            "treatment_displayed": str(self.subsession.this_app_constants()["treatment_displayed"]),
        }


page_sequence = [MPP_Instructions, MPP_Decision]
