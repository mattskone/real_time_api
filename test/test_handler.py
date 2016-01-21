import unittest

import handler


class HandlerTest(unittest.TestCase):

    def setUp(self):
        self.h = handler.MessageHandler()

    def test_handle_message_get(self):
        self.assertEqual(self.h.handle_message('get foo'), 'foo')
        with self.assertRaises(ValueError):
            self.h.handle_message('get foo bar')

    def test_handle_message_set(self):
        self.assertEqual(self.h.handle_message('set foo bar'), 'ok')
        with self.assertRaises(ValueError):
            self.h.handle_message('set')
            self.h.handle_message('set foo')

    def test_handle_message_invalid_command(self):
        with self.assertRaises(ValueError):
            self.h.handle_message('')
            self.h.handle_message('foo')

