from MPP.models import Constants as OriginalConstants, SharedBaseSubsession, SharedBaseGroup, SharedBasePlayer


author = "Hauke Roggenkamp"

doc = """
This app is a clone of another app (MPP) that is designed to elicit beliefs via  Multiple Point Prediction (MPP) as 
proposed in Eyting & Schmidt (2020, Working Paper).

As such, this app is just an iteration of the original app. The only element that is new in this app is the introduction
of additional information.
"""


class Constants(OriginalConstants):
    name_in_url = "postMPP"


class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment_displayed = True
        )


class Group(SharedBaseGroup):
    pass


class Player(SharedBasePlayer):
    pass
