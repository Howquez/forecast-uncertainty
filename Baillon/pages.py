from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Baillon_Instructions(Page):
    def is_displayed(self):
            # print(self.subsession.this_app_constants()["treatment_displayed"])
        if self.subsession.this_app_constants()["treatment_displayed"] == False and self.round_number == 1:
            return True

    def js_vars(self):
        return dict(
            ticks=[0, 14, 20, 34],
            event_decision="E3",
            treatment=self.participant.vars["treatment"],
            enabledLabel=False,
        )

    def vars_for_template(self):
        choices = self.player.participant.vars["baillon_compound_choices"]
        indices = [0, 1, 3, 7, 11, 19]
        return {
            "choices":[choices[i] for i in indices],
            "num_choices": 6
        }


class Baillon_Decision(Page):
    form_model = "player"

    # form fields
    def get_form_fields(self):
        if len(self.player.event_decision) == 3: #compound decision
            form_fields = [list(t) for t in zip(*self.participant.vars["baillon_compound_choices"])][1]
        else:
            form_fields = [list(t) for t in zip(*self.participant.vars["baillon_single_choices"])][1]
        return form_fields

    def js_vars(self):
        return dict(
            ticks = Constants.ticks,
            event_decision = self.player.event_decision,
            treatment = self.participant.vars["treatment"],
            enabledLabel=True,
            # the following three vars are needed such that the weather viz can be displayed on decision screen as well
            treatment_displayed = str(self.subsession.this_app_constants()["treatment_displayed"]),
            page="decision",
            location=self.participant.vars["location"],
            small=True,

        )

    def vars_for_template(self):
        if len(self.player.event_decision) == 3: #compound decision
            choices = self.player.participant.vars["baillon_compound_choices"]
        else:
            choices = self.player.participant.vars["baillon_single_choices"]
        return {
            "choices" : choices,
            "num_choices" : Constants.num_choices
        }

    # set player's payoff
    def before_next_page(self):
        if len(self.player.event_decision) == 3: #compound decision
            form_fields = [list(t) for t in zip(*self.participant.vars["baillon_compound_choices"])][1]
            indices = [list(t) for t in zip(*self.participant.vars["baillon_compound_choices"])][0]
        else:
            form_fields = [list(t) for t in zip(*self.participant.vars["baillon_single_choices"])][1]
            indices = [list(t) for t in zip(*self.participant.vars["baillon_single_choices"])][0]

        # unzip indices and form fields from <mpl_choices> list
        # round_number = self.subsession.round_number
        # form_fields = [list(t) for t in zip(*self.participant.vars['baillon_choices'])][1]
        # indices = [list(t) for t in zip(*self.participant.vars['baillon_choices'])][0]
        # index = indices[round_number - 1]

        for j, choice in zip(indices, form_fields):
            choice_i = getattr(self.player, choice)
            self.participant.vars["baillon_choices_made"][j - 1] = choice_i

        self.player.set_payoffs()
        self.player.set_consistency()
        self.player.set_switching_row()




class Historic_Viz(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment_displayed"] == False and self.round_number == 1:
            return True

    def js_vars(self):
        return dict(
            page = "historic",
            treatment=self.participant.vars["treatment"],
            location=self.participant.vars["location"],
        )

class Forecast_Viz(Page):
    def is_displayed(self):
        if self.subsession.this_app_constants()["treatment_displayed"] == True and self.round_number == 1: # as defined in post_baillon/models
            return True

    def js_vars(self):
        return dict(
            page = "forecast",
            treatment = self.participant.vars["treatment"],
            location = self.participant.vars["location"],
        )


page_sequence = [Baillon_Instructions,
                 # Historic_Viz,
                 # Forecast_Viz,
                 Baillon_Decision]
