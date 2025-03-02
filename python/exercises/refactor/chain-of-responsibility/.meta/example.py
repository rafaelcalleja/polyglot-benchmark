from abc import ABC, abstractmethod

class DocumentHandler(ABC):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, document):
        if self._next_handler:
            self._next_handler.handle(document)

class SanitizationHandler(DocumentHandler):
    def handle(self, document):
        document.content = document.content.translate(str.maketrans('', '', '!@#$%^&*()'))
        super().handle(document)

class ValidationHandler(DocumentHandler):
    def handle(self, document):
        if "parties" not in document.content.lower():
            raise ValueError("Invalid contract structure")
        super().handle(document)

class WatermarkHandler(DocumentHandler):
    def handle(self, document):
        document.metadata['watermark'] = "CONFIDENTIAL"
        super().handle(document)

class EncryptionHandler(DocumentHandler):
    def handle(self, document):
        if "confidential" in document.content.lower():
            document.content = f"ENCRYPTED::{document.content}::ENCRYPTED"
        super().handle(document)

class StorageHandler(DocumentHandler):
    def handle(self, document):
        print(f"Saving to S3: {document.content[:50]}...")
        print(f"Archiving to DB: {document.metadata}")

class DocumentProcessor:
    def __init__(self, content):
        self.content = content
        self.metadata = {}
        
    def process(self):
        sanitizer = SanitizationHandler()
        validator = ValidationHandler()
        watermark = WatermarkHandler()
        encryptor = EncryptionHandler()
        storage = StorageHandler()

        sanitizer.set_next(validator).set_next(watermark).set_next(encryptor).set_next(storage)
        sanitizer.handle(self)
