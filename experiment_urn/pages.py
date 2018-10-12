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
        ball_lst = self.player.participant.vars['20balls']
        self.player.flip_coin() # flip the virtual coin
        red = 0
        black = 0
        for i in range(0,20):
            if ball_lst[i] == 'red':
                red += 1
            else:
                black += 1
            ball_lst[i] = 'background:' + ball_lst[i] + ';'
        return {
            'balls_num': range(0, 20),
            'ball_lst1': ball_lst[0:5],
            'ball_lst2': ball_lst[5:10],
            'ball_lst3': ball_lst[10:15],
            'ball_lst4': ball_lst[15:],
            'red': red,
            'black': black,
            'round_num': self.round_number,

        }


class GuessColor(Page):
    form_model = models.Player
    form_fields = ['guess_color']

    def vars_for_template(self):
        ball_lst = self.player.participant.vars['20balls']
        self.player.flip_coin()
        Q_message = self.player.set_payoff()
        self.player.participant.vars['payoff'].append(self.player.payoff)

        return {
            'balls_num': range(0, 20),
            'ball_lst1': ball_lst[0:5],
            'ball_lst2': ball_lst[5:10],
            'ball_lst3': ball_lst[10:15],
            'ball_lst4': ball_lst[15:],
            'round_num': self.round_number,
            'Q_message': Q_message
        }
class Results(Page):
    pass


page_sequence = [
    IntroQ,
    GuessColor
]
