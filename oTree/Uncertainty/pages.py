from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Baillon_Decision(Page):
    form_model = "player"
    form_fields = ["review_weather", "review_instructions", "review_contact",
                   "matching_probability"]

    def js_vars(self):
        compound = False
        if len(self.player.event_decision) == 3:  # compound decision
            compound = True
        treatment_displayed = False
        if self.round_number > 6:
            treatment_displayed = True

        return dict(
            ticks=Constants.ticks,
            event_decision=self.player.event_decision,
            compound=compound,
            treatment=self.participant.vars["treatment"],
            enabledLabel=True,

            # the following three vars are needed such that the weather viz can be displayed on decision screen as well
            treatment_displayed=treatment_displayed,
            page="decision",
            location=self.participant.vars["location"],
            small=True,
        )

    def vars_for_template(self):
        treatment_displayed = False
        if self.round_number > 6:
            treatment_displayed = True
        return {
            "treatment_displayed": treatment_displayed,
        }

    def before_next_page(self):
        self.player.set_payoffs()



page_sequence = [Baillon_Decision]
