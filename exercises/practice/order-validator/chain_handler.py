from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Generic, final, cast

# Define a generic type for the request object
T = TypeVar('T')

class Handler(Generic[T], ABC):
    """Base handler class for the Chain of Responsibility pattern"""
    
    def __init__(self):
        self._next_handler: Optional['Handler[T]'] = None
    
    def set_next(self, handler: 'Handler[T]') -> 'Handler[T]':
        """
        Set the next handler in the chain

        Args:
            handler: The next handler in the chain

        Returns:
            The next handler, to allow for method chaining
        """
        self._next_handler = handler
        return handler
    
    @final
    def next(self, request: T) -> T:
        """
        Pass the request to the next handler if it exists

        Args:
            request: The request object to be processed

        Returns:
            The processed request object after being handled by the next handler,
            or the original request if there is no next handler
        """
        if self._next_handler:
            return cast(T, self._next_handler.handle(request))
        return request
    
    @abstractmethod
    def handle(self, request: T) -> T:
        """
        Process the request and pass it to the next handler

        Args:
            request: The request object to be processed

        Returns:
            The processed request object
        """
        pass
