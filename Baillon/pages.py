# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Baillon_Instructions(Page):

    form_model = "player"
    form_fields = [#"BaillonQ1",
                   #"BaillonQ2",
                   #"BaillonQ3",
                   #"BaillonQ4",
                   #"BaillonQ5"
                    ]

    def is_displayed(self):
            # print(self.subsession.this_app_constants()["treatment_displayed"])
        if self.subsession.this_app_constants()["treatment_displayed"] == False and self.round_number == 1:
            return True

    def js_vars(self):
        return dict(
            ticks=Constants.ticks,
            event_decision="E3",
            compound=False,
            treatment=self.participant.vars["treatment"],
            enabledLabel=True,
            location=self.participant.vars["location"],
        )

    # def error_message(self, values):
    #     solutions = dict(
    #         BaillonQ1=False,
    #         BaillonQ2=True,
    #         BaillonQ4=True,
    #         BaillonQ5=True,
    #     )
    #
    #     error_messages = dict(
    #         BaillonQ1="Sie müssen die Situation verstanden haben.",
    #         BaillonQ2="Sie müssen die Situation verstanden haben.",
    #         BaillonQ4="Sie müssen die Situation verstanden haben.",
    #         BaillonQ5="Sie müssen die Situation verstanden haben.",
    #     )
    #
    #     for field_name in solutions:
    #         if values[field_name] != solutions[field_name]:
    #             return error_messages[field_name]  # = 'Wrong answer' # wenn error message dict leer
    #             # return error_messages



class Baillon_Confirmation(Page):
    def is_displayed(self):
        if not self.subsession.this_app_constants()["treatment_displayed"] and self.round_number == 1:
            return True


class Forecast_Viz(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment_displayed"] == True and self.round_number == 1: # as defined in post_baillon/models
            return True

    def js_vars(self):
        return dict(
            opacity = 0.2,
        )



class Baillon_Decision(Page):
    form_model = "player"
    form_fields = ["review_weather", "review_instructions", "window_width", "window_height", "browser",
                   "baillon_equivalent"]

    def js_vars(self):
        if len(self.player.event_decision) == 3:  # compound decision
            compound = True
        else:
            compound = False
        return dict(
            ticks=Constants.ticks,
            event_decision=self.player.event_decision,
            compound=compound,
            treatment=self.participant.vars["treatment"],
            enabledLabel=True,
            # the following three vars are needed such that the weather viz can be displayed on decision screen as well
            treatment_displayed=str(self.subsession.this_app_constants()["treatment_displayed"]),
            page="decision",
            location=self.participant.vars["location"],
            small=True,
        )

    def vars_for_template(self):
        return {
            "treatment_displayed": str(self.subsession.this_app_constants()["treatment_displayed"]),
        }

    def before_next_page(self):
        self.player.prepare_payoffs()
        self.player.set_payoffs()
    pass



class Baillon_Direct(Page):

    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True

    def vars_for_template(self):
        return {
            "treatment_displayed": str(self.subsession.this_app_constants()["treatment_displayed"]),
        }


page_sequence = [Baillon_Instructions,
                 Baillon_Confirmation,
                 Baillon_Decision,
                 Baillon_Direct
                 ]
