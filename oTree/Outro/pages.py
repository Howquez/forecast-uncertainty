from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Demographic_Questions(Page):
    form_model = "player"
    form_fields = ["Age", "Gender", "Education", "Income"]

class Domain_Questions_1(Page):
    form_model = "player"
    form_fields = ["Accuracy", "Authenticity", "Credibility"]

    def js_vars(self):
        return dict(
            location=self.participant.vars["location"],
            treatment=self.participant.vars["treatment"],
        )

class Domain_Questions_2(Page):
    form_model = "player"
    form_fields = ["Comprehension", "Usage"]

class CLICCS_Questions(Page):
    form_model = "player"
    form_fields = ["CLICCS1", "CLICCS2"]

class Results(Page):
    def js_vars(self):
        return dict(
            page="revelation",
            location=self.participant.vars["location"],

            ticks=self.participant.vars["baillon_ticks"],
            event_decision=self.participant.vars["payment_event"],
            enabledLabel=True,
            results=True,
        )


page_sequence = [Domain_Questions_1,
                 Domain_Questions_2,
                 CLICCS_Questions,
                 Demographic_Questions,
                 Results]
