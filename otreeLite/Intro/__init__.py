from otree.api import *
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = "Intro"
    players_per_group = None
    num_rounds = 1
    bonus = 10  # same as Constants.prize_payoff in Uncertainty

    locations = ["Weiskirchen", "Ilomantsi"]  # ["confirmation", "contradiction"]
    treatments = ["best_guess", "interval", "both"]
    Weiskirchen_temp = 9
    Ilomantsi_temp = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Treatment Info
    location = models.StringField()
    treatment = models.StringField()

    # Tracking
    wrong_answer_1 = models.IntegerField(doc="Counts the number of wrong guesses for CQ_1.", initial=0)
    wrong_answer_2 = models.IntegerField(doc="Counts the number of wrong guesses for CQ_2.", initial=0)

    CQ_1 = models.IntegerField(
        choices=[
            [10, "10 Euro"],
            [7, "7 Euro"],
            [3, "3 Euro"],
            [0, "0 Euro"],
            [9999, "Weiß nicht"]
        ],
        widget=widgets.RadioSelect
    )

    CQ_2 = models.IntegerField(
        choices=[
            [10, "10 Euro"],
            [7, "7 Euro"],
            [3, "3 Euro"],
            [0, "0 Euro"],
            [9999, "Weiß nicht"]
        ],
        widget=widgets.RadioSelect
    )


# FUNCTIONS
def creating_session(subsession: BaseSubsession):
    # define settings here (i.e. in Intro App) such that the instructions match the location etc.
    if subsession.round_number == 1:
        locations = Constants.locations.copy()
        treatments = Constants.treatments.copy()

        for p in subsession.get_players():
            # set location variable
            if subsession.session.config["location"] == "random":
                p.participant.location = random.choice(locations)
                p.participant.treatment = random.choice(treatments)
            else:
                p.participant.location = subsession.session.config["location"]
                p.participant.treatment = subsession.session.config["treatment"]

            # store information in Player Class
            p.location = p.participant.location
            p.treatment = p.participant.treatment

            # set winning temperature conditional on location and link it to baillon event
            if p.participant.location == "Weiskirchen":
                p.participant.observed_temp = Constants.Weiskirchen_temp
                p.participant.winning_event = "2"

            elif p.participant.location == "Ilomantsi":
                p.participant.observed_temp = Constants.Ilomantsi_temp
                p.participant.winning_event = "1"


# PAGES
class Intro_Welcome(Page):
    pass


class Intro_Instructions(Page):
    form_model = "player"
    form_fields = ["CQ_1", "CQ_2"]

    @staticmethod
    def js_vars(player):
        return dict(
            template="instructions",
            event_decision="E2",
            ticks=[0, 8, 14, 22],
            treatment=player.participant.vars["treatment"],
            location=player.participant.vars["location"],

        )

    @staticmethod
    def error_message(player, values):
        if values['CQ_1'] != 0:
            player.wrong_answer_1 += 1
            return 'Fehler in Frage 1. Versuchen Sie es noch einmal.'
        if values['CQ_2'] != 0:
            player.wrong_answer_2 += 1
            return 'Fehler in Frage 2. Versuchen Sie es noch einmal.'

    @staticmethod
    def vars_for_template(player):
        print(player.wrong_answer_1 + player.wrong_answer_2)
        if player.wrong_answer_1 + player.wrong_answer_2 > 2:
            screenout = True
        else:
            screenout = False

        if player.participant.label is not None:
            tic = player.participant.label
        else:
            tic = "tic_is_missing"

        return dict(
            screenout=screenout,
            redirect="https://mingle.respondi.com/s/1523917/ospe.php3?c_0002=0&return_tic="+tic,
        )


page_sequence = [Intro_Welcome, Intro_Instructions]
