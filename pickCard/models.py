from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import statistics
import numpy

author = 'Danlin Chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pickCard'
    players_per_group = None
    num_rounds = 1

    show_up = 5

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            list = []
            for p in self.get_players():
                p.participant.vars['n_correct'] = random.randint(0,10)
                list.append(p.participant.vars['n_correct'])
            median = statistics.median(list)
            for p in self.get_players():
                p.participant.vars['median'] = median

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    k = models.IntegerField()
    content = models.StringField()
    believe1 = models.StringField(choices=['Sincere','Random'], widget=widgets.RadioSelect,label="Do you believe that your card was a sincere card or a random card? ")
    believe2 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect, label=" After having observed the statement of your card, do you believe that you have performed better than the median?")
    scale1 = models.IntegerField(widget=widgets.Slider(attrs={'min': '0', 'max':'10'}), label="How sure are you? (Rate on a 10-point scale.)")
    scale2 = models.IntegerField(widget=widgets.Slider(attrs={'min': '0', 'max':'10'}), label="How sure are you? (Rate on a 10-point scale.)")
    final_payoff = models.FloatField()

    def set_k(self):
        self.k = random.randint(5,10)

    def card_content(self):
        if_sincere = numpy.random.choice(numpy.arange(1,3), p=[self.k/10,1-self.k/10]) # 1 sincere, 2 random
        if if_sincere == 1:
            return 0 # True message
        else:
            random_true = random.randint(0,1) # 0: random false, 1:random true
            if random_true == 0:
                return 1 # False message
            else:
                return 0 # True message

    def get_msg(self):
        if self.participant.vars['median'] <= self.participant.vars['n_correct']:
            return ["You performed better than the median","You performed worse than the median "]
        else:
            return ["You performed worse than the median ","You performed better than the median"]