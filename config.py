import os

from dotenv import load_dotenv

load_dotenv()

context = os.getenv('context', 'bstack')
bstack_userName = os.getenv('bstack_userName', os.getenv('bstack_userName'))
bstack_accessKey = os.getenv('bstack_accessKey', os.getenv('bstack_accessKey'))