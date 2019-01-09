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
    guess_color = models.StringField(choices=['red', 'black'], widget=widgets.RadioSelect,
                                     label="Please guess, which urn is used in this round?")
    Q_value = models.FloatField()
    true_color = models.StringField()
    cur_case = models.IntegerField()

    def flip_coin(self):
        self.Q_value = self.participant.vars['Q_lst'][self.round_number-1]
        self.true_color = self.participant.vars['color_lst'][self.round_number-1][0]

    def set_payoff(self):
        self.payoff = Constants.endowment
        if self.round_number == 1:
            self.participant.vars['payoff'] = []

        return ''

    def select_color(self, case):  # red urn / black urn
        Urn_prob = Constants.cases[case][0]
        draw = random.random()
        color = 0
        if draw <= 1 - Urn_prob:
            color = 1
        col_order = ['red', 'black']
        if color == 1:
            col_order.reverse()
        # print("cur_color_prob: ", Urn_prob, 'order: ', color, ' color: ', col_order[0])
        return col_order

    def draw_balls(self):
        if self.round_number == 1:
            self.participant.vars['Q_lst'] = []
            self.participant.vars['color_lst'] = []

        cur_blk = 0

        if 11 <= self.round_number <= 20:
            cur_blk = 1
        if 21 <= self.round_number <= 30:
            cur_blk = 2
        if 31 <= self.round_number <= 40:
            cur_blk = 3

        self.cur_case = self.participant.vars['case_lst'][cur_blk]
        # print("round: ", self.round_number, 'cur_case: ', self.cur_case)
        color = self.select_color(self.cur_case - 1)
        Q = Constants.cases[self.cur_case-1][1]

        balls_lst = []  # draw 6 balls with replacement
        for i in range(0, 6):
            balls_lst.append(np.random.choice(np.array(color), p=[Q, 1 - Q]))

        self.participant.vars['6balls'] = balls_lst
        self.participant.vars['Q_lst'].append(Q)
        self.participant.vars['color_lst'].append([color[0]])