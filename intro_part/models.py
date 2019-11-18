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
    computer_id = models.StringField(label="Please enter your computer number:")
    free_Q = models.StringField(choices=["Yes", "No"], widget=widgets.RadioSelectHorizontal,
                                label="Before you guess which urn is used, do you want to know Q?")

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
        choices=[('A', "Drawing two balls of different color is more likely in the “High Q” urn."),
                 ('B', "Drawing two balls of different color is more likely in the “Low Q” urn.")],
        label="Which statement is true?", widget=widgets.RadioSelect)
    correct_q3 = models.StringField()
    Q4 = models.StringField(
        choices=[('A', "It is more likely that these six balls have been drawn from the “High Q” urn."),
                 ('B', "It is more likely that these six balls have been drawn from the “Low Q” urn.")],
        label="Which statement is true?", widget=widgets.RadioSelect)
    correct_q4 = models.StringField()
    Q5 = models.StringField(
        choices=[('A', "It is more likely that these six balls have been drawn from the “High Q” urn."),
                 ('B', "It is more likely that these six balls have been drawn from the “Low Q” urn.")],
        label="Which statement is true?", widget=widgets.RadioSelect)
    correct_q5 = models.StringField()
    Q6 = models.StringField(
        choices=["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"],
        label="Given information in the picture above, before seeing any ball drawings what is the probability of a red urn?",
        widget=widgets.RadioSelect)
    correct_q6 = models.StringField()

    def set_payoff(self):
        self.payoff = 0
        if self.correct_q1:
            self.payoff += 20
        if self.correct_q2:
            self.payoff += 20
        if self.correct_q3:
            self.payoff += 20
        if self.correct_q4:
            self.payoff += 20
        if self.correct_q5:
            self.payoff += 20


