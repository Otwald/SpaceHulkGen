import random
from database import difficulty, objectiv, calamity, ca_en_diff, encounter
from database import hull, enemy


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
        print(self.getEnemyPerHull(self.hulltypes))
        self.block = self.getBlock(self.diff, self.hulltypes)
        # except RuntimeError as err:
        # print(err)

    def getEnemyPerHull(self, hull):
        out = []
        for types in hull:
            roll = self.getEnemyRoll(types, self.diff, self.scale)
            if(1 <= roll <= 25):
                out.append(0)
            elif (26 <= roll <= 50):
                out.append(1)
            elif (51 <= roll <= 60):
                out.append(2)
            elif (61 <= roll <= 70):
                out.append(3)
            elif (71 <= roll <= 90):
                out.append(4)
            elif (91 <= roll <= 110):
                out.append(5)
            elif (111 <= roll <= 120):
                out.append(6)
            elif (121 <= roll <= 130):
                out.append(7)
            else:
                out.append(8)
        return out

    def getEnemyRoll(self, hull, diff, scale):
        roll = random.randint(1, 100)
        if(hull == 4 or hull == 5):
            if(
                roll == 11 or roll == 22 or roll == 33 or roll == 44 or
                roll == 55 or roll == 66 or roll == 77 or roll == 88 or
                roll == 99
            ):
                if(hull == 4):
                    return 30
                else:
                    return 65
        if(diff == 0):
            roll2 = random.randint(1, 100)
            if(roll2 < roll):
                roll = roll2
        elif (diff == 2):
            roll += 20
        elif (diff == 3):
            roll2 = random.randint(1, 100)
            if(roll2 > roll):
                roll = roll2
            roll += 20
        elif (diff == 4):
            roll += 40
        if(scale <= 5):
            roll += 10
        elif (scale >= 11):
            roll -= 10
        if(hull == 6 or hull == 7):
            roll += 20
        return roll

    def getBlock(self, diff, hull) -> list:
        """builds an dict of blockers
        """
        out = {}
        i = 0
        for types in hull:
            block = random.randint(2, (2 + (2 * diff)))
            x = 0
            temp = []
            while x < block:
                x += 1
                grade, vers = self.getThreat(diff)
                temp.append(
                    {"threat": grade, "version": vers})
            out[i] = temp
            i += 1
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
