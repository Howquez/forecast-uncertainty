from BSR.models import Constants as OriginalConstants, SharedBaseSubsession, SharedBaseGroup, SharedBasePlayer


author = 'Hauke Roggenkamp'

doc = """
This app is a clone of another app that is designed to elicit a respondent's belief distribution using Hossain & Okui's 
(2013, Review of Economic Studies) Binarized Scoring Rule.

As such, this app is just an iteration of the original app. The only element that is new in this app is the revelation
of the events that are addressed as well as the corresponding revelation of payments.

The task at hand is an estimation of an (yet) unknown weather event. To this end, subjects are exposed to some sort of
a temperature report from a short time period in an (yet) unknown region to an unknown time. Subjects are then asked
about the temperature in 9 days after the last reported temperature.

This app is intended to be played twice in an alternating sequence where another app (Baillon) is played twice as well: 
[initialize, Baillon, BSR, Baillon, BSR]
Therefore, this app is "cloned" where the clone (postBSR) is played as the second iteration. Looking at this app in
isolation may consequently break.
"""


class Constants(OriginalConstants):
    name_in_url = "postBSR"


class Subsession(SharedBaseSubsession):
    def this_app_constants(self):
        return dict(
            treatment_displayed = True
        )


class Group(SharedBaseGroup):
    pass


class Player(SharedBasePlayer):
    pass

