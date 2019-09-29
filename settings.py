from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.033,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
       'name': 'Urn_Game',
       'display_name': "Urn_Game",
       'num_demo_participants': 2,
       'app_sequence': ['intro_part','experiment_urn','IQ','pickCard'],
    },
    {
       'name': 'Urn_Game_trt',
       'display_name': "Urn_Game_trt",
       'num_demo_participants': 2,
       'app_sequence': ['intro_part_trt','experiment_urn_trt','IQ','pickCard'],
    },
    {
       'name': 'urn',
       'display_name': "urn",
       'num_demo_participants': 1,
       'app_sequence': ['experiment_urn'],
    },
    {
       'name': 'pickCard',
       'display_name': "PickCard",
       'num_demo_participants': 1,
       'app_sequence': ['pickCard'],
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
POINTS_DECIMAL_PLACES = 0
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2
USE_POINTS = True


ROOMS = [
    {
        'name': 'Urn_Game',
        'display_name': 'Urn_Game',
    }
]

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = '1-bui4%2&9sy6h$c3^s7s(itc*ndeomuzukr(79zn3z^k1_9sw'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
