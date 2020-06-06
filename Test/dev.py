import asyncio
from codewatchman.Watchman import Watchman
from codewatchman.WatchmanLog import WatchmanLog

import logging
logging.basicConfig(level=logging.DEBUG)

instance = Watchman(token_id="", access_token="")
print("Validation Status", instance.is_validated, instance.validation_message)

first_log = WatchmanLog(log_code="TESTLOG", message="IT IS WORKING!!!!!", payload={ "test": True })
instance.send_log(first_log)
print("This is to let you konw that the script is complete.")