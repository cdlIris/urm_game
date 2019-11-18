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
            self.player.set_payoff()

        else:
            self.player.correct_q1 = 'False'
        self.player.participant.vars['comprehension'] = self.player.payoff


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
    Example,
    ExperimentStart,
    Q1
]
