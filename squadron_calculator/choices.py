""" 
Conditions:
        When accompanying:
                Class-wise:
                        a class
                        someone of same class
                        someone of different class
                        not of same class
                        3 or more squadrons of the same class
                        all squadron members diff class
                Race-wise:
                        a race
                        someone of same race
                        someone of different race
                        not of same race
                        3 or more members same race
                        all squadron diff race
        When:
                An active squadron member
                at or above a duty's recommended level
                above level 50
Bonus:
        3%
        5%
        10%
        15%
        20%
        30%
        40%
        50%
        to all? boolean

Reward:
        Stats:
                a stat bonus (Physical, Mental, Tactical)
                exp
        Misc:
                + party chemistry trigger rates
                (Items:)
                Contemporary Warfare:
                        Offence
                        Defense
                        Magics
                Materia:
                        DoH
                        DoL
                        DoM
                        tank
                        physical DPS
                Crystal Clusters
                (Currency:)
                Gatherers' scrips
                Crafters' scrips
                Extra Company Seals
                MGP
                Gil
        Priority:
                0 - 5 Scale


"""
from django.db import models


class RewardType(models.TextChoices):
        PHYSICAL = "PHYSICAL", "Physical"
        MENTAL = "MENTAL", "Mental"
        TACTICS = "TACTICS", "Tactics"
        EXPERIENCE = "EXPERIENCE", "Experience"
        INCREASED_CHEMISTRY_TRIGGER_RATE = "INCREASED_CHEMISTRY_TRIGGER_RATE", "Increased chemistry trigger rate"
        CONTEMPORARY_WARFARE_OFFENCE = "CONTEMPORARY_WARFARE_OFFENCE", "Contemporary Warfare: Offence"
        CONTEMPORARY_WARFARE_DEFENSE = "CONTEMPORARY_WARFARE_DEFENSE", "Contemporary Warfare: Defense"
        CONTEMPORARY_WARFARE_MAGICS = "CONTEMPORARY_WARFARE_MAGICS", "Contemporary Warfare: Magics"
        DOH_MATERIA = "DOH_MATERIA", "DoH materia"
        DOL_MATERIA = "DOL_MATERIA", "DoL materia"
        DOM_MATERIA = "DOM_MATERIA", "DoM materia"
        TANK_MATERIA = "TANK_MATERIA", "Tank materia"
        PHYSICAL_DPS_MATERIA = "PHYSICAL_DPS_MATERIA", "Physical DPS materia"
        CRYSTAL_CLUSTERS = "CRYSTAL_CLUSTERS", "Crystal clusters"
        GATHERERS_SCRIPS = "GATHERERS_SCRIPS", "Gatherers' scrips"
        CRAFTERS_SCRIPS = "CRAFTERS_SCRIPS", "Crafter Scrips"
        COMPANY_SEALS = "COMPANY_SEALS", "Company Seals"
        MGP = "MGP", "MGP"
        GIL = "GIL", "Gil"

class SuccessChance(models.IntegerChoices):
        LOW = 0, 'There is little Chances that this mission will succeed...'
        RISKY = 1, 'This mission will test the squadron to its limits. Are the risks worth the reward?'
        CHALLENGING = 2, 'This mission will be challenging, but I think our squadron is equal to the task!'
        BOUND = 3, 'This mission is bound to succeed!'


class ConditionProc(models.TextChoices):
        accompanying_arcanist = "ACCOMPANYING ARCANIST", "Accompanying an Arcanist"
        accompanying_archer = "ACCOMPANYING ARCHER", "Accompanying an Archer"
        accompanying_conjurer = "ACCOMPANYING CONJURER", "Accompanying a Conjurer"
        accompanying_gladiator = "ACCOMPANYING GLADIATOR", "Accompanying a Gladiator"
        accompanying_lancer = "ACCOMPANYING LANCER", "Accompanying a Lancer"
        accompanying_marauder = "ACCOMPANYING MARAUDER", "Accompanying a Marauder"
        accompanying_pugilist = "ACCOMPANYING PUGILIST", "Accompanying a Pugilist"
        accompanying_rogue = "ACCOMPANYING ROGUE", "Accompanying a Rogue"
        accompanying_thaumaturge = "ACCOMPANYING THAUMATURGE", "Accompanying a Thaumaturge"
        accompanying_same_class = "ACCOMPANYING SAME CLASS", "Accompanying someone of the same class"
        accompanying_diff_class = "ACCOMPANYING DIFF CLASS", "Accompanying someone of a different class"
        not_accompanying_same_class = "NOT ACCOMPANYING SAME CLASS", "Not accompanying someone of the same class"
        three_or_more_same_class = "3 OR MORE SAME CLASS", "3 or more squadrom members are of the same class"
        all_diff_class = "ALL DIFF CLASS", "All squadron members are of a differnet class"
        accompanying_au_ra = "ACCOMPANYING AU RA", "Accompanying an Au Ra"
        accompanying_elezen = "ACCOMPANYING ELEZEN", "Accompanying an Elezen"
        accompanying_hyur = "ACCOMPANYING HYUR", "Accompanying a Hyur"
        accompanying_lalafell = "ACCOMPANYING LALAFELL", "Accompanying a Lalafell"
        accompanying_miqote = "ACCOMPANYING MIQOTE", "Accompanying a Miqo'te"
        accompanying_roegadyn = "ACCOMPANYING ROEGADYN", "Accompanying a Roegadyn"
        accompanying_same_race = "ACCOMPANYING SAME RACE", "Accompanying someone of the same race"
        accompanying_diff_race = "ACCOMPANYING DIFF RACE", "Accompanying someone of a different race"
        not_accompanying_same_race = "NOT ACCOMPANYING SAME RACE", "Not accompanying someone of the same race"
        three_or_more_same_race = "3 OR MORE SAME RACE", "3 or more squadron members are of the same race"
        all_diff_race = "ALL DIFF RACE", "All squadron members are of a different race"
        active = "ACTIVE", "An active squadron member"
        at_or_above_level = "AT OR ABOVE LEVEL", "At or above a duty's recommended level"
        over_50 = "OVER 50", "Above level 50"


class Bonus(models.IntegerChoices):
        three = 3, "3%"
        five = 5, "5%"
        ten = 10, "10%"
        fifteen = 15, "15%"
        twenty = 20, "20%"
        thirty = 30, "30%"
        fourty = 40, "40%"
        fifty = 50, "50%"

class ChemistryRewards(models.TextChoices):
        physical = "PHYSICAL", "Physical"
        mental = "MENTAL", "Mental"
        tactical = "TACTICAL", "Tactical"
        exp = "EXP", "Experience"
        increased_rates = "INCREASED RATES", "Increased party chemistry trigger rates"
        warfare_offence = "WARFARE OFFENCE", "Chance to receive Contemporary Warfare: Offence"
        warfare_defense = "WARFARE DEFENSE", "Chance to receive Contemporary Warfare: Defence"
        warfare_magics = "WARFARE MAGICS", "Chance to receive Contemporary Warfare: Magics"
        doh_materia = "DOH MATERIA", "Chance to receive DoH-specific materia"
        dol_materia = "DOL MATERIA", "Chance to receive DoL-specific materia"
        dom_materia = "DOM MATERIA", "Chance to receive DoM-specific materia"
        tank_materia = "TANK MATERIA", "Chance to receive tank-specific materia"
        physical_DPS_materia = "PHYSICAL DPS MATERIA", "Chance to receive physical DPS-specific materia"
        crystal_clusters = "CRYSTAL CLUSTERS", "Chance to receive crystal clusters"
        gatherers_scrips = "GATHERERS SCRIPS", "Chance to receive gatherers' scrips"
        crafters_scrips = "CRAFTERS SCRIPS", "Chance to receive crafters' scrips"
        seals = "SEALS", "Chance to receive bonus company seals"
        mgp = "MGP", "Chance to receive bonus MGP"
        gil = "GIL", "Chance to receive bonus gil"
