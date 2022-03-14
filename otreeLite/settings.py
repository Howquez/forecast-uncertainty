from os import environ

SESSION_CONFIGS = [
    dict(
        name="Baillon",
        display_name="Baillon",
        num_demo_participants=1,
        app_sequence=["Intro", "Baillon", "Outro"],
        location="random",
        treatment="random",
    ),
    dict(
        name="English_Baillon",
        display_name="Baillon",
        num_demo_participants=1,
        app_sequence=["EN1_Intro", "EN2_Baillon", "EN3_Outro"],
        location="random",
        treatment="random",
    ),
]

ROOMS = [
    dict(
        name="Baillon",
        display_name="Baillon",
        participant_label_file="_rooms/test.txt"
    ),
    dict(
        name="noLabel",
        display_name="noLabel"
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=2.00, doc=""
)

PARTICIPANT_FIELDS = ["location",
                      "treatment",
                      "observed_temp",
                      "winning_event",

                      "event_sequence",
                      "round_to_pay",
                      "pivotal_lottery",
                      "pivotal_draw",
                      "pivotal_lottery",
                      "lottery_success",
                      "bet_success",
                      "baillon_ticks",
                      "payment_event",
                      "pivotal_matching_probability",
                      "mechanism"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "EUR"
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = environ.get('OTREE_SECRET_KEY')
# SECRET_KEY = '6414986324531'
