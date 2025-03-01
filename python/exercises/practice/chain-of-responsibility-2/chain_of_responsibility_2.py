from abc import ABC, abstractmethod

class Handler(ABC):
    """Base handler class for the chain of responsibility"""
    
    @abstractmethod
    def set_next(self, handler):
        """Set the next handler in the chain"""
        pass
        
    @abstractmethod
    def handle(self, email):
        """Process the email and/or pass to the next handler"""
        pass

class SpamHandler:
    """Handler that detects and removes spam content"""
    pass

class ValidatorHandler:
    """Handler that validates email format"""
    pass

class DisclaimerHandler:
    """Handler that adds legal disclaimers to emails"""
    pass
    
class LoggerHandler:
    """Handler that logs email processing"""
    pass

class EmailProcessor:
    """Manages the chain of responsibility for email processing"""
    pass
