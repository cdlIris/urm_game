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
    Urn_set = [[0.8, 0.2], [0.6, 0.4]]
    cases = [[0.8, [0.7, 0.6]],[0.8, [0.9, 0.6]], [0.6, [0.7, 0.5]], [0.6, [0.9, 0.5]]]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['charge'] = []
                p.participant.vars['case_lst'] = [1,2,3,4]
                random.shuffle(p.participant.vars['case_lst'])
                random.seed()
                p.participant.vars['chosen_round'] = random.randint(1, Constants.num_rounds)
                p.draw_balls()
                for i in range(0, Constants.num_rounds):
                    p.participant.vars['charge'].append(random.randint(0, 100))



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_red = models.IntegerField()
    free_Q = models.StringField(choices=["Yes", "No"], widget=widgets.RadioSelect,
                                label="Before you guess which urn is used, do you want to know Q?")


    guess_color = models.StringField(choices=['red', 'black'], widget=widgets.RadioSelect,
                                     label="Please guess, which urn is used in this round?")

    coin_value = models.IntegerField()
    Q_value = models.FloatField()
    charge = models.IntegerField()
    true_color = models.StringField()
    cur_case = models.IntegerField()
    Q_known = models.IntegerField()
    Urn_color = models.StringField()

    quiz0 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect, blank=True)
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

    StrategyQ_1 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal)
    StrategyQ_2 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal,
                                      label="1 red balls and 5 black balls are drawn.")
    StrategyQ_3 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal,
                                      label="2 red balls and 4 black balls are drawn.")
    StrategyQ_4 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal,
                                      label="3 red balls and 3 black balls are drawn.")
    StrategyQ_5 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal,
                                      label="4 red balls and 2 black balls are drawn.")
    StrategyQ_6 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal,
                                      label="5 red balls and 1 black balls are drawn.")
    StrategyQ_7 = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal,
                                      label="6 red balls and 0 black balls are drawn.")

    q1 = models.StringField(label='You decided sometimes to pay for information about Q when it’s not free. What were your reasons?')
    q2 = models.StringField(label="Sometimes you decided not to obtain information about Q even for free. What were your reasons?")


    def flip_coin(self):
        self.coin_value = random.randint(0, 1) # 0 not free, 1 free
        self.participant.vars['if_free_Q'] = self.coin_value # if see the value free
        self.Q_value = self.participant.vars['Q_lst'][self.round_number-1]
        self.true_color = self.participant.vars['color_lst'][self.round_number-1][0]

    def set_payoff(self):
        self.payoff = Constants.endowment
        self.charge = self.participant.vars['charge'][self.round_number - 1]
        message = 'The value of Q is ' + str(int(self.Q_value*10))
        if self.round_number == 1:
            self.participant.vars['payoff'] = []
        if self.free_Q == 'No': # not see Q
            self.payoff = Constants.endowment
            return ''
        if self.free_Q == 'Yes' and self.charge == 0: # see Q free
            self.payoff = Constants.endowment
            if self.quiz0 == 'Yes':
                return 'The value of Q is ' + str(int(self.Q_value*10))
            else:
                return 'Sorry. You can not see the vlaue of Q.'
        if self.free_Q == 'Yes' and self.charge != 0: # see Q not free
            choice_lst = [self.quiz1, self.quiz2, self.quiz3, self.quiz4, self.quiz5, self.quiz6, self.quiz7, self.quiz8,
                          self.quiz9, self.quiz10]
            if self.charge <= 10:
                if 'Yes' in choice_lst:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 10 < self.charge <= 20:
                if 'Yes' in choice_lst[1:]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 20 < self.charge <= 30:
                if 'Yes' in choice_lst[2:]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 30 < self.charge <= 40:
                if 'Yes' in choice_lst[3:]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 40 < self.charge <= 50:
                if 'Yes' in choice_lst[4:]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 50 < self.charge <= 60:
                if 'Yes' in choice_lst[5:]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 60 < self.charge <= 70:
                if 'Yes' in choice_lst[6:]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 70 < self.charge <= 80:
                if 'Yes' in choice_lst[7:]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 80 < self.charge <= 90:
                if 'Yes' in choice_lst[8:]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            if 90 < self.charge <= 100:
                if 'Yes' in choice_lst[9]:
                    self.payoff -= self.charge
                    self.Q_known = 1
                    return message
            self.Q_known = 0
            return 'Sorry. You can not see the value of Q. Because you did not pay the price.'
        return ''

    def select_Q(self,case):
        cur_q = np.random.choice(np.arange(0, 2), p=[0.5, 0.5])  # 0 the first rate, 1 the second rate
        return Constants.cases[case][1][cur_q]

    def select_color(self, case):  # red urn / black urn
        # 1. prob of red urn
        Urn_prob = Constants.cases[case][0]
        # 2. get which color to draw, if 0 then red, if 1 then black
        draw = ['red'] * int(Urn_prob*10) + ['black'] * int((1-Urn_prob)*10)
        random.shuffle(draw)
        col_order = ['red', 'black']
        if draw[0] == 'black':
            col_order.reverse()
        return col_order

    def draw_balls(self):
        self.participant.vars['Q_lst'] = []
        self.participant.vars['color_lst'] = []
        self.participant.vars['ball_lsts'] = []
        self.participant.vars['color_orders'] = []
        self.participant.vars['Q_s'] = []

        for i in range(0, Constants.num_rounds):
            # 1. get current block (round block)
            cur_blk = int(i/10)
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
        self.Urn_color = self.participant.vars['color_orders'][self.round_number - 1]
        self.Q_value = self.participant.vars['Q_s'][self.round_number - 1]
        self.participant.vars['Q_lst'].append(self.Q_value)
        self.participant.vars['color_lst'].append(self.Urn_color)
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