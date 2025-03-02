import unittest
from document_processor import DocumentProcessor

class TestDocumentProcessor(unittest.TestCase):
    def test_full_processing(self):
        doc = DocumentProcessor("Parties: ABC Corp and XYZ Ltd [Confidential Terms]")
        doc.process()
        
        self.assertIn("CONFIDENTIAL", doc.metadata['watermark'])
        self.assertTrue(doc.content.startswith("ENCRYPTED::"))
    
    def test_invalid_document(self):
        doc = DocumentProcessor("Simple agreement")
        with self.assertRaises(ValueError):
            doc.process()
