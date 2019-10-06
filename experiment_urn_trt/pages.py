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
        (red, black, lst) = self.player.draw()
        self.player.flip_coin() # flip the virtual coin
        pic = 'intro_part_trt/control_' + str(self.player.cur_case) + '.jpg'
        self.player.red = red
        return {
            'balls_num': range(0, 6),
            'ball_lst1': lst[0:3],
            'ball_lst2': lst[3:6],
            'red': red,
            'black': black,
            'round_num': self.round_number,
            'pic': pic

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
