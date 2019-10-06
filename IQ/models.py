from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = """
IQ Test from https://iqpro.org
"""



class Constants(BaseConstants):
    name_in_url = 'IQ'
    players_per_group = None
    num_rounds = 10
    tasks = ['1','2', '3','4', '5','6', '7','8', '9','10']
    ans = [5, 8, 2, 6, 8, 5, 4, 6, 4, 4]
    prize = 10
    time = 20
    show_up = 5

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['n_correct'] = 0
                round_numbers = list(range(1, Constants.num_rounds + 1))
                random.shuffle(round_numbers)
                p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=18,max=100, label="1.What is your age?")
    # gender_female = models.BooleanField()
    gender = models.StringField(choices=["Male", "Female", "Other"], widget=widgets.RadioSelect)
    # gender_other= models.StringField()
    student = models.StringField(choices=["Full time","Part time (less than the normal full time course load)","Non-student"],
                                 label="3.What is your student status?")
    edu_level = models.StringField(label="4.What is the highest level of study that you have completed? (Use your current year in school if you are a student.)",
                                   choices=['High school or lower','Undergraduate 1st year','Undergraduate 2nd year',
                                            'Undergraduate 3rd year','Undergraduate 4th year','Graduate 1st year','Graduate 2nd year',
                                            'Graduate 3 or more years'], widget=widgets.RadioSelect)
    no_major = models.BooleanField(widget=widgets.CheckboxInput)
    arts = models.BooleanField(widget=widgets.CheckboxInput)
    business = models.BooleanField(widget=widgets.CheckboxInput)
    economics = models.BooleanField(widget=widgets.CheckboxInput)
    politics = models.BooleanField(widget=widgets.CheckboxInput)
    psychology = models.BooleanField(widget=widgets.CheckboxInput)
    other_Social_Sciences = models.BooleanField(widget=widgets.CheckboxInput)
    law = models.BooleanField(widget=widgets.CheckboxInput)
    medical = models.BooleanField(widget=widgets.CheckboxInput)
    math = models.BooleanField(widget=widgets.CheckboxInput)


    other = models.StringField(label="other(Please specify)", blank=True)
    math_course = models.StringField()
    econ_course = models.StringField()

    n_correct = models.IntegerField()
    final_real = models.FloatField()
    q1 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    correct_q = models.BooleanField()
    q2 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q3 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q4 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q5 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q6 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q7 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q8 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q9 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                             label="Please answer the question:")
    q10 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8], widget=widgets.RadioSelect,
                              label="Please answer the question:")

