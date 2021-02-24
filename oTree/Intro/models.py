from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from django.forms.widgets import CheckboxSelectMultiple
import re
import random

author = "Hauke Roggenkamp"

doc = """
Welcome participants, display instructions and comprehension questions.
"""


class Constants(BaseConstants):
    name_in_url = "Intro"
    players_per_group = None
    num_rounds = 1
    bonus = 10

    locations = ["Weiskirchen", "Ilomantsi"]  # ["confirmation", "contradiction"]
    treatments = ["best_guess", "interval", "both"]
    Weiskirchen_temp = 9
    Ilomantsi_temp = 3



class Subsession(BaseSubsession):
    def creating_session(self):
        # make settings here such that the instructions match the location etc.
        if self.round_number == 1:
            locations = Constants.locations.copy()
            treatments = Constants.treatments.copy()
            for p in self.get_players():
                # set location variable
                if self.session.config["location"] == "random":
                    p.participant.vars["location"] = random.choice(locations)
                    p.participant.vars["treatment"] = random.choice(treatments)
                else:
                    p.participant.vars["location"] = self.session.config["location"]
                    p.participant.vars["treatment"] = self.session.config["treatment"]

                # set winning temperature conditional on location and link it to baillon event
                if p.participant.vars["location"] == "Weiskirchen":
                    p.participant.vars["observed_temp"] = Constants.Weiskirchen_temp
                    p.participant.vars["winning_event"] = "2"

                elif p.participant.vars["location"] == "Ilomantsi":
                    p.participant.vars["observed_temp"] = Constants.Ilomantsi_temp
                    p.participant.vars["winning_event"] = "1"


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Tracking Fields
    window_width = models.IntegerField(doc="Documents the respondent's browser window's width.")
    window_height = models.IntegerField(doc="Documents the respondent's browser window's height.")
    browser = models.StringField(doc="Documents the respondent's browser (incl. its version).")

    CQ1_1 = models.IntegerField(doc="Comprehension Question 1.1", initial=20)

    def CQ1_1_error_message(self, value):
        if value != 20:
            return "Leider falsch."

    CQ1_2 = models.IntegerField(doc="Comprehension Question 1.2", initial=20)
    def CQ1_2_error_message(self, value):
        if value != 20:
            return "Leider falsch."

    CQ2_1 = models.IntegerField(doc="Comprehension Question 2.1", initial=25)
    def CQ2_1_error_message(self, value):
        if value != 25:
            return "Leider falsch."

    CQ2_2 = models.IntegerField(doc="Comprehension Question 2.2", initial=25)
    def CQ2_2_error_message(self, value):
        if value != 25:
            return "Leider falsch."

    MCQ_1 = models.StringField(
        widget=CheckboxSelectMultiple(
            choices=(
                (1, "Ihr Guthaben zu Beginn der Folgerunde beträgt 40 Punkte."),
                (2, "Ihr Guthaben zu Beginn der Folgerunde beträgt 35 Punkte."),
                (3, "Sie bekommen einen Ertrag von 25 Punkten ausgezahlt."),
            )
        ),
    )
    def MCQ_1_error_message(self, value):
        pattern = re.compile("^\[\'2\', \'3\'\]$")
        if pattern.search(value) == None:
            return "Leider falsch."

    MCQ_2 = models.StringField(
        widget=CheckboxSelectMultiple(
            choices=(
                (1, "Sie investieren Ihr gesamtes Guthaben und Ihre Gruppenmitglieder nichts."),
                (2, "Sie und Ihre Gruppenmitglieder investieren jeweils z.B. 10 Punkte."),
                (3, "Ihre Gruppenmitglieder investieren ihr gesamtes Guthaben und Sie nichts."),
                (4, "Weder Sie noch Ihre Gruppenmitglieder investieren."),
            )
        ),
    )

    def MCQ_2_error_message(self, value):
        pattern = re.compile("^\[\'2\', \'3\'\]$")
        if pattern.search(value) == None:
            return "Leider falsch."