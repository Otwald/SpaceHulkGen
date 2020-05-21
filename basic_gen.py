class Basic:

    def __init__(self, size, level, option):
        self.init = {'size': size, 'level': level, 'option': option}

    def mainLoop(self):
        self.checkInit()

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
