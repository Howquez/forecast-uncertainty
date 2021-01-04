# coding=utf-8
# coding=utf-8
# coding=utf-8
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
import math
import re



author = "Hauke Roggenkamp"

doc = """
Belief elicitation using Eyting & Schmidt's (2019, WP) Multiple Point Prediction (MPP) Method.
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

    # a deviation from the observed temp costs punishment_scale/(3*chance_constant)*100 PP per °C (with 3 questions)
    # this equals 2 PP for each degree°C with chance_constant = 50 & punishment_scale = 3 & punishment_scale = 1


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

    review_weather = models.IntegerField(doc="Counts the number of times a player reviews weather information.")
    review_instructions = models.IntegerField(doc="Counts the number of times a player reviews instructions.")
    window_width = models.IntegerField(doc="Documents the respondent's browser window's width.")
    window_height = models.IntegerField(doc="Documents the respondent's browser window's height.")
    browser = models.StringField(doc="Documents the respondent's browser (incl. its version).")

    FEV1 = models.StringField(doc="FrontEndVariable1 to style table rows.")

    lower_bound = models.FloatField(
        label="... wenn Überschätzen drei Mal so teuer wie Unterschätzen ist?",
        doc="Question for Testing purposes",
        blank=False
    )
    diff_LB = models.FloatField(doc="Difference between guess and realized value.")
    costs_LB = models.FloatField(doc="Loss stemming from corresponding difference.")
    chance_LB = models.FloatField(doc="Winning probability stemming from corresponding difference.")


    best_guess = models.FloatField(
        label="... wenn Überschätzen genau so teuer wie Unterschätzen ist?",
        doc="Question for Testing purposes",
        blank=False
    )
    diff_BG = models.FloatField(doc="Difference between guess and realized value.")
    costs_BG = models.FloatField(doc="Loss stemming from corresponding difference.")
    chance_BG = models.FloatField(doc="Winning probability stemming from corresponding difference.")

    upper_bound = models.FloatField(
        label="... wenn Unterschätzen drei Mal so teuer wie Überschätzen ist?",
        doc="Question for Testing purposes",
        blank=False
    )
    diff_UB = models.FloatField(doc="Difference between guess and realized value.")
    costs_UB = models.FloatField(doc="Loss stemming from corresponding difference.")
    chance_UB = models.FloatField(doc="Winning probability stemming from corresponding difference.")

    total_chance = models.IntegerField(doc="Chance of winning the prize.")
    random_draw = models.IntegerField(doc="Random draw determining the classic lottery's outcome (win if <= probability_to_pay).")
    success = models.BooleanField(doc="True if player won in this round.", initial=False)
    is_relevant = models.BooleanField(doc="Describes whether the result determines payoff.")


    def prepare_payoffs(self):
        realization = self.participant.vars["observed_temp"]

        self.diff_LB = round(self.lower_bound - realization, 1)
        if self.diff_LB > 0:
            self.costs_LB = self.diff_LB * Constants.punishment_scale * Constants.punishment_factor
        else:
            self.costs_LB = -self.diff_LB * Constants.punishment_scale
        self.chance_LB = Constants.chance_constant - self.costs_LB

        self.diff_BG = round(self.best_guess - realization, 1)
        if self.diff_BG > 0:
            self.costs_BG = self.diff_BG * Constants.punishment_scale
        else:
            self.costs_BG = -self.diff_BG * Constants.punishment_scale
        self.chance_BG = Constants.chance_constant - self.costs_BG

        self.diff_UB = round(self.upper_bound - realization, 1)
        if self.diff_UB > 0:
            self.costs_UB = self.diff_UB * Constants.punishment_scale
        else:
            self.costs_UB = -self.diff_UB * Constants.punishment_scale * Constants.punishment_factor
        self.chance_UB = Constants.chance_constant - self.costs_UB

        self.total_chance = math.ceil((self.chance_LB + self.chance_BG + self.chance_UB) / (3 * Constants.chance_constant) * 100)
        if self.total_chance < 0:
            self.total_chance = 0

        self.random_draw = random.randint(0, 100)

        if self.random_draw < self.total_chance:
            self.success = True

    def set_payoffs(self):
        if bool(re.search("MPP", self.participant.vars["winning_app"])): # if one of the MPP apps is chosen
            if not bool(re.search("post", self.participant.vars["winning_app"])): # if the pre treatment version is chosen
                self.participant.vars["payment_task"] = "Aufgabe 2"
                if not self.subsession.this_app_constants()["treatment_displayed"]: # select pre treatment app
                    self.participant.vars["payment_outcome"] = "leider verloren"
                    self.is_relevant = True
                    self.store_payoff_info()

                    if self.success: # the player needs to be successful to win the prize
                        self.payoff = Constants.prize_payoff
                        self.participant.vars["payment_outcome"] = "gewonnen"
            elif bool(re.search("post", self.participant.vars["winning_app"])): # if the post treatment version is chosen:
                self.participant.vars["payment_task"] = "Aufgabe 4"
                if self.subsession.this_app_constants()["treatment_displayed"]: # select post treatment app
                    self.participant.vars["payment_outcome"] = "leider verloren"
                    self.is_relevant = True
                    self.store_payoff_info()

                    if self.success: # the player needs to be successful to win the prize
                        self.payoff = Constants.prize_payoff
                        self.participant.vars["payment_outcome"] = "gewonnen"

    def store_payoff_info(self):
        self.participant.vars["MPP_guess"] = [self.lower_bound, self.best_guess, self.upper_bound]
        self.participant.vars["MPP_diffs"] = [self.diff_LB, self.diff_BG, self.diff_UB]
        costs = [self.costs_LB, self.costs_BG, self.costs_UB]
        self.participant.vars["MPP_loss"] = [x * 2/3 for x in costs] # costs in percentage points
        self.participant.vars["Chance"] = self.total_chance


class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment_displayed = False
        )

class Group(SharedBaseGroup):
    pass

class Player(SharedBasePlayer):
    pass
