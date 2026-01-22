from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from project.settings import SQUADRON_MIN_LEVEL, SQUADRON_MAX_LEVEL

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    class Meta:
        abstract = True


class MemberClass(TimeStampedModel):
    name = models.CharField(max_length=16, verbose_name="Class Name")
    shorthand = models.CharField(max_length=3, verbose_name="Class Shorthand")


class Race(TimeStampedModel):
    name = models.CharField(max_length=16, verbose_name="Race Name")


class SquadronMember(TimeStampedModel):
    name = models.CharField(max_length=32, verbose_name="Name")
    physical_stat = models.IntegerField(verbose_name="Physical Stat")
    mental_stat = models.IntegerField(verbose_name="Mental Stat")
    tactical_stat = models.IntegerField(verbose_name="Tactical Stat")
    member_class = models.ForeignKey(MemberClass, on_delete=models.PROTECT, verbose_name="Class")
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Race")
    chemistry = models.TextField(verbose_name="Chemistry")
    level = models.IntegerField(
        default=1, 
        validators= [
            MinValueValidator(SQUADRON_MIN_LEVEL),
            MaxValueValidator(SQUADRON_MAX_LEVEL)
        ],
        help_text=f"Level can only be between {SQUADRON_MIN_LEVEL} and {SQUADRON_MAX_LEVEL}"
    )

    def __str__(self) -> str:
        return "Squadron Member # {0}, {1}, with {2}/{3}/{4} stats, {5} class.".format(
            self.pk, 
            self.name,
            self.physical_stat,
            self.mental_stat,
            self.tactical_stat,
            self.member_class
            )

class SquadronMissionType(TimeStampedModel):
    title = models.TextField(verbose_name="Title")
    reward = models.TextField(verbose_name="Reward")

    def __str__(self):
        return f"I am mission type titled '{self.title}' and my reward is '{self.reward}'."

class SquadronMission(TimeStampedModel):
    class SuccessChance(models.IntegerChoices):
        LOW = 0, 'There is little chances that this mission will succeed...'
        RISKY = 1, 'This mission will test the squadron to its limits. Are the risks worth the reward?'
        CHALLENGING = 2, 'This mission will be challenging, but I think our squadron is equal to the task!'
        BOUND = 3, 'This mission is bound to succeed!'

    mission_type = models.ForeignKey(SquadronMissionType, on_delete=models.PROTECT)
    success_chance_message = models.IntegerField(
        choices=SuccessChance.choices,
        default=SuccessChance.LOW,
        verbose_name="Success Chance Message"
    )
    required_physical = models.IntegerField(verbose_name="Required Physical Stat")
    required_mental = models.IntegerField(verbose_name="Required Mental Stat")
    required_tactical = models.IntegerField(verbose_name="Required Tactical Stat")

    def __str__(self):
        return f"I am mission with title '{self.mission_type.title}', and I require {self.required_physical}/{self.required_mental}/{self.required_tactical}. My rewards are: {self.mission_type.reward}"