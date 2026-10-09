from typing import Any
from squadron_calculator import models
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        classes = (
            ('Gladiator', 'GLA'),
            ('Marauder', 'MRD'),
            ('Pugilist', 'PGL'),
            ('Lancer', 'LNC'),
            ('Archer', 'ARC'),
            ('Rogue', 'ROG'),
            ('Conjurer', 'CNJ'),
            ('Thaumaturge', 'THM'),
            ('Arcanist', 'ACN')
        )
        for tuple in classes:
            new_class = models.MemberClass(name=tuple[0], shorthand=tuple[1])
            new_class.save()
        races = (
            'Hyur',
            'Elezen',
            'Lalafell',
            "Miqo'te",
            'Roegadyn', 
            'Au Ra',
            'Viera',
            'Hrothgar'
        )
        for name in races:
            new_race = models.Race(name=name)
            new_race.save()

        missions = (
            ('Allied Maneuvers', '1 Squadron Enlistment Manual'),
            ('Pest Eradication', '1 Squadron Enlistment Manual'),
            ('Imposter Alert', '10 Priority Aetheryte Passes'),
            ('Invasive Testing', '10 Squadron Gear Maintenance Manuals'),       
            ('Armor Annihilation', '10 Squadron Rationing Manuals'),
            ('Voidsent Elimination', '10 Squadron Spiritbonding Manuals'),     
            ('Cult Crackdown', '10 Squadron Engineering Manuals'),
            ('Outlaw Subjugation', '10 Squadron Survival Manuals'),
            ('Infiltrate and Rescue', '10 Squadron Battle Manuals'),
            ('Counter-magitek Exercises', '10 Gold Saucer VIP Cards'),
            ('Primal Recon', '10 Priority Seal Allowances'),
            ('Chimerical Elimination', '5 Priority Aetheryte Passes'),
            ('Supply Wagon Destruction', '5 Squadron Gear Maintenance Manuals'),
            ('Criminal Pursuit', '5 Rationing Manuals'),
            ('Supply Line Disruption', '5 Squadron Rationing Manuals'),
            ('Imperial Feint', '5 Squadron Spiritbonding Manuals'),
            ('Imperial Pursuit', '5 Squadron Survival Manuals'),
            ('Imperial Recon', '5 Squadron Battle Manuals'),
            ('Black Market Crackdown', '5 Gold Saucer VIP Cards'),
            ('Stronghold Assault', '5 Priority Seal Allowances'),
        )
        for mission_tuple in missions:
            new_mission = models.SquadronMissionType(title=mission_tuple[0], reward=mission_tuple[1])
            new_mission.save()