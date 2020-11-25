from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import re


class Results(Page):

    def js_vars(self):
        return dict(
            page = "revelation",
            location=self.participant.vars["location"],
        )


    def vars_for_template(self):
        if bool(re.search("MPP", self.participant.vars["winning_app"])):
            return {
                "winning_app": "MPP",
                "round2": bool(re.search("post", self.participant.vars["winning_app"])),
                "diff1": self.participant.vars["MPP_diffs"][0],
                "diff2": self.participant.vars["MPP_diffs"][1],
                "diff3": self.participant.vars["MPP_diffs"][2],
                "guess1": self.participant.vars["MPP_guess"][0],
                "guess2": self.participant.vars["MPP_guess"][1],
                "guess3": self.participant.vars["MPP_guess"][2],
                "chance": self.participant.vars["Chance"],
            }
        elif bool(re.search("Baillon", self.participant.vars["winning_app"])):
            return {
                "winning_app": "Baillon",
                "round2": bool(re.search("post", self.participant.vars["winning_app"])),
                "round": self.participant.vars["baillon_round_to_pay"],
                "row": self.participant.vars["baillon_choice_to_pay"],
                "chance": self.participant.vars["Chance"],
                "lottery": self.participant.vars["option_chosen"],
            }


page_sequence = [Results]
