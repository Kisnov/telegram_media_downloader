"""test HookClient"""

import unittest

import pyrogram

from module.app import Application
from module.pyrogram_extension import HookClient


class HookClientTestCase(unittest.TestCase):
    def test_default_config_builds_client(self):
        start_timeout = pyrogram.session.Session.START_TIMEOUT
        self.addCleanup(
            setattr, pyrogram.session.Session, "START_TIMEOUT", start_timeout
        )
        app = Application("", "")

        client = HookClient(
            "test", proxy=app.proxy, start_timeout=app.start_timeout, in_memory=True
        )

        self.assertIsNone(client.proxy)
        self.assertEqual(pyrogram.session.Session.START_TIMEOUT, app.start_timeout)
