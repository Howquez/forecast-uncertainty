from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import re


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
            event_decision=event,
            ticks=ticks,
            enabledLabel = True,
            results=True,
        )


    def vars_for_template(self):
        if bool(re.search("MPP", self.participant.vars["winning_app"])):
            print(self.participant.vars["MPP_guess"])
            return {
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
                "winning_app": "Baillon",
                "round": self.participant.vars["baillon_round_to_pay"],
                "row": self.participant.vars["baillon_choice_to_pay"],
                "chance": self.participant.vars["lottery_chance"],
                "lottery": self.participant.vars["option_chosen"],
            }


page_sequence = [Results]
