from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random

class PickCard(Page):
    form_model = models.Player
    form_fields = ['believe1', 'scale1', 'believe2', 'scale2']

    def vars_for_template(self):
        return {
            'msg': self.player.content
        }


class PickSelect(Page):
    pass


class Intro(Page):
    def vars_for_template(self):
        self.player.set_k()
        msgs = self.player.get_msg()
        self.player.content = msgs[self.player.card_content()]


class FinalResult(Page):
    def vars_for_template(self):
        # random.shuffle(self.player.participant.vars['payoff'])
        chosen_round = self.player.participant.vars['chosen_round']
        urn = self.player.participant.vars['payoff'][chosen_round]
        comprehension = round(float(self.player.participant.vars['comprehension']), 1)
        urn = round(float(urn) * self.session.config['real_world_currency_per_point'],1)
        IQ = round(float(self.player.participant.vars['IQ']) * self.session.config['real_world_currency_per_point'], 1)
        self.player.final_payoff = round(urn + IQ + Constants.show_up + comprehension, 1)
        return {
            'Urn': urn,
            'IQ': IQ,
            'show_up': Constants.show_up,
            'comprehension': comprehension,
            'total': urn + IQ + Constants.show_up + comprehension
        }

page_sequence = [
    Intro,
    PickSelect,
    PickCard,
    FinalResult
]
