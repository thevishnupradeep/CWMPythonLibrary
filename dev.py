from codewatchman.watchman import watchman
from codewatchman.watchmanlog import watchmanlog

instance = watchman(tokenId="MnFmlGAQao5dp3VtKlzF", accessToken="ae3db243e56e1591027324")
print("Validation Status", instance.is_validated, instance.validation_message)

first_log = watchmanlog("IT IS WORKING!!!!!", { "test": True })

instance.send_log(first_log)

print("This is to let you konw that the script is complete.")