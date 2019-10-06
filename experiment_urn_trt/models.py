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
                p.participant.vars['charge'] = []
                p.participant.vars['case_lst'] = [1, 2, 3, 4]
                random.shuffle(p.participant.vars['case_lst'])
                random.seed()
                p.participant.vars['chosen_round'] = random.randint(1, Constants.num_rounds)
                p.draw_balls()
                for i in range(0, Constants.num_rounds):
                    p.participant.vars['charge'].append(random.randint(0, 100))


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

    def select_Q(self,case):
        return Constants.cases[case][1]

    def draw_balls(self):
        self.participant.vars['Q_lst'] = []
        self.participant.vars['color_lst'] = []
        self.participant.vars['ball_lsts'] = []
        self.participant.vars['color_orders'] = []
        self.participant.vars['Q_s'] = []

        for i in range(0, Constants.num_rounds):
            # 1. get current block (round block)
            cur_blk = int(i / 10)
            # 2. get current case by block [1,2,3,4]
            cur_case = self.participant.vars['case_lst'][cur_blk]
            # 3. get color
            color_order = self.select_color(cur_case - 1)
            self.participant.vars['color_orders'].append(color_order[0])
            # 4. get Q
            Q = self.select_Q(cur_case - 1)
            self.participant.vars['Q_s'].append(Q)
            balls_lst = []
            # 5. draw 6 balls with replacement
            for j in range(0, 6):
                balls_lst.append(np.random.choice(np.array(color_order), p=[Q, 1 - Q]))
            self.participant.vars['ball_lsts'].append(balls_lst)

    def draw(self):
        cur_blk = int((self.round_number - 1) / 10)
        self.cur_case = self.participant.vars['case_lst'][cur_blk]
        self.urn_color = self.participant.vars['color_orders'][self.round_number - 1]
        self.Q_value = self.participant.vars['Q_s'][self.round_number - 1]
        self.participant.vars['Q_lst'].append(self.Q_value)
        self.participant.vars['color_lst'].append(self.urn_color)
        ball_lst = self.participant.vars['ball_lsts'][self.round_number - 1]
        new_lst = ball_lst.copy()
        red = 0
        black = 0
        for i in range(0, 6):
            if ball_lst[i] == 'red':
                red += 1
            else:
                black += 1
            new_lst[i] =  'background:' + ball_lst[i] + ';'
        return (red, black, new_lst)