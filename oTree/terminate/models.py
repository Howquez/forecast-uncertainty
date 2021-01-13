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


author = "Hauke Roggenkamp"

doc = """
Similar to the initialize app, this app wraps the survey/experiment and closes it. It utilizes participant vars to display
results and payoffs. In addition, it contains a little survey for control variables.
"""


class Constants(BaseConstants):
    name_in_url = 'terminate'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Demographics
    Age = models.IntegerField(doc="Respondent's age",
                              label="Wie alt sind Sie?")
    Gender = models.StringField(doc="Respondent's gender",
                                label="Geschlecht",
                                choices=[
                                    ["female", "weiblich"],
                                    ["male", "männlich"],
                                    ["diverse", "divers"],
                                    ["not specified", "keine Angabe"]
                                ],
                                widget=widgets.RadioSelect)

    Education = models.StringField(doc="Respondent's highest educational degree",
                                   label="Welchen beruflichen Ausbildungsabbschluss haben Sie?",
                                   choices=[
                                       ["student", "Ich bin noch in beruflicher Ausbildung (Studium oder Ausbildung)"],
                                       ["none", "Ich habe keinen beruflichen Abschluss und bin nicht in beruflicher Ausbildung"],
                                       ["apprenticeship", "Ich habe eine beruflich-betriebliche Berufsausbildung (Lehre) abgeschlossen"],
                                       ["highschool", "Ich habe eine beruflich-schulische Ausbildung (Berufsfachschule, Handelsschule) abgeschlossen"],
                                       ["applied highschool", "Ich habe eine Ausbildung an einer Fachschule, Meister-, Technikerschule, Berufs- oder Fachakademie abgeschlossen"],
                                       ["applied uni", "Ich habe einen Fachhochschulabschluss"],
                                       ["uni", "Ich habe einen Hochschulabschluss"]
                                   ],
                                   widget=widgets.RadioSelect)

    Income = models.IntegerField(doc="Respondent's income",
                                 label="Bitte nennen Sie Ihr ungefähres jährliches Nettoeinkommen.",
                                 blank=True)

    Comprehension = models.StringField(doc="Respondent's understanding of the tasks",
                                        label="Haben Sie die Aufgaben gut verstanden?",
                                        choices=[
                                            ["no", "Nein"],
                                            ["rather not", "Eher nicht"],
                                            ["rather yes", "Eher schon"],
                                            ["yes", "Ja"]
                                        ],
                                       widget=widgets.RadioSelect)

    Usage = models.IntegerField(doc="Respondent's usage of the weather forecasts",
                                label="Wie häufig nutzen Sie Wettervorhersagen im Durchschnitt",
                                choices=[
                                   [5, "Mehrmals täglich"],
                                   [4, "Täglich"],
                                   [3, "Merhmals wöchentlich"],
                                   [2, "Wöchentlich"],
                                   [1, "Seltener"],
                                   [0, "Nie"]
                                ],
                                widget=widgets.RadioSelect)

    Accuracy = models.IntegerField(doc="Respondent's assessment of message's accuracy",
                                   label="Für wie akkurat halten Sie die Aussage?",
                                   choices=[
                                       [-2, ""],
                                       [-1, ""],
                                       [0, ""],
                                       [1, ""],
                                       [2, ""]
                                   ],
                                   widget=widgets.RadioSelectHorizontal)

    Authenticity = models.IntegerField(doc="Respondent's assessment of message's authenticity",
                                   label="Für wie authentisch halten Sie die Aussage?",
                                   choices=[
                                       [-2, ""],
                                       [-1, ""],
                                       [0, ""],
                                       [1, ""],
                                       [2, ""]
                                   ],
                                   widget=widgets.RadioSelectHorizontal)

    Credibility = models.IntegerField(doc="Respondent's assessment of message's credibility",
                                      label="Für wie glaubwürdig halten Sie die Aussage?",
                                      choices=[
                                          [-2, ""],
                                          [-1, ""],
                                          [0, ""],
                                          [1, ""],
                                          [2, ""]
                                      ],
                                      widget=widgets.RadioSelectHorizontal)


    # CLICCS common questions
    CLICCS1 = models.LongStringField(doc="CLICCS' common question #1",
                                     label="Was sehen Sie als größte Herausforderung in Bezug auf ein sich wandelndes Klima?")
    CLICCS2 = models.LongStringField(doc="CLICCS' common question #2",
                                     label="Wie gehen Sie damit um?")


    # Domain specific questions
