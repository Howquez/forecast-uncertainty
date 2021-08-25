from otree.api import *


doc = """
Your app description
"""

# MODELS
class Constants(BaseConstants):
    name_in_url = 'Outro'
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

    Education = models.IntegerField(doc="Respondent's highest educational degree",
                                    label="Bitte wählen Sie den höchsten Bildungsabschluss, den Sie bisher erreicht haben.",
                                    # "Welchen beruflichen Ausbildungsabbschluss haben Sie?",
                                    choices=[
                                        [0, "Schule beendet ohne Abschluss"],
                                        [1, "Noch Schüler"],
                                        [2, "Volks-, Hauptschulabschluss, Quali "],
                                        [3, "Mittlere Reife, Realschul- oder gleichwertiger Abschluss"],
                                        [4, "Abgeschlossene Lehre"],
                                        [5, "Fachabitur, Fachhochschulreife"],
                                        [6, "Abitur, Hochschulreife"],
                                        [7, "Fachhochschul-/Hochschulabschluss"],
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
                                    ["same-sex union",
                                     "Eingetragene, gleichgeschlechtliche Partnerschaft zusammenlebend"],
                                    ["distance marriage", "Verheiratet, dauernd getrennt lebend"],
                                    ["distance same-sex union",
                                     "Eingetragene, gleichgeschlechtliche Partnerschaft getrennt lebend"],
                                    ["single", "Ledig, war nie verheiratet"],
                                    ["divorced",
                                     "Geschieden / eingetragene, gleichgeschlechtliche Partnerschaft aufgehoben"],
                                    ["widowed",
                                     "Verwitwet / Lebenspartner/-in aus eingetragener, gleichgeschlechtlicher Partnerschaft verstorben"]
                                ],
                                widget=widgets.RadioSelect)

    Kids = models.BooleanField(doc="Respondent's number of children",
                               label="Haben Sie Kinder?")

    Income = models.IntegerField(doc="Respondent's income",
                                 label="Welches monatliche Budget haben Sie zur Verfügung? Bitte geben Sie Ihr eigenes monatliches Nettoeinkommen an.",
                                 choices=[
                                     [0, "0-500 €"],
                                     [1, "501-1.000 €"],
                                     [2, "1.001-2.000 €"],
                                     [3, "2.001-3.000 €"],
                                     [4, "3.001-4.000 €"],
                                     [5, "mehr als 4.000 €"],
                                     [99999, "keine Angabe"]
                                 ],
                                 widget=widgets.RadioSelect)

    ZIP = models.StringField(doc="Respondent's ZIP Code",
                             label="Von wo füllen Sie die Studie aus? Bitte geben Sie Ihre Postleitzahl an",
                             blank=True)

    Vac = models.StringField(doc="Vaccination status",
                             label="Wir interessieren uns für das aktuelle Impfgeschehen in Deutschland und bitten Sie Ihren aktuellen Impfstatus (gegen Covid-19) anzugeben:",
                             choices=[
                                 ["yes", "Ich habe mich bereits impfen lassen."],
                                 ["no", "Ich plane mich noch impfen zu lassen."],
                                 ["no interest", "Ich möchte mich nicht impfen."],
                                 ["NA", "Keine Angabe."]
                             ],
                             widget=widgets.RadioSelect)

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
                                     blank=True)
    CLICCS2 = models.LongStringField(doc="CLICCS' common question #2",
                                     label="Wie gehen Sie damit um?",
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


# FUNCTIONS


# PAGES
class Outro_Risk(Page):
    form_model = "player"
    form_fields = ["Risk_General", "Risk_Weather"]

    @staticmethod
    def vars_for_template(self):
        return dict(
            choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )

class Domain_Questions_1(Page):
    form_model = "player"
    form_fields = ["Accuracy", "Credibility"]

    @staticmethod
    def vars_for_template(self):
        return dict(
            choices=[0, 1, 2, 3, 4],
        )

    @staticmethod
    def js_vars(self):
        return dict(
            location=self.participant.vars["location"],
            treatment=self.participant.vars["treatment"],
        )

class Domain_Questions_2(Page):
    form_model = "player"
    form_fields = ["Comprehension", "Usage", "Temp"]

class Demographic_Questions(Page):
    form_model = "player"
    form_fields = ["Age", "Gender", "Family", "Kids", "Education", "Income", "ZIP", "Vac"]

class CLICCS_Questions(Page):
    form_model = "player"
    form_fields = ["CLICCS1", "CLICCS2"]

class Results(Page):
    form_model = "player"

    @staticmethod
    def js_vars(self):
        return dict(
            page="revelation",
            location=self.participant.vars["location"],

            ticks=self.participant.vars["baillon_ticks"],
            event_decision=self.participant.vars["payment_event"],
            enabledLabel=True,
            results=True,
        )

    @staticmethod
    def vars_for_template(self):
        return dict(
            redirect="https://mingle.respondi.com/s/XXXXX/ospe.php3?c_0002=1&return_tic="+self.participant.label,
        )


page_sequence = [Outro_Risk,
                 Domain_Questions_1,
                 Domain_Questions_2,
                 Demographic_Questions,
                 CLICCS_Questions,
                 Results]
