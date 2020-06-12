import asyncio
from codewatchman.Watchman import Watchman
from codewatchman.WatchmanLog import WatchmanLog

import logging
logging.basicConfig(level=logging.DEBUG)

instance = Watchman(token_id="rJ0SGEMNaOsggLEXHAC4", access_token="25fb9f04465b1591893909369")
first_log = WatchmanLog(log_code="TESTLOG", message="IT IS WORKING!!!!!", payload={ "test": True })
instance.send_log(first_log)
print("This is to let you know that the script is complete.")