from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Danlin Chen'

doc = """
Instruction and example round 
"""


class Constants(BaseConstants):
    name_in_url = 'intro_part'
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
    correct_q1 = models.StringField()
    Q2 = models.StringField(choices=[("A", "“High Q” urns have more balls of the same color as the urn than “Low Q” urns."),
                                     ("B", "“High Q” urns have fewer balls of the same color as the urn than “Low Q” urns.")],
                            label="Which statement is true?", widget=widgets.RadioSelect)
    correct_q2 = models.StringField()
    Q3 = models.StringField(
        choices=[('A', "Drawing two balls of different color is more likely in the “High Precision” urn."),
                 ('B', "Drawing two balls of different color is more likely in the “Low Precision” urn.")],
        label="Which statement is true?", widget=widgets.RadioSelect)
    correct_q3 = models.StringField()
    Q4 = models.StringField(
        choices=[('A', "It is more likely that these six balls have been drawn from the “High Precision” urn."),
                 ('B', "It is more likely that these six balls have been drawn from the “Low Precision” urn.")],
        label="Which statement is true?", widget=widgets.RadioSelect)
    correct_q4 = models.StringField()
    Q5 = models.StringField(
        choices=[('A', "It is more likely that these six balls have been drawn from the “High Precision” urn."),
                 ('B', "It is more likely that these six balls have been drawn from the “Low Precision” urn.")],
        label="Which statement is true?", widget=widgets.RadioSelect)
    correct_q5 = models.StringField()

