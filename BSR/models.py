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
    BSR_prize = [0, 10]
    observed_temp = 25
    temp_range = [0, 50]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    minTemp=models.IntegerField(
        label="Was ist die niedrigste Temperatur, die Ihrer Meinung nach gerade so noch wahrscheinlich ist?",
        min=Constants.temp_range[0],
        initial=24,
        # max=Constants.temp_range[1],
        doc="define the range of temperatures with positive probability"
    )

    def minTemp_max(self):
        return self.maxTemp

    maxTemp = models.IntegerField(
        label="Was ist die höchste Temperatur, die Ihrer Meinung nach gerade so noch wahrscheinlich ist?",
        # min=Constants.temp_range[0],
        initial=26,
        max=Constants.temp_range[1],
        doc="define the range of temperatures with positive probability"
    )

    def maxTemp_min(self):
        return self.minTemp

    prob0, prob1, prob2, prob3, prob4, prob5, prob6, prob7, prob8, prob9, prob10,\
        prob11, prob12, prob13, prob14, prob15, prob16, prob17, prob18, prob19, prob20,\
        prob21, prob22, prob23, prob24, prob25, prob26, prob27, prob28, prob29, prob30,\
        prob31, prob32, prob33, prob34, prob35, prob36, prob37, prob38, prob39, prob40,\
        prob41, prob42, prob43, prob44, prob45, prob46, prob47, prob48, prob49, prob50,\
        = [models.IntegerField(min=0,
                               max=100,
                               label="{}°C".format(i),
                               doc="probability assigned to {}°C".format(i),
                               blank=True,
                               initial=0)
    for i in range(Constants.temp_range[0],
                   Constants.temp_range[1] + 1)]

    random_int = models.IntegerField()
    loss = models.CurrencyField()

    def set_loss(self):
        self.random_int = randint(0, 100)
        self.loss = 0
        for i in range(Constants.temp_range[1] + abs(Constants.temp_range[0] + 1)): #0<=i<=49+1
            p = eval("self.prob{}".format(i))/100
            if i == Constants.observed_temp + abs(Constants.temp_range[0]):
                l=((1-p)**2)*100
            else:
                l=(p**2)*100
            self.loss+=l

    def set_payoff(self):
        if self.loss <= self.random_int:
            self.payoff = Constants.BSR_prize[1]
        else:
            self.payoff = Constants.BSR_prize[0]





    # temp01, temp02, temp03 = [make_temperature(label="{}°C".format(i)) for i in range(3)]


    # def generate_fields(self):
    #    for temp in range(10, 46):
    #        locals()["temp{}".format(temp)] = make_integer_field(label="{}°C".format(temp))



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


    pass
