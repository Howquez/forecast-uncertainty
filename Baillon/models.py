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
Your app description
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

    payment = 10
    currency = "EUR"

    # create (hard coded) list of choices, temperature ticks and events
    # --------------------------------------------------
    probability_list = [00, 20, 35, 40, 45,
                        50, 55, 60, 65, 70,
                        75, 80, 85, 90, 93,
                        95, 97, 98, 99, 100]
    num_choices = len(probability_list)

    ticks = [0, 8, 14, 22] # min and max value is only needed for plotting options, the second and third value is important
    # ticks = [0, 2, 8, 22]
    events = ["E1", "E2", "E3", "E12", "E23", "E13"]


class SharedBaseSubsession(BaseSubsession):
    class Meta:
        abstract = True

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

                # create event list for Baillon decision sequence once per player
                events = Constants.events.copy()
                random.shuffle(events)
                p.participant.vars["event_sequence"] = events

                # randomly draw pivotal decision ex ante
                p.participant.vars["baillon_pivotal_round"] = randrange(1, 7)


        n = Constants.num_choices
        for p in self.get_players():

            indices = [j for j in range(1, n + 1)]
            probability_list = Constants.probability_list.copy()
            p.participant.vars["list_probabilities"] = probability_list

            form_fields = ["choice_" + str(k) for k in indices]
            p.participant.vars["baillon_choices"] = list(
                zip(indices, form_fields, p.participant.vars["list_probabilities"])
            )

            # does not make too much sense on a participant level with multiple rounds to play
            p.participant.vars["baillon_index_to_pay"]  = random.choice(indices)
            p.participant.vars["baillon_choice_to_pay"] = "choice_" + str(p.participant.vars["baillon_index_to_pay"])

            p.participant.vars['baillon_choices_made'] = [None for j in range(1, n + 1)]

            # use the random Baillon decision sequence per player per round
            p.event_decision = p.participant.vars["event_sequence"][self.round_number - 1]


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

    event_decision = models.StringField()
    random_draw = models.IntegerField()
    choice_to_pay = models.StringField()
    probability_to_pay = models.IntegerField()
    option_to_pay = models.StringField()
    inconsistent = models.IntegerField()
    switching_row = models.IntegerField()

    def set_payoffs(self):
        self.choice_to_pay = self.participant.vars['baillon_choice_to_pay']
        self.option_to_pay = getattr(self, self.choice_to_pay)
        self.probability_to_pay = self.participant.vars["list_probabilities"][self.participant.vars["baillon_index_to_pay"] - 1]
        self.random_draw = randrange(0, 101)

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
            # print(self.in_round(self.round_number).payoff)
            # print("baillon_payoff" + str(self.round_number) + " is:", self.participant.vars["baillon_payoff" + str(self.round_number)])

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
