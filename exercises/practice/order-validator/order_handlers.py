from typing import Dict, Any, Optional, List
from chain_handler import Handler
from order_validator import Order


class InventoryValidator(Handler[Order]):
    """Validates that all items are in stock"""
    
    def handle(self, order: Order) -> Order:
        print(f"Validating inventory for order {order.order_id}")
        # Simulation of inventory validation
        # In a real system, this would check against a database
        
        # Assuming all items are in stock for this example
        return self.next(order)


class TaxCalculator(Handler[Order]):
    """Calculates taxes based on the order's region"""
    
    def handle(self, order: Order) -> Order:
        print(f"Calculating taxes for order {order.order_id}")
        
        if order.region == "EU":
            order.total *= 1.21  # 21% VAT
        elif order.region == "US":
            order.total *= 1.08  # 8% sales tax
        # Other regions could be added here
        
        return self.next(order)


class PromotionApplier(Handler[Order]):
    """Applies promotional discounts if valid promo codes are provided"""
    
    def handle(self, order: Order) -> Order:
        print(f"Checking for promotions on order {order.order_id}")
        
        if order.promo_code == "SUMMER23":
            print("Applying 10% summer discount")
            order.total *= 0.9
        elif order.promo_code == "WELCOME":
            print("Applying 15% welcome discount")
            order.total *= 0.85
        # Other promo codes could be added here
        
        return self.next(order)


class PaymentProcessor(Handler[Order]):
    """Processes payment for the order"""
    
    def handle(self, order: Order) -> Order:
        print(f"Processing payment of ${order.total:.2f} for order {order.order_id}")
        # In a real system, this would interact with a payment gateway
        
        # Simulate successful payment
        return self.next(order)


class InventoryUpdater(Handler[Order]):
    """Updates inventory after successful order processing"""
    
    def handle(self, order: Order) -> Order:
        print(f"Updating inventory for order {order.order_id}")
        # In a real system, this would update a database
        
        for item_id, quantity in order.items.items():
            print(f"Decreasing stock of item {item_id} by {quantity}")
        
        return self.next(order)


class OrderConfirmationSender(Handler[Order]):
    """Sends order confirmation to the customer"""
    
    def handle(self, order: Order) -> Order:
        print(f"Sending order confirmation for order {order.order_id}")
        # In a real system, this would send an email or notification
        
        order.validated = True
        return self.next(order)


def create_order_processing_chain() -> Handler[Order]:
    """
    Creates and returns the order processing chain with all handlers configured
    in the correct order: inventory validation → tax calculation → promotion
    application → payment processing → inventory update → order confirmation

    Returns:
        The first handler in the chain (InventoryValidator)
    """
    inventory_validator = InventoryValidator()
    tax_calculator = TaxCalculator()
    promotion_applier = PromotionApplier()
    payment_processor = PaymentProcessor()
    inventory_updater = InventoryUpdater()
    confirmation_sender = OrderConfirmationSender()
    
    # Set up the chain
    inventory_validator.set_next(tax_calculator)
    tax_calculator.set_next(promotion_applier)
    promotion_applier.set_next(payment_processor)
    payment_processor.set_next(inventory_updater)
    inventory_updater.set_next(confirmation_sender)
    
    return inventory_validator
