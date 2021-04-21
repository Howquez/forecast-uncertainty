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
import re


author = "Hauke Roggenkamp"

doc = """
This app is designed to measure ambiguity attitudes as proposed in Baillon et al. (2018, Econometrica).
The task at hand is an estimation of an (yet) unknown weather event. To this end, subjects are exposed to some sort of
a temperature report from a short time period in an (yet) unknown region to an unknown time. Subjects are then asked
about the temperature in 9 days after the last reported temperature.
"""


class Constants(BaseConstants):
    name_in_url = "Baillon"

    locations = ["Weiskirchen", "Ilomantsi"]  # ["confirmation", "contradiction"]
    treatments = ["best_guess", "interval", "both"]
    Weiskirchen_temp = 8
    Ilomantsi_temp = 3

    players_per_group = None
    num_rounds = 12

    null_payoff = 0
    prize_payoff = 10

    currency = "EUR"

    ticks = [0, 8, 14, 22]  # min and max value is only needed for plotting options, the second and third value is important
    events = ["E1", "E2", "E3", "E12", "E23", "E13"]


class Subsession(BaseSubsession):
    pivotal_round = models.BooleanField(doc="round_to_pay", initial=False)
    lottery_success = models.BooleanField(doc="lottery_success", initial=False)
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                # create event list for Baillon decision sequence once per player
                events = Constants.events.copy()
                random.shuffle(events)
                p.participant.vars["event_sequence"] = events*2

                # randomly draw pivotal decision ex ante
                p.participant.vars["round_to_pay"] = random.randint(1, Constants.num_rounds)

                # prepare lottery outcome for pivotal decision ex ante
                p.participant.vars["pivotal_lottery"] = random.randint(0, 100)
                p.participant.vars["pivotal_draw"] = random.randint(0, 99)
                p.participant.vars["lottery_success"] = False
                if p.participant.vars["pivotal_lottery"] > p.participant.vars["pivotal_draw"]:
                    p.participant.vars["lottery_success"] = True

                # ticks are needed in terminate app
                p.participant.vars["baillon_ticks"] = Constants.ticks.copy()

        for p in self.get_players():
            # use the random Baillon decision sequence per player per round
            p.event_decision = p.participant.vars["event_sequence"][self.round_number - 1]
            if self.round_number == p.participant.vars["round_to_pay"]:
                self.pivotal_round = True
                self.lottery_success = True



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    review_weather = models.IntegerField(doc="Counts the number of times a player reviews weather information.",
                                         initial=0,
                                         blank=True)
    review_instructions = models.IntegerField(doc="Counts the number of times a player reviews instructions.",
                                         initial=0,
                                         blank=True)
    review_contact = models.IntegerField(doc="Counts the number of times a player reviews contact information.",
                                         initial=0,
                                         blank=True)
    matching_probability = models.IntegerField(doc="Main variable", min=0, max=101)
    event_decision = models.StringField(doc="Weather event code the bet corresponds to.")
    payment_mechanism = models.StringField(doc="Describes whether player is paid via lottery or bet.")
    pivotal_lottery = models.IntegerField(doc="listed for debugging purposes")
    pivotal_draw = models.IntegerField(doc="listed for debugging purposes")



    def set_payoffs(self):
        self.payoff == 0
        if self.round_number == self.participant.vars["round_to_pay"]:
            self.participant.vars["payment_event"] = self.event_decision # for revelation_viz on last screen
            self.participant.vars["pivotal_matching_probability"] = self.matching_probability
            self.pivotal_lottery = self.participant.vars["pivotal_lottery"]
            if self.matching_probability <= self.pivotal_lottery:
                self.payment_mechanism = "lottery"
                self.participant.vars["mechanism"] = "Lotterie"
                self. pivotal_draw = self.participant.vars["pivotal_draw"]
                if self.participant.vars["lottery_success"]:
                    self.payoff = Constants.prize_payoff
            else:
                self.payment_mechanism = "bet"
                self.participant.vars["mechanism"] = "Wette"
                if bool(re.search(self.participant.vars["winning_event"], self.event_decision)):
                    self.participant.vars["bet_success"] = True
                    self.payoff = Constants.prize_payoff
                else:
                    self.participant.vars["bet_success"] = False
