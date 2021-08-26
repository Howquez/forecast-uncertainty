from otree.api import *

import random
import re

doc = """
Your app description
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

    ticks = [0, 8,
             14, 22]  # min and max value is only needed for plotting options, the second and third values are important
    events = ["E1", "E2", "E3", "E12", "E23", "E13"]


class Subsession(BaseSubsession):

    pivotal_round = models.BooleanField(doc="round_to_pay", initial=False)
    lottery_success = models.BooleanField(doc="lottery_success", initial=False)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    review_weather = models.IntegerField(doc="Counts the number of times a player reviews weather information.",
                                         initial=0,
                                         blank=True)
    review_instructions = models.IntegerField(doc="Counts the number of times a player reviews instructions.",
                                              initial=0,
                                              blank=True)

    matching_probability = models.IntegerField(doc="Main variable", min=0, max=101)
    event_decision = models.StringField(doc="Weather event code the bet corresponds to.")
    payment_mechanism = models.StringField(doc="Describes whether player is paid via lottery or bet.")
    pivotal_lottery = models.IntegerField(doc="listed for debugging purposes")
    pivotal_draw = models.IntegerField(doc="listed for debugging purposes")


# FUNCTIONS
def creating_session(subsession: BaseSubsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():

            # create event list for Baillon decision sequence once per player
            events = Constants.events.copy()
            random.shuffle(events)
            p.participant.event_sequence = events*2

            # randomly draw pivotal decision ex ante
            p.participant.round_to_pay = random.randint(1, Constants.num_rounds)

            # prepare lottery outcome for pivotal decision ex ante
            p.participant.pivotal_lottery = random.randint(0, 100)
            p.participant.pivotal_draw = random.randint(0, 99)
            p.participant.lottery_success = False
            if p.participant.pivotal_lottery > p.participant.pivotal_draw:
                p.participant.lottery_success = True

            # ticks are needed in terminate app
            p.participant.baillon_ticks = Constants.ticks.copy()

    for p in subsession.get_players():
        # use the random Baillon decision sequence per player per round
        p.event_decision = p.participant.event_sequence[subsession.round_number - 1]
        if subsession.round_number == p.participant.round_to_pay:
            subsession.pivotal_round = True
            subsession.lottery_success = True


def set_payoffs(player: Player):

    # initialize zero-payoff
    player.payoff == 0

    # get ex ante determined payment objects
    if player.round_number == player.participant.round_to_pay:
        player.participant.payment_event = player.event_decision # for revelation_viz on last screen
        player.participant.pivotal_matching_probability = player.matching_probability
        player.pivotal_lottery = player.participant.pivotal_lottery

        # consider the case where the player prefers the lottery
        if player.matching_probability <= player.pivotal_lottery:
            # document the decision
            player.payment_mechanism = "lottery"
            player.participant.mechanism = "Lotterie"
            player.pivotal_draw = player.participant.pivotal_draw

            # pay the prize if the (ex-ante drawn) lottery was a success
            if player.participant.lottery_success:
                player.payoff = Constants.prize_payoff

        # consider the case where the player prefers to bet on the weather
        else:
            # document the decision
            player.payment_mechanism = "bet"
            player.participant.mechanism = "Wette"

            # get the winning elements and test, whether the player put a bet on them
            if bool(re.search(player.participant.winning_event, player.event_decision)):
                player.participant.bet_success = True
                player.payoff = Constants.prize_payoff
            else:
                player.participant.bet_success = False


# PAGES
class Baillon_Decision(Page):
    form_model = "player"
    form_fields = ["review_weather", "review_instructions",
                   "matching_probability"]

    @staticmethod
    def js_vars(player):
        compound = False
        if len(player.event_decision) == 3:  # compound decision
            compound = True
        treatment_displayed = False
        if player.round_number > 6:
            treatment_displayed = True

        return dict(
            template="decisions",
            ticks=Constants.ticks,
            event_decision=player.event_decision,
            compound=compound,
            treatment=player.participant.treatment,
            enabledLabel=True,

            # the following three vars are needed such that the weather viz can be displayed on decision screen as well
            treatment_displayed=treatment_displayed,
            page="decision",
            location=player.participant.location,
            small=True,
        )

    @staticmethod
    def vars_for_template(player):
        treatment_displayed = False
        if player.round_number > 6:
            treatment_displayed = True
        return {
            "treatment_displayed": treatment_displayed,
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        set_payoffs(player)


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Baillon_Decision]
