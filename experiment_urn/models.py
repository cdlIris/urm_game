from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np

author = 'Danlin Chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'experiment_urn'
    players_per_group = None
    num_rounds = 40

    endowment = 100
    ball_set_Q = [[0.7, 0.6], [0.9, 0.6], [0.7, 0.5], [0.9, 0.5]]
    Urn_set = [[0.75, 0.25], [0.6, 0.4]]


class Subsession(BaseSubsession):
    def select_Q(self):
        case = np.random.choice(np.arange(0, 2), p=[0.5, 0.5])  # 0 case 1 (8,2), 1 case 2 (6,4)
        case_selected = None

        if 1 <= self.round_number <= 10:
            case_selected = Constants.ball_set_Q[0][case]
        if 11 <= self.round_number <= 20:
            case_selected = Constants.ball_set_Q[1][case]
        if 21 <= self.round_number <= 30:
            case_selected = Constants.ball_set_Q[2][case]
        if 31 <= self.round_number <= 40:
            case_selected = Constants.ball_set_Q[3][case]

        return case_selected

    def select_color(self):
        Urn_prob = Constants.Urn_set
        if self.round_number <= 10:
            Urn_prob = Urn_prob[0]
        if 10 < self.round_number <= 20:
            Urn_prob = Urn_prob[0]
        if 20 < self.round_number <= 30:
            Urn_prob = Urn_prob[1]
        if 30 < self.round_number <= 40:
            Urn_prob = Urn_prob[1]

        color = np.random.choice(np.arange(0, 2), p=[Urn_prob[0], Urn_prob[1]])  # 0 Red, 1 Black
        col_order = ['red', 'black']
        if color == 1:
            col_order.reverse()

        return col_order

    def draw_balls(self):
        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['Q_lst'] = []
                p.participant.vars['color_lst'] = []

            color = self.select_color()
            Q = self.select_Q()
            balls_lst = [] # draw 20 balls with replacement
            for i in range(0,6):
                balls_lst.append(np.random.choice(np.array(color), p=[Q, 1-Q]))

            p.participant.vars['6balls'] = balls_lst
            p.participant.vars['Q_lst'].append(Q)
            p.participant.vars['color_lst'].append([color[0]])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    free_Q = models.StringField(choices=["Yes", "No"], widget=widgets.RadioSelect,
                                label="Before you guess which urn is used, do you want to know Q if this information "
                                      "is free?")

    guess_color = models.StringField(choices=['Red', 'Black'], widget=widgets.RadioSelect,
                                     label="Please guess, which urn is used in this round?")

    coin_value = models.IntegerField()
    Q_value = models.FloatField()
    charge = models.IntegerField()

    quiz1 = models.StringField(choices=['Yes','No'], widget=widgets.RadioSelect, blank=True)
    quiz2 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)
    quiz3 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)
    quiz4 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)
    quiz5 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)
    quiz6 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)
    quiz7 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)
    quiz8 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)
    quiz9 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)
    quiz10 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect,blank=True)

    def flip_coin(self):
        self.coin_value = random.randint(0, 1) # 0 not free, 1 free
        self.participant.vars['if_free_Q'] = self.coin_value # if see the value free
        self.Q_value = self.participant.vars['Q_lst'][self.round_number-1]

    def set_payoff(self):
        self.charge = 0
        if self.round_number == 1:
            self.participant.vars['payoff'] = []
        if self.free_Q == 'No': # not see Q
            self.payoff = Constants.endowment
            return ''
        if self.free_Q == 'Yes' and self.coin_value == 1: # see Q free
            self.payoff = Constants.endowment
            return 'The value of Q is ' + str(self.Q_value)
        if self.free_Q == 'Yes' and self.coin_value == 0: # see Q not free
            choice_lst = [self.quiz1, self.quiz2, self.quiz3, self.quiz4, self.quiz5, self.quiz6, self.quiz7, self.quiz8,
                          self.quiz9, self.quiz10]
            self.charge = random.randint(0, 100)
            if self.charge <= 10:
                if 'Yes' in choice_lst:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 10 < self.charge <= 20:
                if 'Yes' in choice_lst[1:]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 20 < self.charge <= 30:
                if 'Yes' in choice_lst[2:]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 30 < self.charge <= 40:
                if 'Yes' in choice_lst[3:]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 40 < self.charge <= 50:
                if 'Yes' in choice_lst[4:]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 50 < self.charge <= 60:
                if 'Yes' in choice_lst[5:]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 60 < self.charge <= 70:
                if 'Yes' in choice_lst[6:]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 70 < self.charge <= 80:
                if 'Yes' in choice_lst[7:]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 80 < self.charge <= 90:
                if 'Yes' in choice_lst[8:]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            if 90 < self.charge <= 100:
                if 'Yes' in choice_lst[9]:
                    self.payoff = Constants.endowment - self.charge
                    return 'The value of Q is ' + str(self.Q_value)
            self.payoff = Constants.endowment
            return 'Sorry.You can not see the value of Q. Because you did not pay the price.'
        return ''
