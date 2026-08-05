import random
from patterns.factory.factory import AbstractFactory
from entities.enemy import EnemyTypeA, EnemyTypeB, EnemyTypeC

class EnemyFactory(AbstractFactory):
    def create_product(self, x, y):
        enemy_class = random.choice([EnemyTypeA, EnemyTypeB, EnemyTypeC])
        return enemy_class(x, y)

