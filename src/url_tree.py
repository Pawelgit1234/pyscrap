
class UrlTree:
    def __init__(self, deepness: int, parent: 'UrlTree'):
        self.deepness = deepness
        self.parent = parent
