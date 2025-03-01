import unittest
from chain_of_responsibility_2 import SpamHandler, ValidatorHandler, DisclaimerHandler, LoggerHandler, EmailProcessor

class EmailProcessorTest(unittest.TestCase):
    def test_spam_detection(self):
        processor = EmailProcessor()
        processor.add_handler(SpamHandler())
        processor.add_handler(ValidatorHandler())
        result = processor.process("Buy cheap pills!")
        self.assertEqual(result, "SPAM_REMOVED")

    def test_valid_email_flow(self):
        processor = EmailProcessor()
        processor.add_handler(DisclaimerHandler())
        processor.add_handler(LoggerHandler())
        result = processor.process("Hello Team!")
        self.assertEqual(result, "Hello Team! [DISCLAIMER]")
