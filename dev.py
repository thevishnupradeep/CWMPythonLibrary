from codewatchman.watchman import watchman
instance = watchman(tokenId="19UYyGqfVWWNX8uiA5o9", accessToken="a44e75c6e4e01590564553")
print("Validation Status", instance.is_validated, instance.validation_message)