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
    name_in_url = 'experiment_urn_trt'
    players_per_group = None
    num_rounds = 40

    endowment = 100
    ball_set_Q = [[0.7, 0.6], [0.9, 0.6], [0.7, 0.5], [0.9, 0.5]]
    Urn_set = [[0.75, 0.25], [0.6, 0.4]]
    cases = [[0.75, 0.7],[0.75, 0.9], [0.6, 0.7], [0.6, 0.9]]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['case_lst'] = [1,2,3,4]
                random.shuffle(p.participant.vars['case_lst'])
                # print("p ", p.id_in_group, " case lst; ", p.participant.vars['case_lst'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    red = models.IntegerField()
    guess_color = models.StringField(choices=['red', 'black'], widget=widgets.RadioSelect,
                                     label="Please guess, which urn is used in this round?")
    true_color = models.StringField()
    Q_value = models.FloatField()
    cur_case = models.IntegerField()
    urn_color = models.StringField()

    def flip_coin(self):
        self.Q_value = self.participant.vars['Q_lst'][self.round_number-1]
        self.true_color = self.participant.vars['color_lst'][self.round_number-1][0]

    def set_payoff(self):
        self.payoff = Constants.endowment
        if self.round_number == 1:
            self.participant.vars['payoff'] = []

        return ''

    def select_color(self, case):  # red urn / black urn
        # 1. prob of red urn
        Urn_prob = Constants.cases[case][0]
        # 2. get which color to draw, if 0 then red, if 1 then black
        draw = ['red'] * int(Urn_prob * 10) + ['black'] * int((1 - Urn_prob) * 10)
        random.shuffle(draw)
        col_order = ['red', 'black']
        if draw[0] == 'black':
            col_order.reverse()
        return col_order

    def draw_balls(self):
        if self.round_number == 1:
            self.participant.vars['Q_lst'] = []
            self.participant.vars['color_lst'] = []

        # 1. get block
        cur_blk = int((self.round_number - 1)/10)
        # 2. get current case
        self.cur_case = self.participant.vars['case_lst'][cur_blk]
        # 3. get urn color
        color_order = self.select_color(self.cur_case - 1)
        # 4. get Q value
        Q = Constants.cases[self.cur_case-1][1]

        balls_lst = []  # draw 6 balls with replacement
        for i in range(0, 6):
            balls_lst.append(np.random.choice(np.array(color_order), p=[Q, 1 - Q]))

        # 6. record ball list, Q list, color list (player's and session-wide)
        self.urn_color = color_order[0]
        self.Q_value = Q
        self.participant.vars['6balls'] = balls_lst
        self.participant.vars['Q_lst'].append(Q)
        self.participant.vars['color_lst'].append([color_order[0]])