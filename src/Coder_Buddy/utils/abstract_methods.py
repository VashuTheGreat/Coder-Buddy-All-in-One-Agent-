
from abc import abstractmethod,ABC


class Pipeline(ABC):
    def __init__(self):
        super().__init__()

    async def initiate(self):
        pass    