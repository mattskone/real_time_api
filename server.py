"""A simple key/value store websocket API."""

import tornado.websocket

from handler import MessageHandler


class SocketHandler(tornado.websocket.WebSocketHandler):

    def __init__(self, *args, **kwargs):
        self.message_handler = MessageHandler()
        super().__init__(*args, **kwargs)

    def check_origin(self, origin):
        return True

    def open(self):
        self.write_message('hello')

    def on_message(self, msg):
        try:
            self.write_message(self.message_handler.handle_message(msg))
        except Exception as e:
            self.write_message(str(e))

def make_app():
    return tornado.web.Application([
        (r'/connect', SocketHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

