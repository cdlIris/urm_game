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
    gender = models.StringField(choices=['Female', 'Male'], label="What is your gender?", widget=widgets.RadioSelect)
    gender_other= models.StringField(label="other(Please specify) ", blank=True)
    student = models.StringField(choices=["Full time","Part time (less than the normal full time course load)","Non-student"],
                                 label="3.What is your student status?")
    edu_level = models.StringField(label="4.What is the highest level of study that you have completed? (Use your current year in school if you are a student.)",
                                   choices=['High school or lower','Undergraduate 1st year','Undergraduate 2nd year',
                                            'Undergraduate 3rd year','Undergraduate 4th year','Graduate 1st year','Graduate 2nd year',
                                            'Graduate 3 or more years'], widget=widgets.RadioSelect)
    major = models.StringField(label="5.Which of the following best describes your current major course of study? (Check more than one option if you are a double major or if your undergraduate and graduate majors differ. For non-students, use the major for the highest year of school completed.)",
                               choices=['No Major or Pre-College',
                                        'Arts/Humanities/Education',
                                        'Business/Management (including MBA)',
                                        'Economics',
                                        'Politics',
                                        'Psychology',
                                        'Other Social Sciences',
                                        'Law School (but not pre-law)',
                                        'Medical/Nursing (but not pre-med)',
                                        'Math/Engineering/Computer Science/Science'],
                               widget=widgets.RadioSelect)
    major_other = models.StringField(label="other(Please specify)", blank=True)
    math_course = models.IntegerField(label="6.How many college-level mathematics courses have you taken")
    econ_course = models.IntegerField(label="7.How many college-level economics courses have you taken?")

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

    def set_payoff(self):
        self.payoff = 0
        self.payoff = self.n_correct * Constants.prize
