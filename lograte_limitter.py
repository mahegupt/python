class Logger:
    def __init__(self):
        # Dictionary to keep track of each message's last printed timestamp
        self.message_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Check if the message has been printed before
        if message in self.message_timestamp:
            # Calculate the time since the last print
            last_print_time = self.message_timestamp[message]
            # Only print if at least 10 seconds have passed
            if timestamp - last_print_time < 10:
                return False
        
        # Update the timestamp and allow printing
        self.message_timestamp[message] = timestamp
        return True

logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))  # returns True
print(logger.shouldPrintMessage(2, "bar"))  # returns True
print(logger.shouldPrintMessage(3, "foo"))  # returns False, "foo" was just printed at timestamp 1
print(logger.shouldPrintMessage(8, "bar"))  # returns False, "bar" was just printed at timestamp 2
print(logger.shouldPrintMessage(10, "foo")) # returns False, "foo" was printed at timestamp 1, needs to wait until timestamp 11
print(logger.shouldPrintMessage(11, "foo")) # returns True, now 10 seconds have passed since timestamp 1


