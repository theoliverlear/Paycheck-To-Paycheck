import logging
from typing import Generic, TypeVar, override

from channels.generic.websocket import AsyncWebsocketConsumer

T = TypeVar("T")

class WebSocketConsumer(AsyncWebsocketConsumer, Generic[T]):

    @override
    async def connect(self) -> None:
        logging.info("WebSocket connected")
        await self.accept()

    @override
    async def disconnect(self, code) -> None:
        logging.info("WebSocket disconnected")

    @override
    async def receive(self, text_data=None, bytes_data=None) -> None:
        pass
