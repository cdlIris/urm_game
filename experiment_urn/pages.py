from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class IntroQ(Page):
    form_fields = ['free_Q', 'quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'quiz7', 'quiz8', 'quiz9', 'quiz10']
    form_model = models.Player

    def vars_for_template(self):
        self.subsession.draw_balls()
        ball_lst = self.player.participant.vars['6balls']
        self.player.flip_coin() # flip the virtual coin
        red = 0
        black = 0
        chart = None
        if self.round_number <= 10:
            chart = 'intro_part/case1.png'
        if 11 <= self.round_number <= 20:
            chart = 'intro_part/case2.png'
        if 21 <= self.round_number <= 30:
            chart  = 'intro_part/case3.png'
        if self.round_number >= 31:
            chart = 'intro_part/case4.png'

        for i in range(0,6):
            if ball_lst[i] == 'red':
                red += 1
            else:
                black += 1
            ball_lst[i] = 'background:' + ball_lst[i] + ';'
        return {
            'balls_num': range(0, 6),
            'ball_lst1': ball_lst[0:3],
            'ball_lst2': ball_lst[3:6],
            'red': red,
            'black': black,
            'round_num': self.round_number,
            'chart': chart

        }


class GuessColor(Page):
    form_model = models.Player
    form_fields = ['guess_color']

    def vars_for_template(self):
        ball_lst = self.player.participant.vars['6balls']
        self.player.flip_coin()
        Q_message = self.player.set_payoff()
        self.player.participant.vars['payoff'].append(self.player.payoff)

        return {
            'balls_num': range(0, 6),
            'ball_lst1': ball_lst[0:3],
            'ball_lst2': ball_lst[3:6],
            'round_num': self.round_number,
            'Q_message': Q_message
        }


class Results(Page):
    def is_displayed(self):
        return self.round_number in [10,20,30,40]

    def vars_for_template(self):
        return {
            'case': self.round_number/10
        }


page_sequence = [
    IntroQ,
    GuessColor,
    Results
]
