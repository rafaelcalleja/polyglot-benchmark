import unittest
from typing import Dict, Optional
from order_validator import Order, OrderValidator
from chain_handler import Handler
from order_handlers import (
    InventoryValidator, TaxCalculator, PromotionApplier,
    PaymentProcessor, InventoryUpdater, OrderConfirmationSender,
    create_order_processing_chain
)

class OrderValidatorTest(unittest.TestCase):

    def test_basic_order_processing(self):
        """Test basic order processing with no promo or region"""
        # Arrange
        order = Order(
            order_id="12345",
            customer_id="customer1",
            items={"item1": 2, "item2": 1},
            total=100.0
        )
        validator = OrderValidator()
        
        # Act
        processed_order = validator.process_order(order)
        
        # Assert
        self.assertEqual(processed_order.total, 100.0)
        self.assertTrue(processed_order.validated)

    def test_eu_region_tax_calculation(self):
        """Test order with EU region applies correct tax"""
        # Arrange
        order = Order(
            order_id="12346",
            customer_id="customer2",
            items={"item1": 1},
            total=100.0,
            region="EU"
        )
        validator = OrderValidator()
        
        # Act
        processed_order = validator.process_order(order)
        
        # Assert
        self.assertEqual(processed_order.total, 121.0)  # 21% VAT
        self.assertTrue(processed_order.validated)

    def test_us_region_tax_calculation(self):
        """Test order with US region applies correct tax"""
        # Arrange
        order = Order(
            order_id="12347",
            customer_id="customer3",
            items={"item1": 1},
            total=100.0,
            region="US"
        )
        validator = OrderValidator()
        
        # Act
        processed_order = validator.process_order(order)
        
        # Assert
        self.assertEqual(processed_order.total, 108.0)  # 8% sales tax
        self.assertTrue(processed_order.validated)

    def test_promo_code_discount(self):
        """Test order with valid promo code applies discount"""
        # Arrange
        order = Order(
            order_id="12348",
            customer_id="customer4",
            items={"item1": 1},
            total=100.0,
            promo_code="SUMMER23"
        )
        validator = OrderValidator()
        
        # Act
        processed_order = validator.process_order(order)
        
        # Assert
        self.assertEqual(processed_order.total, 90.0)  # 10% discount
        self.assertTrue(processed_order.validated)

    def test_multiple_handlers(self):
        """Test order with multiple handlers processes completely"""
        # Arrange
        order = Order(
            order_id="12349",
            customer_id="customer5",
            items={"item1": 2, "item2": 3},
            total=100.0,
            region="EU",
            promo_code="SUMMER23"
        )
        validator = OrderValidator()
        
        # Act
        processed_order = validator.process_order(order)
        
        # Assert
        # First applies 21% VAT, then 10% discount: 100 * 1.21 * 0.9 = 108.9
        self.assertAlmostEqual(processed_order.total, 108.9, places=1)
        self.assertTrue(processed_order.validated)

    def test_refactor_preparation(self):
        """Test large class implementation can be refactored to chain"""
        # This test is a placeholder to verify the behavior before and after refactoring
        # Students will implement the Chain of Responsibility pattern but maintain
        # the same behavior
        order = Order(
            order_id="12350",
            customer_id="customer6",
            items={"item1": 1, "item2": 1},
            total=100.0,
            region="US",
            promo_code="WELCOME"
        )
        validator = OrderValidator()
        
        processed_order = validator.process_order(order)
        
        # 100 * 1.08 (US tax) * 0.85 (WELCOME discount) = 91.8
        self.assertAlmostEqual(processed_order.total, 91.8, places=1)
        self.assertTrue(processed_order.validated)
        
    def test_chain_implementation(self):
        """Test that the chain of responsibility implementation works correctly"""
        # Create an order
        order = Order(
            order_id="12351",
            customer_id="customer7",
            items={"item1": 2, "item2": 1},
            total=100.0,
            region="EU",
            promo_code="SUMMER23"
        )
        
        # Get the chain
        chain = create_order_processing_chain()
        
        # Process through chain
        processed_order = chain.handle(order)
        
        # 100 * 1.21 (EU tax) * 0.9 (SUMMER23 discount) = 108.9
        self.assertAlmostEqual(processed_order.total, 108.9, places=1)
        self.assertTrue(processed_order.validated)
        
    def test_individual_handlers(self):
        """Test that individual handlers work correctly"""
        # Create an order
        order = Order(
            order_id="12352",
            customer_id="customer8",
            items={"item1": 1},
            total=100.0
        )
        
        # Test tax calculator
        tax_calculator = TaxCalculator()
        order.region = "US"
        order = tax_calculator.handle(order)
        self.assertEqual(order.total, 108.0)
        
        # Test promotion applier
        promotion_applier = PromotionApplier()
        order.promo_code = "WELCOME"
        order = promotion_applier.handle(order)
        self.assertEqual(order.total, 108.0 * 0.85)
        
    def test_all_individual_handlers(self):
        """Test each handler individually to ensure 100% coverage"""
        order = Order(
            order_id="12353",
            customer_id="customer9",
            items={"item1": 2, "item2": 3},
            total=100.0,
            region="EU",
            promo_code="SUMMER23"
        )
        
        # Test inventory validator
        inventory_validator = InventoryValidator()
        processed = inventory_validator.handle(order)
        self.assertEqual(processed.total, 100.0)
        
        # Test payment processor
        payment_processor = PaymentProcessor()
        processed = payment_processor.handle(order)
        self.assertEqual(processed.total, 100.0)
        
        # Test inventory updater
        inventory_updater = InventoryUpdater()
        processed = inventory_updater.handle(order)
        self.assertEqual(processed.total, 100.0)
        
        # Test order confirmation sender
        confirmation_sender = OrderConfirmationSender()
        processed = confirmation_sender.handle(order)
        self.assertEqual(processed.total, 100.0)
        self.assertTrue(processed.validated)
        
    def test_handler_chain_building(self):
        """Test the creation and linking of the handler chain"""
        chain = create_order_processing_chain()
        
        # Verify the chain is correctly built by checking the type of first handler
        self.assertIsInstance(chain, InventoryValidator)
        
        # Process an order to verify the complete chain works
        order = Order(
            order_id="12354",
            customer_id="customer10",
            items={"item1": 1},
            total=100.0,
            region="US",
            promo_code="WELCOME"
        )
        
        processed_order = chain.handle(order)
        self.assertAlmostEqual(processed_order.total, 91.8, places=1)
        self.assertTrue(processed_order.validated)


if __name__ == "__main__":
    unittest.main()
