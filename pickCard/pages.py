from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class PickCard(Page):
    form_model = models.Player
    form_fields = ['believe1', 'scale1', 'believe2', 'scale2']

    def vars_for_template(self):
        return {
            'msg': self.player.content
        }


class Results(Page):
    pass


class PickSelect(Page):
    pass


class Intro(Page):
    def vars_for_template(self):
        self.player.set_k()
        msgs = self.player.get_msg()
        self.player.content = msgs[self.player.card_content()]


page_sequence = [
    Intro,
    PickSelect,
    PickCard,
    Results
]
