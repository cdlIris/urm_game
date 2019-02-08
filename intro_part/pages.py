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
    form_fields = ['Q1']
    form_model = models.Player


class Q2(Page):
    form_fields = ['Q2']
    form_model = models.Player

class Q3(Page):
    form_fields = ['Q3']
    form_model = models.Player

class Q4(Page):
    form_fields = ['Q4']
    form_model = models.Player

class Q5(Page):
    form_fields = ['Q5']
    form_model = models.Player

page_sequence = [
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
    Q5
]
