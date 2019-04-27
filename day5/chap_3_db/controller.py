from chap_3_db.model import Model
from chap_3_db.view import View

class Controller:
    def __init__(self):
        self._m = Model()
        self._v = View()

    def count_members(self):
        m = self._m
        count = m.create_db()

        return count