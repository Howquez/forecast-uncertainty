from Baillon.models import Constants as OriginalConstants, SharedBaseSubsession, SharedBaseGroup, SharedBasePlayer


author = 'Hauke Roggenkamp'

doc = """
This app is a clone of another app (Baillon) that is designed to measure ambiguity attitudes as prposed in Baillon et al. 
(2018, Econometrica).

As such, this app is just an iteration of the original app. The only element that is new in this app is the introduction
of a treatment that corresponds to the whole survey (and in particular to the following apps).


The task at hand is an estimation of an (yet) unknown weather event. To this end, subjects are exposed to some sort of
a temperature report from a short time period in an (yet) unknown region to an unknown time. Subjects are then asked
about the temperature in 9 days after the last reported temperature.

The treatment is the introduction of a weather forecast for the same region and period as the weather report mentioned
above.

This app is intended to be played twice in an alternating sequence where another app (Baillon) is played twice as well: 
[initialize, Baillon, BSR, Baillon, BSR]
Therefore, this app is "cloned" where the clone (postBSR) is played as the second iteration. Looking at this app in
isolation may consequently break.
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
