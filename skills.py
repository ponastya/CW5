from abc import ABC, abstractmethod


class Skill(ABC):
    def __init__(self):
        self.user = None,
        self.target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self):
        pass

    def _is_stamina_enough(self):
        return self.user.stamina >= self.stamina

    def use(self, user, target):
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name}, но не хватило выносливости."


class FuryPunch(Skill):
    name = 'Свирепый Пинок'
    stamina = 2
    damage = 5

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)

        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику"


class HardShot(Skill):
    name = 'Тяжелый удар'
    stamina = 5
    damage = 15

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)

        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику"