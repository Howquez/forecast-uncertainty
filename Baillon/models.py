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
    num_rounds = 6

    null_payoff = 0
    prize_payoff = 10

    currency = "EUR"

    # create (hard coded) list of choices, temperature ticks and events
    compound_event_probabilities = [00, 20, 35, 40, 45, # center 66%
                                    50, 55, 60, 65, 70,
                                    75, 80, 85, 90, 93,
                                    95, 97, 98, 99, 100]

    single_event_probabilities = [00,  5, 10, 15, 20, # to do: center 33%
                                  25, 30, 35, 40, 50,
                                  55, 60, 65, 70, 75,
                                  80, 85, 87, 88, 100]

    # probability_list = compound_event_probabilities
    num_choices = len(compound_event_probabilities)

    ticks = [0, 8, 14, 22] # min and max value is only needed for plotting options, the second and third value is important
    # ticks = [0, 2, 8, 22]
    events = ["E1", "E2", "E3", "E12", "E23", "E13"]


class SharedBaseSubsession(BaseSubsession):
    class Meta:
        abstract = True

    def creating_session(self): # having these configs in here, it is impossible to play the BSR App independently
        if self.round_number == 1:
            for p in self.get_players():

                # create event list for Baillon decision sequence once per player
                events = Constants.events.copy()
                random.shuffle(events)
                p.participant.vars["event_sequence"] = events

                # define compound events based on the string length of their name
                # compound_events = []
                # for e in events:
                #     if len(e) == 3:
                #         compound_events.append(True)
                #     else:
                #         compound_events.append(False)

                # randomly draw pivotal decision ex ante
                p.participant.vars["baillon_round_to_pay"] = random.randint(1, Constants.num_rounds)


        n = Constants.num_choices
        for p in self.get_players():

            indices = [j for j in range(1, n + 1)]
            # use the random Baillon decision sequence per player per round
            p.event_decision = p.participant.vars["event_sequence"][self.round_number - 1]
            p.participant.vars['baillon_choices_made'] = [None for j in range(1, n + 1)]
            form_fields = ["choice_" + str(k) for k in indices]
            p.participant.vars["baillon_index_to_pay"] = random.choice(indices)
            p.participant.vars["baillon_choice_to_pay"] = "choice_" + str(p.participant.vars["baillon_index_to_pay"])

            # probability_list = Constants.probability_list.copy()
            # p.participant.vars["list_probabilities"] = probability_list
            # p.participant.vars["baillon_choices"] = list(
            #     zip(indices, form_fields, p.participant.vars["list_probabilities"])
            # )

            compound_list = Constants.compound_event_probabilities.copy()
            p.participant.vars["list_compound"] = compound_list
            p.participant.vars["baillon_compound_choices"] = list(
                zip(indices, form_fields, p.participant.vars["list_compound"])
            )

            single_list = Constants.single_event_probabilities.copy()
            p.participant.vars["list_single"] = single_list
            p.participant.vars["baillon_single_choices"] = list(
                zip(indices, form_fields, p.participant.vars["list_single"])
            )


class SharedBaseGroup(BaseGroup):
    class Meta:
        abstract = True


class SharedBasePlayer(BasePlayer):
    class Meta:
        abstract = True

    BaillonQ1 = models.BooleanField(
        doc="Baillon Comprehension Question 1",
        blank=False
    )
    BaillonQ2 = models.BooleanField(
        doc="Baillon Comprehension Question 2",
        blank=False
    )
    BaillonQ3 = models.FloatField(
        doc="Baillon Comprehension Question 3",
        blank=True
    )
    BaillonQ4 = models.BooleanField(
        doc="Baillon Comprehension Question 4",
        blank=False
    )
    BaillonQ5 = models.BooleanField(
        doc="Baillon Comprehension Question 5",
        blank=False
    )


    CQ2 = models.IntegerField(
        label="Was ist der Ergebnis von 4+4?",
        doc="Question for Testing purposes",
        initial=8
    )

    for j in range(1, Constants.num_choices + 1):
        locals()['choice_' + str(j)] = models.StringField()
    del j

    switching_row = models.IntegerField(doc="First row in which B (weather dependent lottery) was selected.")
    choice_to_pay = models.StringField(doc="Randomly determined row(/choice) that determines the payment.")
    option_to_pay = models.StringField(doc="Lottery chosen in that row(/choice) the payment (weather dependent if == A).")
    probability_to_pay = models.IntegerField(doc="Probability of the classic lottery in the pivotal row(/choice).")
    event_decision = models.StringField(doc="Event that represents the weather dependent lottery in this round.")
    random_draw = models.IntegerField(doc="Random draw determining the classic lottery's outcome (win if <= probability_to_pay).")
    success = models.BooleanField(doc="True if player won in this round.", initial=False)
    is_relevant = models.BooleanField(doc="Describes whether the result determines payoff.")
    inconsistent = models.IntegerField(doc="")

    def prepare_payoffs(self):
        self.choice_to_pay = self.participant.vars["baillon_choice_to_pay"]
        self.option_to_pay = getattr(self, self.choice_to_pay)
        self.random_draw = random.randint(0, 100)
        if len(self.event_decision) == 3: #compound event
            self.probability_to_pay = self.participant.vars["list_compound"][
                self.participant.vars["baillon_index_to_pay"] - 1]
        else:
            self.probability_to_pay = self.participant.vars["list_single"][
                self.participant.vars["baillon_index_to_pay"] - 1]
        self.participant.vars["Chance"] = self.probability_to_pay

        if self.option_to_pay == "A":
            self.participant.vars["option_chosen"] = "weather event"
            if bool(re.search(self.participant.vars["winning_event"], self.event_decision)):
                self.success = True
        else:
            self.participant.vars["option_chosen"] = "lottery event"
            if self.random_draw <= self.probability_to_pay:
                self.success = True

    def set_payoffs(self):
        if bool(re.search("Baillon", self.participant.vars["winning_app"])): # if one of the baillon apps is chosen
            if not bool(re.search("post", self.participant.vars["winning_app"])): # if the pre treatment version is chosen
                if not self.subsession.this_app_constants()["treatment_displayed"]: # select pre treatment app
                    if self.round_number == self.participant.vars["baillon_round_to_pay"]: # round has to be the chosen one
                        if self.success: # the player needs to be successful to win the prize
                            self.payoff = Constants.prize_payoff
                            self.is_relevant = True
            elif bool(re.search("post", self.participant.vars["winning_app"])): # if the post treatment version is chosen:
                if self.subsession.this_app_constants()["treatment_displayed"]: # select post treatment app
                    if self.round_number == self.participant.vars["baillon_round_to_pay"]: # round has to be the chosen one
                        if self.success: # the player needs to be successful to win the prize
                            self.payoff = Constants.prize_payoff
                            self.is_relevant = True




    def set_consistency(self):
        n = Constants.num_choices
        # replace A and B by 1 and 0, respectively
        self.participant.vars["baillon_choices_made"] = [
            1 if j == "A" else 0 for j in self.participant.vars["baillon_choices_made"]
        ]
        # check for multiple switching behavior
        for j in range(1, n):
            choices = self.participant.vars["baillon_choices_made"]
            self.inconsistent = 1 if choices[j] > choices[j - 1] else 0
            if self.inconsistent == 1:
                break


    def set_switching_row(self):
        # set switching pont to row number of first "B" choice
        if self.inconsistent == 0:
            self.switching_row = sum(self.participant.vars["baillon_choices_made"]) + 1


class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment_displayed = False
        )

class Group(SharedBaseGroup):
    pass


class Player(SharedBasePlayer):
    pass
