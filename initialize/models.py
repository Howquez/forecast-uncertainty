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
# from random import randrange

author = 'Hauke Roggenkamp'

doc = """
This app initializes the remainder of the survey and sets participant vars that are used in Baillon and BSR apps.
It is also a convenient place to carry general app overarching instructions.
"""


class Constants(BaseConstants):
    name_in_url = 'initialize'
    players_per_group = None
    num_rounds = 1

    locations = ["Weiskirchen", "Ilomantsi"]  # ["confirmation", "contradiction"]
    treatments = ["best_guess", "interval", "both"]
    Weiskirchen_temp = 8.5
    Ilomantsi_temp = 3.2

    null_payoff = 0
    prize_payoff = 10

    payment = 10
    currency = "EUR"


class Subsession(BaseSubsession):
    def creating_session(self): # having these configs in here, it is impossible to play the BSR App independently
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
                # print(p.participant.vars["location"])

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
    pass