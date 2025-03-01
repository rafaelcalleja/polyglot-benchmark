from abc import ABC, abstractmethod


class Handler(ABC):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class SanitizerHandler(Handler):
    def handle(self, request):
        cleaned = request.translate(str.maketrans('', '', '!@#$%^&*()'))
        return super().handle(cleaned) if cleaned != request else None


class ValidatorHandler(Handler):
    def handle(self, request):
        if request.isalnum():
            return request
        return super().handle(request)


class LoggerHandler(Handler):
    def handle(self, request):
        print(f"Processing: {request}")
        return super().handle(request) if self._next_handler else request
