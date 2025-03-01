from abc import ABC, abstractmethod


class Handler(ABC):
    """Base handler class for the chain of responsibility pattern."""
    pass


class SanitizerHandler:
    """Handler that sanitizes input by removing special characters."""
    pass


class ValidatorHandler:
    """Handler that validates if the input is in the correct format."""
    pass


class LoggerHandler:
    """Handler that logs the processed request."""
    pass
