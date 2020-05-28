from codewatchman.watchman import watchman
from codewatchman.watchmanlog import watchmanlog

instance = watchman(tokenId="sHltDBIyEcXoJB1o3Kbb", accessToken="3fbaca5d18c81590694822")
print("Validation Status", instance.is_validated, instance.validation_message)

first_log = watchmanlog("This is a test log", { "test": True })

instance.send_log(first_log)

print("This is to let you konw that the script is complete.")