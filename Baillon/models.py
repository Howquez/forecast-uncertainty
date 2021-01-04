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

author = 'Hauke Roggenkamp'

doc = """
This app is designed to measure ambiguity attitudes as proposed in Baillon et al. (2018, Econometrica).
The task at hand is an estimation of an (yet) unknown weather event. To this end, subjects are exposed to some sort of
a temperature report from a short time period in an (yet) unknown region to an unknown time. Subjects are then asked
about the temperature in 9 days after the last reported temperature.

This app is intended to be played twice in an alternating sequence where another app (BSR) is played twice as well: 
[initialize, Baillon, BSR, Baillon, BSR]
Therefore, this app is "cloned" where the clone (postBaillon) is played as the second iteration. Looking at this app in
isolation may consequently feel a little weird. This app has succeed the initialize app in order to run.
"""


class Constants(BaseConstants):

    name_in_url = 'Baillon'

    locations  = ["Weiskirchen", "Ilomantsi"] # ["confirmation", "contradiction"]
    treatments = ["best_guess", "interval", "both"]
    Weiskirchen_temp = 8 # 8.5
    Ilomantsi_temp   = 3 # 3.2

    players_per_group = None
    num_rounds = 2

    null_payoff = 0
    prize_payoff = 10

    currency = "EUR"

    ticks = [0, 8, 14, 22] # min and max value is only needed for plotting options, the second and third value is important
    # ticks = [0, 2, 8, 22]
    events = ["E1", "E2", "E3", "E12", "E23", "E13"]


class SharedBaseSubsession(BaseSubsession):
    class Meta:
        abstract = True

    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():

                # create event list for Baillon decision sequence once per player
                events = Constants.events.copy()
                random.shuffle(events)
                p.participant.vars["event_sequence"] = events

                # randomly draw pivotal decision ex ante
                p.participant.vars["baillon_round_to_pay"] = random.randint(1, Constants.num_rounds)


        for p in self.get_players():

            # use the random Baillon decision sequence per player per round
            p.event_decision = p.participant.vars["event_sequence"][self.round_number - 1]

            # ticks are needed in terminate app
            p.participant.vars["baillon_ticks"] = Constants.ticks.copy()



class SharedBaseGroup(BaseGroup):
    class Meta:
        abstract = True


class SharedBasePlayer(BasePlayer):
    class Meta:
        abstract = True

    BaillonQ1 = models.BooleanField(
        doc="Baillon Comprehension Question 1",
        blank=True
    )
    BaillonQ2 = models.BooleanField(
        doc="Baillon Comprehension Question 2",
        blank=True
    )
    BaillonQ3 = models.FloatField(
        doc="Baillon Comprehension Question 3",
        blank=True
    )
    BaillonQ4 = models.BooleanField(
        doc="Baillon Comprehension Question 4",
        blank=True
    )
    BaillonQ5 = models.BooleanField(
        doc="Baillon Comprehension Question 5",
        blank=True
    )


    CQ2 = models.IntegerField(
        label="Was ist der Ergebnis von 4+4?",
        doc="Question for Testing purposes",
        initial=8,
        blank=True
    )

    review_weather = models.IntegerField(doc="Counts the number of times a player reviews weather information.")
    review_instructions = models.IntegerField(doc="Counts the number of times a player reviews instructions.")
    window_width = models.IntegerField(doc="Documents the respondent's browser window's width.")
    window_height = models.IntegerField(doc="Documents the respondent's browser window's height.")
    browser = models.StringField(doc="Documents the respondent's browser (incl. its version).")

    baillon_equivalent = models.IntegerField(doc="Main variable")
    pivotal_lottery = models.IntegerField(doc="Random lottery that decides the outcome if it is larger than the respondent's baillon_equivalent")
    payment_mechanism = models.StringField(doc="Mechanism determining the payment in this round.")
    random_draw = models.IntegerField(doc="Random draw determining the pivotal lottery's outcome (win if it is smaller than the pivotal_lottery.")
    event_decision = models.StringField(doc="Event that represents the weather dependent lottery in this round.")
    success = models.BooleanField(doc="True if player won in this round.", initial=False)
    is_relevant = models.BooleanField(doc="Describes whether the result determines payoff.", initial=False)

    def prepare_payoffs(self):
        self.pivotal_lottery = random.randint(0, 100)
        self.random_draw = random.randint(0, 100)

        if self.pivotal_lottery >= self.baillon_equivalent: # lottery determines outcome
            self.payment_mechanism = "Lotterie"
            if self.random_draw <= self.pivotal_lottery:
                self.success = True
        else: # weather determines outcome
            self.payment_mechanism = "Wette"
            if bool(re.search(self.participant.vars["winning_event"], self.event_decision)):
                self.success = True


    def set_payoffs(self):
        if bool(re.search("Baillon", self.participant.vars["winning_app"])): # if one of the baillon apps is chosen

            if not bool(re.search("post", self.participant.vars["winning_app"])): # if the pre treatment version is chosen
                self.participant.vars["payment_task"] = "Aufgabe 1"

                if not self.subsession.this_app_constants()["treatment_displayed"]: # select pre treatment app

                    if self.round_number == self.participant.vars["baillon_round_to_pay"]: # round has to be the chosen one
                        self.participant.vars["payment_mechanism"] = self.payment_mechanism
                        self.participant.vars["payment_outcome"] = "leider verloren"
                        self.participant.vars["payment_event"] = self.event_decision
                        self.participant.vars["pivotal_lottery"] = self.pivotal_lottery
                        self.participant.vars["pivotal_equivalent"] = self.baillon_equivalent
                        self.is_relevant = True

                        if self.success: # the player needs to be successful to win the prize
                            self.payoff = Constants.prize_payoff
                            self.participant.vars["payment_outcome"] = "gewonnen"



            elif bool(re.search("post", self.participant.vars["winning_app"])): # if the post treatment version is chosen:
                self.participant.vars["payment_task"] = "Aufgabe 3"

                if self.subsession.this_app_constants()["treatment_displayed"]: # select post treatment app

                    if self.round_number == self.participant.vars["baillon_round_to_pay"]: # round has to be the chosen one
                        self.participant.vars["payment_mechanism"] = self.payment_mechanism
                        self.participant.vars["payment_outcome"] = "leider verloren"
                        self.participant.vars["payment_event"] = self.event_decision
                        self.participant.vars["pivotal_lottery"] = self.pivotal_lottery
                        self.participant.vars["pivotal_equivalent"] = self.baillon_equivalent
                        self.is_relevant = True

                        if self.success: # the player needs to be successful to win the prize
                            self.payoff = Constants.prize_payoff
                            self.participant.vars["payment_outcome"] = "gewonnen"


class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment_displayed = False
        )

class Group(SharedBaseGroup):
    pass


class Player(SharedBasePlayer):
    pass
