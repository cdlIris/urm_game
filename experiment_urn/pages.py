from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class IntroQ(Page):
    form_fields = ['free_Q', 'quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'quiz7', 'quiz8', 'quiz9', 'quiz10']
    form_model = models.Player

    def vars_for_template(self):
        self.player.draw_balls()
        ball_lst = self.player.participant.vars['6balls']
        self.player.flip_coin() # flip the virtual coin
        red = 0
        black = 0
        pic = 'intro_part/Block' + str(self.player.cur_case) + '_unknown.jpg'

        for i in range(0,6):
            if ball_lst[i] == 'red':
                red += 1
            else:
                black += 1
            ball_lst[i] = 'background:' + ball_lst[i] + ';'
        self.player.num_red = red
        return {
            'balls_num': range(0, 6),
            'ball_lst1': ball_lst[0:3],
            'ball_lst2': ball_lst[3:6],
            'red': red,
            'black': black,
            'round_num': self.round_number,
            'pic':pic

        }


class GuessColor(Page):
    form_model = models.Player
    form_fields = ['guess_color']

    def vars_for_template(self):
        ball_lst = self.player.participant.vars['6balls']
        Q_message = self.player.set_payoff()
        pic = 'intro_part/Block' + str(self.player.cur_case) + '_unknown.jpg'
        print("****************************************Q message ", Q_message)
        if self.player.free_Q != 'No':
            if Q_message[0] == 'T':
                if self.player.Q_value == Constants.cases[self.player.cur_case-1][1][0]:
                    pic = 'intro_part/Block' + str(self.player.cur_case) + '_H.jpg'
                else:
                    pic = 'intro_part/Block' + str(self.player.cur_case) + '_L.jpg'

        return {
            'balls_num': range(0, 6),
            'ball_lst1': ball_lst[0:3],
            'ball_lst2': ball_lst[3:6],
            'round_num': self.round_number,
            'Q_message': Q_message,
            'pic':pic
        }

    def before_next_page(self):
        if self.player.true_color == self.player.guess_color:
            self.player.payoff += 100
        self.player.participant.vars['payoff'].append(self.player.payoff)


class Results(Page):
    def is_displayed(self):
        return self.round_number in [10,20,30,40]

    def vars_for_template(self):
        return {
            'case': int(self.round_number/10)
        }


class FinalResult(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class Round0(Page):
    form_fields = ['free_Q', 'quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'quiz7', 'quiz8', 'quiz9', 'quiz10']
    form_model = models.Player
    def is_displayed(self):
        return self.round_number == 1



class Round0_Guess(Page):
    form_model = models.Player
    form_fields = ['guess_color']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        self.player.coin_value = random.randint(0,1)
        Q_random = [0.8, 0.5]
        random.shuffle(Q_random)
        self.player.Q_value = Q_random[0]
        Q_message = self.player.set_payoff()
        Q_pic = 'intro_part/Round0_unknown.jpg'
        self.player.payoff = 0

        if self.player.free_Q != 'No':
            if Q_message[0] == 'T':
                print("before pic ", Q_random[0])
                if Q_random[0] == 0.8:
                    Q_pic = 'intro_part/Round0_H.jpg'
                else:
                    Q_pic = 'intro_part/Round0_L.jpg'

        print("Q_message", Q_message, 'Q_known ', self.player.Q_known, 'Q_random ', Q_random )
        return {
            'balls_num': range(0, 6),
            'round_num': self.round_number,
            'Q_message': Q_message,
            'Q_pic': Q_pic,
        }


class Round0_StrategyQ(Page):
    form_model = models.Player
    form_fields = ['StrategyQ_1','StrategyQ_2','StrategyQ_3','StrategyQ_4','StrategyQ_5','StrategyQ_6','StrategyQ_7']

    def is_displayed(self):
        return self.round_number == 1


class Round_StrategyQ(Page):
    form_model = models.Player
    form_fields = ['StrategyQ_1','StrategyQ_2','StrategyQ_3','StrategyQ_4','StrategyQ_5','StrategyQ_6','StrategyQ_7']

    def is_displayed(self):
        return self.round_number in [10,20,30,40]

    def vars_for_template(self):
        pic = 'intro_part/Block' + str(self.player.cur_case) + '_unknown.jpg'
        return {
            'pic': pic
        }

class Questions(Page):
    form_fields = ['q1','q2']
    form_model = models.Player

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
page_sequence = [
    Round0,
    Round0_Guess,
    Round0_StrategyQ,
    IntroQ,
    GuessColor,
    Round_StrategyQ,
    Results,
    Questions

]
