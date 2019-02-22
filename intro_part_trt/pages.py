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
    form_fields = ['color']


class Example1(Page):
    form_model = models.Player
    form_fields = ['color']


class ExperimentStart(Page):
    pass


class Q1(Page):
    form_model = models.Player
    form_fields = ['Q1', 'correct_q1']

    def before_next_page(self):
        if self.player.Q1 == 'Yes':
            self.player.correct_q1 = 'True'
            self.player.payoff = 20
        else:
            self.player.correct_q1 = 'False'
        self.player.participant.vars['comprehension'] = self.player.payoff



page_sequence = [
    GeneralInfo,
    Treatment1,
    Treatment1Cont,
    instructionRound,
    Example,
    ExperimentStart,
    Q1
]
