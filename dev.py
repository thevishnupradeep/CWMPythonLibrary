import asyncio
from codewatchman.Watchman import Watchman
from codewatchman.WatchmanLog import WatchmanLog

import logging
logging.basicConfig(level=logging.DEBUG)

tokenData = { "tokenId": "VfY4BJJgE2vgeFbuM576", "accessToken": "4c9538bbfbd21592196292212" }
instance = Watchman(tokenData["tokenId"], tokenData["accessToken"])

first_log = WatchmanLog(log_code="TESTLOG", message="IT IS WORKING!!!!!", payload={ "test": True })
instance.send_log(first_log)
print("This is to let you know that the script is complete.")