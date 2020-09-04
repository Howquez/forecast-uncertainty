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

    form_fields=["temp1", "temp2", "temp3", "temp4", "temp5", "temp6", "temp7", "temp8", "temp9", "temp10",\
        "temp11", "temp12", "temp13", "temp14", "temp15", "temp16", "temp17", "temp18", "temp19", "temp20",\
        "temp21", "temp22", "temp23", "temp24", "temp25", "temp26", "temp27", "temp28", "temp29", "temp30",\
        "temp31", "temp32", "temp33", "temp34", "temp35", "temp36", "temp37", "temp38", "temp39", "temp40",\
        "temp41", "temp42", "temp43", "temp44", "temp45", "temp46", "temp47", "temp48", "temp49", "temp50", "temp51"]

    def get_form_fields(self):
        return self.form_fields[self.player.minTemp + 10 : self.player.maxTemp + 11]
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [# Instructions,
                 BSR_PreSelection,
                 BSR,
                 ResultsWaitPage,
                 Results]
