from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass

class BSR_PreSelection(Page):
    form_model="player"
    form_fields=["minTemp",
                 "maxTemp"]

class BSR(Page):
    form_model="player"

    # def temp_range(self):
    #     if self.player.minTemp < 0:
    #         return
    # def get_form_fields(self):
    #     return ["temp{}".format(i) for i in range(self.player.minTemp, self.player.maxTemp+1)]

    form_fields=["prob0", "prob1", "prob2", "prob3", "prob4", "prob5", "prob6", "prob7", "prob8", "prob9", "prob10",\
        "prob11", "prob12", "prob13", "prob14", "prob15", "prob16", "prob17", "prob18", "prob19", "prob20",\
        "prob21", "prob22", "prob23", "prob24", "prob25", "prob26", "prob27", "prob28", "prob29", "prob30",\
        "prob31", "prob32", "prob33", "prob34", "prob35", "prob36", "prob37", "prob38", "prob39", "prob40",\
        "prob41", "prob42", "prob43", "prob44", "prob45", "prob46", "prob47", "prob48", "prob49", "prob50"]

    def get_form_fields(self):
        return self.form_fields[self.player.minTemp : self.player.maxTemp + 1]

    def before_next_page(self):
        self.player.set_loss()
        self.player.set_payoff()
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):

    pass


page_sequence = [# Instructions,
                 BSR_PreSelection,
                 BSR,
                 # ResultsWaitPage,
                 Results]
