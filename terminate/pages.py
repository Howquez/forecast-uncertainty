from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import re


class Demographic_Questions(Page):
    form_model = "player"
    form_fields = ["Age", "Gender", "Education", "Income"]

class Domain_Questions_1(Page):
    form_model = "player"
    form_fields = ["Accuracy", "Authenticity", "Credibility"]

    def js_vars(self):
        return dict(
            location=self.participant.vars["location"],
            treatment=self.participant.vars["treatment"],
        )

class Domain_Questions_2(Page):
    form_model = "player"
    form_fields = ["Comprehension", "Usage"]

class CLICCS_Questions(Page):
    form_model = "player"
    form_fields = ["CLICCS1", "CLICCS2"]

class Results(Page):

    def js_vars(self):
        event=""
        ticks=[]
        if bool(re.search("Baillon", self.participant.vars["winning_app"])):
            event=self.participant.vars["payment_event"]
            ticks=self.participant.vars["baillon_ticks"]
        return dict(
            page = "revelation",
            location=self.participant.vars["location"],

            ticks=ticks,
            event_decision=event,
            enabledLabel = True,
            results=True,
        )


    def vars_for_template(self):
        if bool(re.search("MPP", self.participant.vars["winning_app"])):
            print(self.participant.vars["MPP_guess"])
            return {
                "task": self.participant.vars["payment_task"],
                "winning_app": "MPP",
                "guess1": self.participant.vars["MPP_guess"][0],
                "guess2": self.participant.vars["MPP_guess"][1],
                "guess3": self.participant.vars["MPP_guess"][2],
                "diff1": self.participant.vars["MPP_diffs"][0],
                "diff2": self.participant.vars["MPP_diffs"][1],
                "diff3": self.participant.vars["MPP_diffs"][2],
                "loss1": round(self.participant.vars["MPP_loss"][0], 1),
                "loss2": round(self.participant.vars["MPP_loss"][1], 1),
                "loss3": round(self.participant.vars["MPP_loss"][2], 1),
                "chance": self.participant.vars["Chance"],
            }
        elif bool(re.search("Baillon", self.participant.vars["winning_app"])):
            return {
                "task": self.participant.vars["payment_task"],
                "winning_app": "Baillon",
                "round": self.participant.vars["baillon_round_to_pay"],
                "pivotal_equivalent": self.participant.vars["pivotal_equivalent"],
                "chance": self.participant.vars["pivotal_lottery"],
                "payment_mechanism": self.participant.vars["payment_mechanism"],
            }


page_sequence = [Domain_Questions_1,
                 Domain_Questions_2,
                 CLICCS_Questions,
                 Demographic_Questions,
                 Demographic_Questions,
                 Results]
