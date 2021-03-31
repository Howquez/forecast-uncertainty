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
Similar to the Intro app, this app wraps the survey/experiment and closes it. It utilizes participant vars to display
results and payoffs. In addition, it contains a little survey for control variables.
"""


class Constants(BaseConstants):
    name_in_url = 'Outro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Beliefs
    Belief = models.IntegerField(doc="Respondent's stated initial belief",
                                 blank=True)

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

    Education = models.IntegerField(doc="Respondent's highest educational degree",
                                    label="Bitte wählen Sie den höchsten Bildungsabschluss, den Sie bisher erreicht haben.",# "Welchen beruflichen Ausbildungsabbschluss haben Sie?",
                                    choices=[
                                        [0, "Schule beendet ohne Abschluss"],
                                        [1, "Noch Schüler"],
                                        [2, "Volks-, Hauptschulabschluss, Quali "],
                                        [3, "Mittlere Reife, Realschul- oder gleichwertiger Abschluss"],
                                        [4, "Abgeschlossene Lehre"],
                                        [5, "Fachabitur, Fachhochschulreife"],
                                        [6, "Fachhochschul-/Hochschulabschluss"],
                                        [7, "Abitur, Hochschulreife"],
                                        [8, "Anderer Abschluss"],
                                    ],
                                   # choices=[
                                   #     ["student", "Ich bin noch in beruflicher Ausbildung (Studium oder Ausbildung)"],
                                   #     ["none",
                                   #      "Ich habe keinen beruflichen Abschluss und bin nicht in beruflicher Ausbildung"],
                                   #     ["apprenticeship",
                                   #      "Ich habe eine beruflich-betriebliche Berufsausbildung (Lehre) abgeschlossen"],
                                   #     ["highschool",
                                   #      "Ich habe eine beruflich-schulische Ausbildung (Berufsfachschule, Handelsschule) abgeschlossen"],
                                   #     ["applied highschool",
                                   #      "Ich habe eine Ausbildung an einer Fachschule, Meister-, Technikerschule, Berufs- oder Fachakademie abgeschlossen"],
                                   #     ["applied uni", "Ich habe einen Fachhochschulabschluss"],
                                   #     ["uni", "Ich habe einen Hochschulabschluss"]
                                   # ],
                                   widget=widgets.RadioSelect)

    Family = models.StringField(doc="Respondent's marital status",
                                   label="Wie ist Ihr Familienstand?",
                                   choices=[
                                       ["married", "Verheiratet, mit Ehepartner zusammenlebend"],
                                       ["same-sex union", "Eingetragene, gleichgeschlechtliche Partnerschaft zusammenlebend"],
                                       ["distance marriage", "Verheiratet, dauernd getrennt lebend"],
                                       ["distance same-sex union", "Eingetragene, gleichgeschlechtliche Partnerschaft getrennt lebend"],
                                       ["single", "Ledig, war nie verheiratet"],
                                       ["divorced", "Geschieden / eingetragene, gleichgeschlechtliche Partnerschaft aufgehoben"],
                                       ["widowed", "Verwitwet / Lebenspartner/-in aus eingetragener, gleichgeschlechtlicher Partnerschaft verstorben"]
                                   ],
                                   widget=widgets.RadioSelect)

    Kids=models.IntegerField(doc="Respondent's number of children",
                             label="Haben Sie Kinder? Wenn ja, wie viele?",
                             blank=True,
                             initial=0)

    Income = models.IntegerField(doc="Respondent's income",
                                 label="Welches monatliche Budget haben Sie zur Verfügung? Bitte geben Sie Ihr monatliches Nettoeinkommen an.",
                                 choices=[
                                     [0, "0-500 €"],
                                     [1, "501-1.000 €"],
                                     [2, "1.001-2.000 €"],
                                     [3, "2.001-3.000 €"],
                                     [4, "3.001-4.000 €"],
                                     [5, "mehr als 4.000 €"],
                                     [9999, "keine Angabe"]
                                 ],
                                 blank=True,
                                 widget=widgets.RadioSelect)

    ZIP=models.StringField(doc="Respondent's ZIP Code",
                           label="Von wo füllen Sie die Studie aus? Bitte geben Sie Ihre Postleitzahl an",
                           blank=True)

    # Domain questions
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
                                    [3, "Mehrmals wöchentlich"],
                                    [2, "Wöchentlich"],
                                    [1, "Seltener"],
                                    [0, "Nie"]
                                ],
                                widget=widgets.RadioSelect)

    Temp = models.IntegerField(doc="Current temperature in Respondent's location",
                               label="Wie viel °C beträgt die Außentemperatur in Ihrer Umgebung jetzt gerade?")

    # see https://doi.org/10.1177/1077699015606057
    Accuracy = models.IntegerField(doc="Respondent's assessment of message's accuracy",
                                   label="Ich halte die Aussage für akkurat.",
                                   choices=[
                                       [0, ""],
                                       [1, ""],
                                       [2, ""],
                                       [3, ""],
                                       [4, ""]
                                   ],
                                   widget=widgets.RadioSelectHorizontal)

    Credibility = models.IntegerField(doc="Respondent's assessment of message's credibility",
                                      label="Ich halte die Aussage für glaubwürdig.",
                                      choices=[
                                          [0, ""],
                                          [1, ""],
                                          [2, ""],
                                          [3, ""],
                                          [4, ""]
                                      ],
                                      widget=widgets.RadioSelectHorizontal)

    # CLICCS common questions
    CLICCS1 = models.LongStringField(doc="CLICCS' common question #1",
                                     label="Was sehen Sie als größte Herausforderung in Bezug auf ein sich wandelndes Klima?",
                                     blank = True)
    CLICCS2 = models.LongStringField(doc="CLICCS' common question #2",
                                     label="Wie gehen Sie damit um?",
                                     blank = True)

    # other
    openText = models.LongStringField(doc="Suggestions, Questions,...",
                                      label="Haben Sie Fragen oder Anmerkungen?",
                                      blank=True)

    # Risk
    Risk_General = models.IntegerField(doc="Respondent's general risk self-assessment",
                                   label="Sind Sie generell eine Person, die voll und ganz bereit ist, Risiken einzugehen, oder versuchen Sie, Risiken zu vermeiden?",
                                   choices=[
                                       [0, ""],
                                       [1, ""],
                                       [2, ""],
                                       [3, ""],
                                       [4, ""],
                                       [5, ""],
                                       [6, ""],
                                       [7, ""],
                                       [8, ""],
                                       [9, ""],
                                       [10, ""]
                                   ],
                                   widget=widgets.RadioSelectHorizontal)

    Risk_Weather = models.IntegerField(doc="Respondent's weather related risk self-assessment",
                                       label="In der Wettervorhersage wird schlechtes Wetter angekündigt. Sind Sie generell eine Person, die voll und ganz bereit ist, trotz angekündigten schlechten Wetters Risiken einzugehen (zum Beispiel, indem Sie ohne Regenschirm das Haus verlassen), oder versuchen Sie, die Risiken zu vermeiden?",
                                       choices=[
                                           [0, ""],
                                           [1, ""],
                                           [2, ""],
                                           [3, ""],
                                           [4, ""],
                                           [5, ""],
                                           [6, ""],
                                           [7, ""],
                                           [8, ""],
                                           [9, ""],
                                           [10, ""]
                                       ],
                                       widget=widgets.RadioSelectHorizontal)
