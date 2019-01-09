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
    form_fields = ['guess_color']
    form_model = models.Player

    def vars_for_template(self):
        self.player.draw_balls()
        ball_lst = self.player.participant.vars['6balls']
        self.player.flip_coin() # flip the virtual coin
        red = 0
        black = 0
        chart = 'intro_part_trt/trt_case' + str(self.player.cur_case) + '.png'

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

    def before_next_page(self):
        self.player.set_payoff()
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


page_sequence = [
    IntroQ,
    Results,

]
