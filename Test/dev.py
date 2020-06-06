import asyncio
from CodeWatchMan.WatchMan import WatchMan
from CodeWatchMan.WatchManLog import WatchManLog

import logging
logging.basicConfig(level=logging.DEBUG)

instance = WatchMan(token_id="MnFmlGAQao5dp3VtKlzF", access_token="ae3db243e56e1591027324")
print("Validation Status", instance.is_validated, instance.validation_message)

first_log = WatchManLog(log_code="TESTLOG", message="IT IS WORKING!!!!!", payload={ "test": True })
instance.send_log(first_log)
print("This is to let you konw that the script is complete.")