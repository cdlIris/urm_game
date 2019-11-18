from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class GeneralInfo(Page):
    pass


class Treatment1(Page):
    pass


class Treatment1Cont(Page):
    pass


class instructionRound(Page):
    pass


class QQuiz(Page):
    pass


class Example(Page):
    form_model = models.Player
    form_fields = ['free_Q','color']


class Example1(Page):
    form_model = models.Player
    form_fields = ['color']


class ExperimentStart(Page):
    pass


class Q1(Page):
    form_fields = ['Q1', 'correct_q1']
    form_model = models.Player

    def before_next_page(self):
        if self.player.Q1 == 'Yes':
            self.player.correct_q1 = 'True'
        else:
            self.player.correct_q1 = 'False'

class Q2(Page):
    form_fields = ['Q2', 'correct_q2']
    form_model = models.Player

    def before_next_page(self):
        if self.player.Q2 == 'A':
            self.player.correct_q2 = 'True'
        else:
            self.player.correct_q2 = 'False'

class Q3(Page):
    form_fields = ['Q3', 'correct_q3']
    form_model = models.Player

    def before_next_page(self):
        if self.player.Q3 == 'B':
            self.player.correct_q3 = 'True'
        else:
            self.player.correct_q3 = 'False'

class Q4(Page):
    form_fields = ['Q4', 'correct_q4']
    form_model = models.Player

    def before_next_page(self):
        if self.player.Q4 == 'A':
            self.player.correct_q4 = 'True'
        else:
            self.player.correct_q4 = 'False'
class Q5(Page):
    form_fields = ['Q5', 'correct_q5']
    form_model = models.Player

    def before_next_page(self):
        if self.player.Q5 == 'B':
            self.player.correct_q5 = 'True'
        else:
            self.player.correct_q5 = 'False'
        self.player.set_payoff()
        self.player.participant.vars['comprehension'] = self.player.payoff


class Q6(Page):
    form_fields = ['Q6', 'correct_q6']
    form_model = models.Player

    def before_next_page(self):
        if self.player.Q6 == '40%':
            self.player.correct_q6 = 'True'
        else:
            self.player.correct_q6 = 'False'
        self.player.set_payoff()
        self.player.participant.vars['comprehension'] = self.player.payoff


class Round0_Start(Page):
    pass

class Start(Page):
    form_fields = ['computer_id']
    form_model = models.Player
    pass

page_sequence = [
    Start,
    GeneralInfo,
    Treatment1,
    Treatment1Cont,
    instructionRound,
    QQuiz,
    Example,
    ExperimentStart,
    Q1,
    Q2,
    Q3,
    Q4,
    Q5,
    Q6,
    Round0_Start
]
