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

from otree.db.models import Model, ForeignKey

from random import randint, seed

seed(123456)


author = 'Hauke Roggenkamp'

doc = """
This app is designed to elicit a respondent's belief distribution using Hossain & Okui's (2013) Binarized Scoring Rule
"""


class Constants(BaseConstants):
    name_in_url = 'BSR'
    players_per_group = None
    num_rounds = 1

    null_payoff = 0
    prize_payoff = 10
    TEMP_RANGE = [-15, 50]
    temps = [j for j in range(TEMP_RANGE[0], TEMP_RANGE[1] + 1)]

    weight = 0.5


class SharedBaseSubsession(BaseSubsession):
    class Meta:
        abstract = True


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

    minTemp = models.IntegerField(
        label="Was ist die niedrigste Temperatur, die Ihrer Meinung nach gerade so noch wahrscheinlich ist?",
        doc="Name the lowest temperature you assign a positive probability of occurring to.",
        min=Constants.TEMP_RANGE[0],
        initial=22,
        blank=True

    )

    maxTemp = models.IntegerField(
        label="Was ist die höchste Temperatur, die Ihrer Meinung nach gerade so noch wahrscheinlich ist?",
        doc="Name the highest temperature you assign a positive probability of occurring to.",
        max=Constants.TEMP_RANGE[1],
        initial=28,
        blank=True
    )

    # define form fields for each temperature
    for i in Constants.temps:
        locals()['prob' + str(i).replace("-", "minus")] = models.IntegerField(
            label=str(i),
            doc="probability assigned to {}°C".format(i),
            min=0,
            max=100,
            initial=0,
            blank=False
        )
    del i

    random_int = models.IntegerField()
    loss = models.CurrencyField()
    winning_prob = models.IntegerField()
    chance2win = models.IntegerField()

    def set_loss(self):  # create Loss Function loss = \Sigma_{i=0}^{50} (1-p_i)^2
        self.loss = 0
        for temp in Constants.temps:
            p = eval("self.prob" + str(temp).replace("-", "minus"))
            # p = eval("self.prob{}".format(str(temp).replace("-", "minus"))) / 100
            if temp == self.participant.vars["observed_temp"]:
                self.winning_prob = int(p * 100)
                l = ((1 - p) ** 2) * 100 * Constants.weight
            else:
                l = (p ** 2) * 100 * Constants.weight
            self.loss += l

        if int(round(100 - self.loss, 0)) < 0:
            self.chance2win = 0
        else:
            self.chance2win = int(round(100 - self.loss, 0))

    def set_payoff(self):
        self.random_int = randint(0, 100)
        if self.loss <= self.random_int:
            self.payoff = Constants.prize_payoff
            self.FEV1 = "alert-success"
        else:
            self.payoff = Constants.null_payoff
            self.FEV1 = "alert-danger"

    FEV1 = models.StringField(
        doc="FrontEndVariable 1 to define appearance of alert on Results Page"
    )

    commonQuestion1 = models.LongStringField(
        label="Was sehen Sie als die größte Herausforderung in Bezug auf ein sich veränderndes Klima?",
        doc="What do you see as the biggest challenge with respect to a changing climate?",
        blank=True
    )

    commonQuestion2 = models.LongStringField(
        label="Wie gehen Sie damit um?",
        doc="How are you dealing with it?[Referring to commonQuestion1",
        blank=True
    )


class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment_displayed = False
        )

class Group(SharedBaseGroup):
    pass


class Player(SharedBasePlayer):
    # def calc_each_loss(self):
    #     losses = dict()
    #     for winner_temp in Constants.temps:
    #         loss = 0
    #         for temp in Constants.temps:
    #             p = eval("self.prob{}".format(temp)) / 100
    #             if temp == winner_temp:
    #                 l = ((1 - p) ** 2) * 100 * Constants.weight
    #             else:
    #                 l = (p ** 2) * 100 * Constants.weight
    #             loss+=l
    #         losses.update({"loss{}".format(winner_temp):loss})
    pass




    # temp01, temp02, temp03 = [make_temperature(label="{}°C".format(i)) for i in range(3)]


    # def generate_fields(self):
    #    for temp in range(10, 46):
    #        locals()["temp{}".format(temp)] = models.IntegerField(min=0,
    #                            max=100,
    #                            label="{}°C".format(temp),
    #                            doc="probability assigned to {}°C".format(temp),
    #                            blank=True,
    #                            initial=0)



    # def make_temperature(label):
    #     return models.IntegerField(
    #         min=0,
    #         max=100,
    #         label=label,
    #         doc="probability assignment"
    #     )
    # def generate_fields(self):
    #    for temp in range(self.minTemp, self.maxTemp + 1):
    #        locals()["temp{0}".format(temp)] = make_integer_field(label="{}°C".format(temp))






    # generate_fields()

    # tempDict={}
    # for temp in range(minTemp, maxTemp):
    #     tempDict["temp{}".format(x)] = make_integer_field(label="{}°C".format(x))


    # for x in range(0, 2):
    #     tempList["temp{}".format(x)] = make_integer_field(label="{}°C".format(x))


