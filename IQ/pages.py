from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class Q1(Page):
    form_model = models.Player
    form_fields = ['q1']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['1']

    def vars_for_template(self):
        return {
            'pics_src': '1.png',
            'index': self.participant.vars['task_rounds']['1']
        }

    def before_next_page(self):
        if self.player.q1 == Constants.ans[0]:
            self.player.participant.vars['n_correct'] += 1

class Q2(Page):
    form_model = models.Player
    form_fields = ['q2']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['2']

    def vars_for_template(self):
        return {
            'pics_src': '2.png',
            'index': self.participant.vars['task_rounds']['2']
        }

    def before_next_page(self):
        if self.player.q2 == Constants.ans[1]:
            self.player.participant.vars['n_correct'] += 1

class Q3(Page):
    form_model = models.Player
    form_fields = ['q3']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['3']

    def vars_for_template(self):
        return {
            'pics_src': '3.png',
            'index': self.participant.vars['task_rounds']['3']
        }

    def before_next_page(self):
        if self.player.q3 == Constants.ans[2]:
            self.player.participant.vars['n_correct'] += 1

class Q4(Page):
    form_model = models.Player
    form_fields = ['q4']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['4']

    def vars_for_template(self):
        return {
            'pics_src': '4.png',
            'index': self.participant.vars['task_rounds']['4']
        }

    def before_next_page(self):
        if self.player.q4 == Constants.ans[3]:
            self.player.participant.vars['n_correct'] += 1

class Q5(Page):
    form_model = models.Player
    form_fields = ['q5']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['5']

    def vars_for_template(self):
        return {
            'pics_src': '5.png',
            'index': self.participant.vars['task_rounds']['5']
        }

    def before_next_page(self):
        if self.player.q5 == Constants.ans[4]:
            self.player.participant.vars['n_correct'] += 1

class Q6(Page):
    form_model = models.Player
    form_fields = ['q6']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['6']

    def vars_for_template(self):
        return {
            'pics_src': '6.png',
            'index': self.participant.vars['task_rounds']['6']
        }

    def before_next_page(self):
        if self.player.q6 == Constants.ans[5]:
            self.player.participant.vars['n_correct'] += 1


class Q7(Page):
    form_model = models.Player
    form_fields = ['q7']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['7']

    def vars_for_template(self):
        return {
            'pics_src': '7.png',
            'index': self.participant.vars['task_rounds']['7']
        }

    def before_next_page(self):
        if self.player.q7 == Constants.ans[6]:
            self.player.participant.vars['n_correct'] += 1


class Q8(Page):
    form_model = models.Player
    form_fields = ['q8']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['8']

    def vars_for_template(self):
        return {
            'pics_src': '8.png',
            'index': self.participant.vars['task_rounds']['8']
        }

    def before_next_page(self):
        if self.player.q8 == Constants.ans[7]:
            self.player.participant.vars['n_correct'] += 1

class Q9(Page):
    form_model = models.Player
    form_fields = ['q9']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['9']

    def vars_for_template(self):
        return {
            'pics_src': '9.png',
            'index': self.participant.vars['task_rounds']['9']
        }

    def before_next_page(self):
        if self.player.q9 == Constants.ans[8]:
            self.player.participant.vars['n_correct'] += 1


class Q10(Page):
    form_model = models.Player
    form_fields = ['q10']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['10']

    def vars_for_template(self):
        return {
            'pics_src': '10.png',
            'index': self.participant.vars['task_rounds']['10']
        }

    def before_next_page(self):
        if self.player.q10 == Constants.ans[9]:
            self.player.participant.vars['n_correct'] += 1


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.n_correct = self.player.participant.vars['n_correct']
        return {
            'correct': self.player.participant.vars['n_correct']
        }


class IntroIQ(Page):
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [
    IntroIQ,
    Q1,
    Q2,
    Q2,
    Q3,
    Q4,
    Q5,
    Q6,
    Q7,
    Q8,
    Q9,
    Q10,
    Results
]
