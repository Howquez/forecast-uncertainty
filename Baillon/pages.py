from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Historic_Viz(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment"] == "pre" and self.round_number == 1:
            return True

class Forecast_Viz(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment"] == "post" and self.round_number == 1:
            return True

class Instructions(Page):
    def is_displayed(self):
        print(self.subsession.this_app_constants())
        if self.subsession.this_app_constants()["treatment"] == "pre" and self.round_number == 1:
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


class Baillon_Decision(Page):
    form_model = "player"

    # form fields
    def get_form_fields(self):
        form_fields = [list(t) for t in zip(*self.participant.vars["baillon_choices"])][1]
        return form_fields

    def js_vars(self):
        return dict(
            ticks = Constants.ticks,
            event_decision = self.player.event_decision,
            treatment = self.participant.vars["treatment"],
        )

    def vars_for_template(self):
        return {
            "choices" : self.player.participant.vars["baillon_choices"],
            "num_choices" : Constants.num_choices
        }

    # set player's payoff
    def before_next_page(self):
        # unzip indices and form fields from <mpl_choices> list
        round_number = self.subsession.round_number
        form_fields = [list(t) for t in zip(*self.participant.vars['baillon_choices'])][1]
        indices = [list(t) for t in zip(*self.participant.vars['baillon_choices'])][0]
        # index = indices[round_number - 1]

        for j, choice in zip(indices, form_fields):
            choice_i = getattr(self.player, choice)
            self.participant.vars["baillon_choices_made"][j - 1] =choice_i

        self.player.set_payoffs()
        self.player.set_consistency()
        self.player.set_switching_row()


class Results(Page):
    pass


page_sequence = [Historic_Viz,
                 Forecast_Viz,
                 Instructions,
                 Baillon_Decision]
