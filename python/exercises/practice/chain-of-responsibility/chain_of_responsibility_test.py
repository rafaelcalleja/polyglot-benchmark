import unittest
from chain_of_responsibility import SanitizerHandler, ValidatorHandler, LoggerHandler


class ChainOfResponsibilityTest(unittest.TestCase):
    def setUp(self):
        self.chain = SanitizerHandler()
        self.chain.set_next(ValidatorHandler()).set_next(LoggerHandler())
    
    def test_full_processing(self):
        test_cases = [
            ("Hello!123", "Hello123"),
            ("Invalid@Data", None),
            ("CleanData", "CleanData")
        ]
        
        for input_data, expected in test_cases:
            with self.subTest(input=input_data):
                result = self.chain.handle(input_data)
                self.assertEqual(result, expected)
    
    def test_sanitizer_handler(self):
        sanitizer = SanitizerHandler()
        result = sanitizer.handle("Test!@#")
        self.assertIsNone(result)  # No next handler, returns None
        
        # Test with next handler
        sanitizer.set_next(LoggerHandler())
        result = sanitizer.handle("Test!@#")
        self.assertEqual(result, "Test")
    
    def test_validator_handler(self):
        validator = ValidatorHandler()
        
        # Valid input
        result = validator.handle("Test123")
        self.assertEqual(result, "Test123")
        
        # Invalid input with no next handler
        result = validator.handle("Test@123")
        self.assertIsNone(result)
        
        # Invalid input with next handler
        validator.set_next(LoggerHandler())
        result = validator.handle("Test@123")
        self.assertIsNone(result)
    
    def test_logger_handler(self):
        logger = LoggerHandler()
        result = logger.handle("TestData")
        self.assertEqual(result, "TestData")
        
        # Test with next handler
        next_handler = ValidatorHandler()
        logger.set_next(next_handler)
        result = logger.handle("TestData")
        self.assertEqual(result, "TestData")
