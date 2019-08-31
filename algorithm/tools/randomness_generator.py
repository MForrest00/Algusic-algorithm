import random


class RandomnessGenerator:

    def __init__(self):
        self.seed = random.randint(1, 9999999)
        random.seed(self.seed)
