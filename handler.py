class MessageHandler(object):

    def handle_message(self, msg):
        tokens = msg.split(' ')
        try:
            return getattr(self, tokens[0])(tokens[1:])
        except AttributeError:
            raise ValueError('command "{0}" not recognized'.format(tokens[0]))

    def get(self, tokens):
        if len(tokens) > 1:
            raise ValueError('too many words for "get" (expected "get key")')

        return tokens[0]

    def set(self, tokens):
        if len(tokens) < 2:
            raise ValueError(
                'not enough words for "set" (expected "set key value")'
            )

        return 'ok'

