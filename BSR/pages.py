from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment"] == "pre":
            return True

    form_model="player"
    form_fields=["CQ1",
                 "CQ2"]

    def error_message(self, values):
        solutions = dict(
            CQ1="Yes",
            CQ2=int(8)
        )

        error_messages = dict(
            CQ1="Sie müssen die Situation verstanden haben.",
            CQ2="Falsch, probieren Sie es erneut."
        )

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] # = 'Wrong answer' # wenn error message dict leer
                return error_messages

class BSR_PreSelection(Page):
    form_model="player"
    form_fields=["minTemp",
                 "maxTemp"]

class BSR(Page):
    form_model="player"

    form_fields = ["prob" + str(k) for k in Constants.temps]

    def get_form_fields(self):
        return self.form_fields[
               self.player.minTemp - Constants.TEMP_RANGE[0]:
               self.player.maxTemp - Constants.TEMP_RANGE[0] + 1
               ]

    def js_vars(self):
        return dict(
            minTemp = self.player.minTemp,
            maxTemp = self.player.maxTemp,
            weight  = Constants.weight
        )


    def before_next_page(self):
        self.player.set_loss()
        # self.player.calc_each_loss()
        self.player.set_payoff()


class ControlQuestions(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment"] == "post":
            return True

    form_model = "player"
    form_fields = ["commonQuestion1",
                   "commonQuestion2"]


class Results(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment"] == "post":
            return True


page_sequence = [Instructions,
                 BSR_PreSelection,
                 BSR,
                 ControlQuestions,
                 Results
                 ]
