import logging
from typing import Optional
from typing import List
import datetime


class AppLogger(logging.Logger):
    def __init__(self, name: str, handler_types: Optional[List[str]] = ['stream']) -> None:
        super().__init__(name)
        self.name = name
        self.add_handlers(handler_types)

    def add_handlers(self, handler_types: List[str]):
        self.handlers = []
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
        if 'file' in handler_types:
            handler = logging.FileHandler(
                f"app-{self.name}-{datetime.datetime.now().strftime('%Y-%m-%d %H')}.log",
                mode="a",
                encoding="utf-8"
            )
            handler.setFormatter(formatter)
            self.handlers.append(handler)
        if 'stream' in  handler_types:
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            self.handlers.append(handler)
        return self.handlers
