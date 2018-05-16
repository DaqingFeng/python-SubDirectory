
class helloWorld(object):
    """description of class"""
    Descrtion="welcome "

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def getTitle(self, title):
        if title is not None:
            title= self.Descrtion+ title
        return title

