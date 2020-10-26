from Baillon.models import Constants as OriginalConstants, SharedBaseSubsession, SharedBaseGroup, SharedBasePlayer


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
