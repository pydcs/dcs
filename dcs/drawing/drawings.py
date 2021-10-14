from dataclasses import dataclass


@dataclass()
class Drawings:
    def load_from_dict(self, data):
        raise NotImplementedError()

    def dict(self):
        raise NotImplementedError()
