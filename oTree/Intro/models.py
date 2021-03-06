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

import random

author = "Hauke Roggenkamp"

doc = """
Welcome participants, display instructions and comprehension questions.
"""


class Constants(BaseConstants):
    name_in_url = "Intro"
    players_per_group = None
    num_rounds = 1
    bonus = 10 # same as Constants.prize_payoff in Uncertainty

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

                # store information in Player Class
                p.location = p.participant.vars["location"]
                p.treatment = p.participant.vars["treatment"]

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
    wrong_answer_1 = models.IntegerField(doc="Counts the number of wrong guesses for CQ_1.", initial=0)
    wrong_answer_2 = models.IntegerField(doc="Counts the number of wrong guesses for CQ_2.", initial=0)

    # Treatment Info
    location = models.StringField()
    treatment = models.StringField()

    CQ_1 = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[
            [False, "10 Euro"],
            [False, "7 Euro"],
            [False, "3 Euro"],
            [True, "0 Euro"],
            [False, "Weiß nicht"]
        ]
    )
    def CQ_1_error_message(self, value):
        if not value:
            self.wrong_answer_1 += 1
            return "Versuchen Sie es noch einmal."

    CQ_2 = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[
            [False, "10 Euro"],
            [False, "7 Euro"],
            [False, "3 Euro"],
            [True, "0 Euro"],
            [False, "Weiß nicht"]
        ]
    )

    def CQ_2_error_message(self, value):
        if not value:
            self.wrong_answer_2 += 1
            return "Versuchen Sie es noch einmal."