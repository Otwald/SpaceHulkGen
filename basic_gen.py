import random
from database import difficulty


class Basic:

    def __init__(self, size, level, option):
        self.init = {'size': size, 'level': level, 'option': option}
        random.seed()

    def mainLoop(self):
        # try:
        self.checkInit()
        self.scale, self.diff = self.getScale(self.init['level'])
        # except RuntimeError as err:
        # print(err)

    def getScale(self, level: str):
        """uses Pseudo Randomnumbers to determen diffculity and scale
        """
        scale = 0
        if(level == 'n'):
            diff = random.randint(0, 2)
            scale = random.randint((diff+1), (diff + 2))
        if(level == 's'):
            diff = random.randint(0, 4)
            scale = diff+6
        if(level == 'v'):
            diff = random.randint(2, 4)
            scale = 11 + (random.randint(diff-2, diff+1) * (diff-1))
        return [scale, difficulty[diff]]

    def checkInit(self):
        """checks the parameter from the user if correct
        """
        try:
            if(self.init['level'] != 'n' and
                    self.init['level'] != 's' and self.init['level'] != 'v'):
                raise RuntimeError(
                    'Skill Level only Allows "n" "s" "v" as values')
            if(self.init['option'] != 'True' and self.init['option'] != 'False'):
                raise RuntimeError(
                    'Optionals only allow True or False as values')
        except RuntimeError as err:
            print(err)
        finally:
            pass
