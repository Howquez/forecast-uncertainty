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


author = 'Hauke Roggenkamp'

doc = """
This app is designed to elicit a respondent's belief distribution using Hossain & Okui's (2013) Binarized Scoring Rule
"""


class Constants(BaseConstants):
    name_in_url = 'BSR'
    players_per_group = None
    num_rounds = 1
    temp_range = [-9, 40]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    minTemp=models.IntegerField(
        label="Was ist die niedrigste Temperatur, die Ihrer Meinung nach gerade so noch wahrscheinlich ist?",
        min=Constants.temp_range[0],
        # max=Constants.temp_range[1],
        doc="define the range of temperatures with positive probability"
    )

    def minTemp_max(self):
        return self.maxTemp

    maxTemp = models.IntegerField(
        label="Was ist die höchste Temperatur, die Ihrer Meinung nach gerade so noch wahrscheinlich ist?",
        # min=Constants.temp_range[0],
        max=Constants.temp_range[1],
        doc="define the range of temperatures with positive probability"
    )

    def maxTemp_min(self):
        return self.minTemp

    temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10,\
        temp11, temp12, temp13, temp14, temp15, temp16, temp17, temp18, temp19, temp20,\
        temp21, temp22, temp23, temp24, temp25, temp26, temp27, temp28, temp29, temp30,\
        temp31, temp32, temp33, temp34, temp35, temp36, temp37, temp38, temp39, temp40,\
        temp41, temp42, temp43, temp44, temp45, temp46, temp47, temp48, temp49, temp50, temp51,\
        = [models.IntegerField(min=0,
                               max=100,
                               label="{}°C".format(i),
                               doc="{}°C".format(i),
                               blank=True,
                               initial=0)
    for i in range(Constants.temp_range[0]-1,
                   Constants.temp_range[1]+1)]




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
