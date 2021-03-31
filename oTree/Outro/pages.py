from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Outro_Belief(Page):
    form_model = "player"
    form_fields = ["Belief"]

class Outro_Risk(Page):
    form_model = "player"
    form_fields = ["Risk_General", "Risk_Weather"]

    def vars_for_template(self):
        return dict(
            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )

class Demographic_Questions(Page):
    form_model = "player"
    form_fields = ["Age", "Gender", "Family", "Kids", "Education", "Income", "ZIP"]

class Domain_Questions_1(Page):
    form_model = "player"
    form_fields = ["Accuracy", "Credibility"]

    def vars_for_template(self):
        return dict(
            choices=[0, 1, 2, 3, 4],
        )

    def js_vars(self):
        return dict(
            location=self.participant.vars["location"],
            treatment=self.participant.vars["treatment"],
        )

class Domain_Questions_2(Page):
    form_model = "player"
    form_fields = ["Comprehension", "Usage", "Temp"]

class CLICCS_Questions(Page):
    form_model = "player"
    form_fields = ["CLICCS1", "CLICCS2"]

class Results(Page):
    form_model = "player"
    form_fields = ["openText"]

    def js_vars(self):
        return dict(
            page="revelation",
            location=self.participant.vars["location"],

            ticks=self.participant.vars["baillon_ticks"],
            event_decision=self.participant.vars["payment_event"],
            enabledLabel=True,
            results=True,
        )


page_sequence = [Outro_Belief,
                 Outro_Risk,
                 Domain_Questions_1,
                 Domain_Questions_2,
                 Demographic_Questions,
                 CLICCS_Questions,
                 Results]
