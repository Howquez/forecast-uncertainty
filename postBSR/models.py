from BSR.models import Constants as OriginalConstants, SharedBaseSubsession, SharedBaseGroup, SharedBasePlayer

class Constants(OriginalConstants):
    name_in_url = "postBSR"


class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment="post"
        )


class Group(SharedBaseGroup):
    pass


class Player(SharedBasePlayer):

    pass

