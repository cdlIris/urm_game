from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Danlin Chen'

doc = """
Instruction and example round 
"""


class Constants(BaseConstants):
    name_in_url = 'intro_part_trt'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    free_Q = models.StringField(choices=["Yes", "No"], widget=widgets.RadioSelectHorizontal,
                                label="Before you guess which urn is used, do you want to know Q if this information is free?")

    color = models.StringField(choices=['Red', 'Black'], widget=widgets.RadioSelectHorizontal,
                               label= "Please guess, which urn is used in this round?")

    Q1 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,
                            label="Is it possible that these six balls have been drawn from this urn?")