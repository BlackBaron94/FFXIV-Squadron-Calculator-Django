from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from project.settings import SQUADRON_MIN_LEVEL, SQUADRON_MAX_LEVEL
from .choices import (
    RewardType, 
    SuccessChance,
    ConditionProc,
    Bonus,
    ChemistryRewards
    )

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    class Meta:
        abstract = True


class MemberClass(TimeStampedModel):
    name = models.CharField(max_length=16, verbose_name="Class Name")
    shorthand = models.CharField(max_length=3, verbose_name="Class Shorthand")

    def __str__(self) -> str:
        return self.name


class Race(TimeStampedModel):
    name = models.CharField(max_length=16, verbose_name="Race Name")

    def __str__(self) -> str:
        return self.name


def get_condition(member):
    chemistry = member.chemistry
    condition = "ERROR: All if-blocks failed to parse condition"
    accompanying_string = 'accompanying '
    different_string = 'all squadron members are of a different '
    if not chemistry:
        return None
    if str(chemistry).find(accompanying_string) != -1:
        try:
            after_accompanying = str(chemistry)[(str(chemistry).find(accompanying_string) + len(accompanying_string)):]
            accompanied = after_accompanying[0:after_accompanying.find(',')]
            if accompanied == 'someone of the same class':
                condition = f'With {member.member_class}'
            else:
                accompanied = accompanied[2:].capitalize()
                races = Race.objects.all().values_list('name', flat=True)
                classes = MemberClass.objects.all().values_list('name', flat=True)
                if accompanied in races:
                    condition = f'With {accompanied}'
                elif accompanied in classes:
                    condition = f'With {accompanied}'
                else:
                    condition = 'ERROR: failed to find condition, accompanied check failed'
        except:
            condition = "ERROR: parsing failed with try-except block in 'accompanying' block."
    elif str(chemistry).find(different_string) != 1:
        try:
            after_condition = str(chemistry)[(str(chemistry).find(different_string) + len(different_string)):]
            different_case = after_condition[0:after_condition.find(',')]
            condition = f'Members different {different_case}'
        except:
            condition = "ERROR: parsing failed with try-except block in 'all squadron members' block."
    return condition

def get_percentage(member):
    chemistry = member.chemistry
    search_string = 'there is a '
    if not chemistry:
        return None
    if str(chemistry).find(search_string) != -1:
        percentage = str(chemistry)[(str(chemistry).find(search_string) + len(search_string)):str(chemistry).find('%')] + '%'
    else:
        percentage = None
    return percentage

def get_reward(member):
    chemistry = member.chemistry
    if not chemistry:
        return None
    end = str(chemistry).find('.')
    reward = 'ERROR: Parsing reward failed.'
    if end == -1:
        end = len(chemistry) - 1
    if str(chemistry).find('receive ') != -1:
        reward = str(chemistry)[str(chemistry).find('receive ') + len('receive '):end].capitalize()
    else:
        search_string = 'party chemistry trigger rates increase by '
        trigger_ratio_increase = str(chemistry)[str(chemistry).find(search_string) + len(search_string):-1]
        reward = f'Trigger Rate +{trigger_ratio_increase}'
    return reward
        

class SquadronMember(TimeStampedModel):
    name = models.CharField(max_length=32, verbose_name="Name", unique=True)
    physical_stat = models.IntegerField(verbose_name="Physical Stat")
    mental_stat = models.IntegerField(verbose_name="Mental Stat")
    tactical_stat = models.IntegerField(verbose_name="Tactical Stat")
    member_class = models.ForeignKey(MemberClass, on_delete=models.PROTECT, verbose_name="Class")
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Race")
    chemistry = models.ForeignKey(
        'Chemistry',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Chemistry"
    )
    level = models.IntegerField(
        default=1, 
        validators= [
            MinValueValidator(SQUADRON_MIN_LEVEL),
            MaxValueValidator(SQUADRON_MAX_LEVEL)
        ],
        help_text=f"Level can only be between {SQUADRON_MIN_LEVEL} and {SQUADRON_MAX_LEVEL}"
    )

    def __str__(self) -> str:
        return "Squadron Member '{0}', with {1}/{2}/{3} stats, {4} class, {5} race.".format(
            self.name,
            self.physical_stat,
            self.mental_stat,
            self.tactical_stat,
            self.member_class,
            self.race
            )

    @property
    def chemistry_condition(self):
        if self.chemistry:
            return self.chemistry.get_condition_proc_display()

    @property
    def chemistry_chance(self):
        if self.chemistry:
            return self.chemistry.get_bonus_display()

    @property
    def chemistry_reward(self):
        if self.chemistry:
            return self.chemistry.get_reward_type_display()
        


class SquadronMissionType(TimeStampedModel):
    title = models.TextField(verbose_name="Title")
    reward = models.TextField(verbose_name="Reward")

    def __str__(self):
        return f"{self.title}"

    @property
    def get_details(self):
        return f"I am mission type titled '{self.title}' and my reward is '{self.reward}'."

class SquadronMission(TimeStampedModel):
    mission_type = models.ForeignKey(
        SquadronMissionType, 
        on_delete=models.PROTECT,
        verbose_name="Mission Type"
    )
    success_chance_message = models.IntegerField(
        choices=SuccessChance.choices,
        default=SuccessChance.LOW,
        verbose_name="Success Chance Message"
    )
    required_physical = models.IntegerField(verbose_name="Required Physical Stat")
    required_mental = models.IntegerField(verbose_name="Required Mental Stat")
    required_tactical = models.IntegerField(verbose_name="Required Tactical Stat")
    
    def __str__(self):
        return f"{self.mission_type.title}"

class Chemistry(TimeStampedModel):
    condition_proc = models.CharField(
        verbose_name="Condition that procs chemistry",
        choices=ConditionProc.choices
    )
    bonus = models.IntegerField(
        verbose_name="Percentage",
        choices=Bonus.choices
    )
    to_all = models.BooleanField(
        default=False
    )
    reward_type = models.CharField(
        verbose_name="Rewards for proccing chemistry",
        choices=ChemistryRewards.choices
    )
    priority = models.IntegerField(
        verbose_name="Priority",
        blank=False,
        choices=(
            (0,'0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
        )
    )
    
    def __str__(self):
        return f"When {self.condition_proc} {self.bonus} chance to {self.reward_type}. To all? {self.to_all}. Priority:{self.priority}."


class UserPreference(TimeStampedModel):
    reward_type = models.CharField(choices=RewardType.choices, verbose_name="Preferred Reward")
    ordering = models.PositiveIntegerField(verbose_name="Ordering of preference")

    def __str__(self):
        return f"{self.reward_type} is preferred as #{self.ordering}"