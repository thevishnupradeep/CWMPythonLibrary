class watchmanlog:
    message = None
    payload = None
    isValid = True

    def __init__(self, message, payload):
        self.message = message
        self.payload = payload
        self.validate()

    def validate(self):
        if self.message is None:
            print("Message is required.")
            self.isValid = False
        elif type(self.message) is not str:
            print("Message is required.")
            self.isValid = False

        if self.payload != None:
            if type(self.payload) is not dict:
                print("Payload has to be a python dictionary.")
                self.isValid = False
