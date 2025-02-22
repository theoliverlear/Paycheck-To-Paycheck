import logging
from typing import Generic, TypeVar

from channels.generic.websocket import AsyncWebsocketConsumer

T = TypeVar("T")

class WebSocketConsumer(AsyncWebsocketConsumer, Generic[T]):
    async def connect(self) -> None:
        logging.info("WebSocket connected")
        await self.accept()

    async def disconnect(self, code) -> None:
        logging.info("WebSocket disconnected")

    async def receive(self, text_data=None, bytes_data=None) -> None:
        pass
