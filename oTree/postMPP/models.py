from MPP.models import Constants as OriginalConstants, SharedBaseSubsession, SharedBaseGroup, SharedBasePlayer


author = "Hauke Roggenkamp"

doc = """
Your app description
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
