from dataclasses import dataclass

from skills import Skill, HardShot, FuryPunch


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name='Воин',
    max_health=100,
    max_stamina=10,
    attack=0.3,
    stamina=2,
    armor=10,
    skill=HardShot(),
)


ThiefClass = UnitClass(
    name='Вор',
    max_health=100,
    max_stamina=3,
    attack=0.7,
    stamina=5,
    armor=3,
    skill=FuryPunch(),
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
