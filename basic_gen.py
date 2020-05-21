import random
from database import difficulty, objectiv, calamity, ca_en_diff, encounter
from database import hull


class Basic:

    def __init__(self, size, level, option):
        self.init = {'size': size, 'level': level, 'option': option}
        random.seed()

    def mainLoop(self):
        # try:
        self.checkInit()
        self.scale, self.diff = self.getScale(self.init['level'])
        self.obj = random.randint(0, 5)
        self.hulltypes = self.getHull(self.scale)
        self.cal = self.getBlock(self.diff, self.hulltypes)
        self.enc = self.getBlock(self.diff, self.hulltypes)
        print(self.enc)
        # except RuntimeError as err:
        # print(err)

    def getBlock(self, diff, hull) -> list:
        """builds an dict of blockers 
        """
        out = {}
        for types in hull:
            block = random.randint(0, diff)
            if block < 2:
                block = 2
            x = 0
            temp = []
            while x < block:
                x += 1
                diff, vers = self.getThreat(self.diff)
                temp.append(
                    {"threat": diff, "version": vers})
            out[types] = temp
        return out

    def getThreat(self, diff):
        """does a check on table 4-4 and 4-3
        """
        roll = random.randint(1, 5) + diff
        return [(roll-1)//3, roll % 3]

    def getHull(self, scale) -> list:
        """a huge switch case to determine the Hulltypes
        """
        x = 0
        out = []
        while x < ((scale//5)+1):
            roll = random.randint(1, 100)
            if(1 <= roll <= 40):
                out.append(0)
            elif (41 <= roll <= 55):
                out.append(1)
            elif (56 <= roll <= 70):
                out.append(2)
            elif (71 <= roll <= 80):
                out.append(3)
            elif (81 <= roll <= 86):
                out.append(4)
            elif (87 <= roll <= 92):
                out.append(5)
            elif (93 <= roll <= 97):
                out.append(6)
            elif (98 <= roll <= 99):
                out.append(7)
            else:
                out.append(8)
            x += 1
        return out

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
        return [scale, diff]

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
