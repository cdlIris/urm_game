from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = """
IQ Test from https://iqpro.org
"""



class Constants(BaseConstants):
    name_in_url = 'IQ'
    players_per_group = None
    num_rounds = 10
    tasks = ['1','2', '3','4', '5','6', '7','8', '9','10']
    ans = [5, 8, 2, 6, 8, 5, 4, 6, 4, 4]

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['n_correct'] = 0
                round_numbers = list(range(1, Constants.num_rounds + 1))
                random.shuffle(round_numbers)
                p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    n_correct = models.IntegerField()
    q1 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q2 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q3 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q4 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q5 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q6 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q7 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q8 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q9 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q10 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                              label="Please answer the question:")

