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
from random import randrange


author = 'Hauke Roggenkamp'

doc = """
This app is designed to measure ambiguity attitudes as prposed in Baillon et al. (2018, Econometrica).
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
    compound_event_porbabilities = [00, 20, 35, 40, 45, # center 66%
                                    50, 55, 60, 65, 70,
                                    75, 80, 85, 90, 93,
                                    95, 97, 98, 99, 100]

    single_event_porbabilities = [00,  5, 10, 15, 20, # to do: center 33%
                                  25, 30, 35, 40, 50,
                                  55, 60, 65, 70, 75,
                                  80, 85, 87, 88, 100]

    # probability_list = compound_event_porbabilities
    num_choices = len(compound_event_porbabilities)

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
                p.participant.vars["baillon_pivotal_round"] = randrange(1, 7)


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

            compound_list = Constants.compound_event_porbabilities.copy()
            p.participant.vars["list_compound"] = compound_list
            p.participant.vars["baillon_compound_choices"] = list(
                zip(indices, form_fields, p.participant.vars["list_compound"])
            )

            single_list = Constants.single_event_porbabilities.copy()
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

    CQ1 = models.StringField(
        label="Haben Sie Ihre Entscheidungssituation verstanden?",
        doc="Comprehension Question 1",
        widget=widgets.RadioSelect,
        choices=[
            ["No", "Nein"],
            ["Yes", "Ja"],
        ],
        initial="Yes"
    )

    CQ2 = models.IntegerField(
        label="Was ist der Ergebnis von 4+4?",
        doc="Question for Testing purposes",
        initial=8
    )

    for j in range(1, Constants.num_choices + 1):
        locals()['choice_' + str(j)] = models.StringField()
    del j

    event_decision = models.StringField(doc="")
    random_draw = models.IntegerField(doc="")
    choice_to_pay = models.StringField(doc="")
    probability_to_pay = models.IntegerField(doc="")
    option_to_pay = models.StringField(doc="")
    inconsistent = models.IntegerField(doc="")
    switching_row = models.IntegerField(doc="")

    def set_payoffs(self):
        self.choice_to_pay = self.participant.vars['baillon_choice_to_pay']
        self.option_to_pay = getattr(self, self.choice_to_pay)
        self.random_draw = randrange(0, 101)
        if len(self.event_decision) == 3: #compound event
            self.probability_to_pay = self.participant.vars["list_compound"][
                self.participant.vars["baillon_index_to_pay"] - 1]
        else:
            self.probability_to_pay = self.participant.vars["list_single"][
                self.participant.vars["baillon_index_to_pay"] - 1]

        # self.probability_to_pay = self.participant.vars["list_probabilities"][self.participant.vars["baillon_index_to_pay"] - 1]


        if self.option_to_pay == "A":
            self.participant.vars["option_chosen"] = "weather event"
            if bool(re.search(self.participant.vars["winning_event"], self.event_decision)):
                self.payoff = Constants.prize_payoff
            else:
                self.payoff = Constants.null_payoff
        else:
            self.participant.vars["option_chosen"] = "lottery event"
            if self.random_draw > self.probability_to_pay:
                self.payoff = Constants.null_payoff
            else:
                self.payoff = Constants.prize_payoff

        # make payoff in round accessible in other apps by writing it into participant vars
        self.participant.vars["baillon_payoff" + str(self.round_number)] = self.payoff


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
