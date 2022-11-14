from aioredis import from_url
from redis_websocket_api import WebsocketServer, WebsocketHandler


class PublishEverythingHandler(WebsocketHandler):

    def channel_is_allowed(self, channel_name):
        return True


WebsocketServer(
    redis=from_url("redis://localhost/:6379", encoding="utf-8", decode_responses=True),
    # read_timeout=30,
    # keep_alive_timeout=120,
    handler_class=PublishEverythingHandler,
).listen(
    host='0.0.0.0',
    port=8766,
    channel_patterns=["*"],
)