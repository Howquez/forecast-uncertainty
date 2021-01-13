from Baillon.models import Constants as OriginalConstants, SharedBaseSubsession, SharedBaseGroup, SharedBasePlayer


author = 'Hauke Roggenkamp'

doc = """
This app is a clone of another app (Baillon) that is designed to measure ambiguity attitudes as proposed in Baillon et al. 
(2018, Econometrica).

As such, this app is just an iteration of the original app. The only element that is new in this app is the introduction
of additional information.
"""


class Constants(OriginalConstants):
    name_in_url = "postBaillon"



class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment_displayed = True
        )
    pass


class Group(SharedBaseGroup):
    pass


class Player(SharedBasePlayer):
    pass
