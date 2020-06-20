import asyncio
from codewatchman.Watchman import Watchman
from codewatchman.WatchmanLog import WatchmanLog

import logging
logging.basicConfig(level=logging.DEBUG)

tokenData = { "tokenId": "cZX877YbyGxZ7Bj9BCGS", "accessToken": "161d5c6a45841592195389664" }
instance = Watchman(tokenData["tokenId"], tokenData["accessToken"])

first_log = WatchmanLog(log_code="TESTLOG", message="IT IS WORKING!!!!!", payload={ "test": True })
instance.send_log(first_log)
print("This is to let you know that the script is complete.")