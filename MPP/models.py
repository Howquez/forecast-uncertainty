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
Belief elicitation usind Eyting & Schmidt's (2019, WP) Multiple Point Prediction (MPP) Method.
"""


class Constants(BaseConstants):
    name_in_url = 'MPP'
    players_per_group = None
    num_rounds = 1

    null_payoff = 0
    prize_payoff = 10

    chance_constant = 50
    punishment_factor = 3
    punishment_scale = 3


class SharedBaseSubsession(BaseSubsession):
    class Meta:
        abstract = True

    def creating_session(self): # having these configs in here, it is impossible to play the BSR App independently
        if self.round_number == 1:
            for p in self.get_players():
                winning_round = random.randint(1, 2)
                p.participant.vars["MPP_winning_round"] = winning_round

class SharedBaseGroup(BaseGroup):
    class Meta:
        abstract = True

class SharedBasePlayer(BasePlayer):
    class Meta:
        abstract = True

    FEV1 = models.StringField(doc="FrontEndVariable1 to style table rows.")

    Q1 = models.FloatField(
        label="... wenn Überschätzen drei Mal so teuer wie Unterschätzen ist?",
        doc="Question for Testing purposes",
        blank=False
    )
    diff_Q1 = models.FloatField(doc="Difference between guess and realized value.")
    costs_Q1 = models.FloatField(doc="Loss stemming from corresponding difference.")
    chance_Q1 = models.FloatField(doc="Winning probability stemming from corresponding difference.")


    Q2 = models.FloatField(
        label="... wenn Überschätzen genau so teuer wie Unterschätzen ist?",
        doc="Question for Testing purposes",
        blank=False
    )
    diff_Q2 = models.FloatField(doc="Difference between guess and realized value.")
    costs_Q2 = models.FloatField(doc="Loss stemming from corresponding difference.")
    chance_Q2 = models.FloatField(doc="Winning probability stemming from corresponding difference.")

    Q3 = models.FloatField(
        label="... wenn Überschätzen drei Mal so teuer wie Unterschätzen ist?",
        doc="Question for Testing purposes",
        blank=False
    )
    diff_Q3 = models.FloatField(doc="Difference between guess and realized value.")
    costs_Q3 = models.FloatField(doc="Loss stemming from corresponding difference.")
    chance_Q3 = models.FloatField(doc="Winning probability stemming from corresponding difference.")

    total_chance = models.IntegerField(doc="Chance of winning the prize.")
    rand_number = models.IntegerField(doc="Random number choosing the prize.")

    def set_payoff(self):
        realization = self.participant.vars["observed_temp"]

        self.diff_Q1 = round(self.Q1 - realization, 1)
        if self.diff_Q1 > 0:
            self.costs_Q1 = self.diff_Q1 * Constants.punishment_scale
        else:
            self.costs_Q1 = abs(self.diff_Q1) * Constants.punishment_factor * Constants.punishment_scale
        self.chance_Q1 = Constants.chance_constant - self.costs_Q1

        self.diff_Q2 = round(self.Q2 - realization, 1)
        self.costs_Q2 = abs(self.diff_Q2) * Constants.punishment_scale
        self.chance_Q2 = Constants.chance_constant - self.costs_Q2

        self.diff_Q3 = round(self.Q3 - realization, 1)
        if self.diff_Q3 > 0:
            self.costs_Q3 = self.diff_Q3 * Constants.punishment_factor * Constants.punishment_scale
        else:
            self.costs_Q3 = abs(self.diff_Q3) * Constants.punishment_scale
        self.chance_Q3 = Constants.chance_constant - self.costs_Q3

        self.total_chance = int((self.chance_Q1 + self.chance_Q2 + self.chance_Q3) / (3 * Constants.chance_constant) * 100)
        if self.total_chance < 0:
            self.total_chance = 0

        self.rand_number = random.randint(0, 100)

        if self.rand_number < self.total_chance:
            self.payoff = Constants.prize_payoff
        else:
            self.payoff = Constants.null_payoff


class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment_displayed = False
        )

class Group(SharedBaseGroup):
    pass

class Player(SharedBasePlayer):
    pass
