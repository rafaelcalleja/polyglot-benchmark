from abc import ABC, abstractmethod

class Handler(ABC):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler
        
    @abstractmethod
    def handle(self, email):
        if self._next_handler:
            return self._next_handler.handle(email)
        return email

class SpamHandler(Handler):
    def handle(self, email):
        cleaned = email.replace("cheap", "").replace("pills", "")
        return super().handle(cleaned) if cleaned != email else "SPAM_REMOVED"

class ValidatorHandler(Handler):
    def handle(self, email):
        return super().handle(email) if "@" in email else "INVALID_EMAIL"
        
class DisclaimerHandler(Handler):
    def handle(self, email):
        return super().handle(email + " [DISCLAIMER]")
        
class LoggerHandler(Handler):
    def handle(self, email):
        # In a real system, we would log the email here
        return super().handle(email)

class EmailProcessor:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_handler(self, handler):
        if not self.head:
            self.head = handler
            self.tail = handler
        else:
            self.tail.set_next(handler)
            self.tail = handler
        return self
        
    def process(self, email):
        if not self.head:
            return email
        return self.head.handle(email)
