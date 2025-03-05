from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, final, cast


class Order:
    """Represents an order with its details"""
    
    def __init__(
        self,
        order_id: str,
        customer_id: str,
        items: Dict[str, int],
        total: float,
        region: str = "",
        promo_code: str = ""
    ):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items  # Dictionary of item_id: quantity
        self.total = total
        self.region = region
        self.promo_code = promo_code
        self.validated = False


class OrderHandler(ABC):
    """Base handler class for the Chain of Responsibility pattern"""
    
    def __init__(self):
        self._next_handler: Optional[OrderHandler] = None
    
    def set_next(self, handler: 'OrderHandler') -> 'OrderHandler':
        """Set the next handler in the chain"""
        self._next_handler = handler
        return handler
    
    @final
    def next(self, order: Order) -> Order:
        """
        Pass the order to the next handler if it exists

        Args:
            order: The order object to be processed

        Returns:
            The processed order after being handled by the next handler,
            or the original order if there is no next handler
        """
        if self._next_handler:
            return cast(Order, self._next_handler.handle(order))
        return order
    
    @abstractmethod
    def handle(self, order: Order) -> Order:
        """Process the order and pass it to the next handler"""
        pass


class InventoryValidator(OrderHandler):
    """Validates that all items are in stock"""
    
    def handle(self, order: Order) -> Order:
        print(f"Validating inventory for order {order.order_id}")
        # Simulation of inventory validation
        # In a real system, this would check against a database
        
        # Assuming all items are in stock for this example
        return self.next(order)


class TaxCalculator(OrderHandler):
    """Calculates taxes based on the order's region"""
    
    def handle(self, order: Order) -> Order:
        print(f"Calculating taxes for order {order.order_id}")
        
        if order.region == "EU":
            order.total *= 1.21  # 21% VAT
        elif order.region == "US":
            order.total *= 1.08  # 8% sales tax
        # Other regions could be added here
        
        return self.next(order)


class PromotionApplier(OrderHandler):
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


class PaymentProcessor(OrderHandler):
    """Processes payment for the order"""
    
    def handle(self, order: Order) -> Order:
        print(f"Processing payment of ${order.total:.2f} for order {order.order_id}")
        # In a real system, this would interact with a payment gateway
        
        # Simulate successful payment
        return self.next(order)


class InventoryUpdater(OrderHandler):
    """Updates inventory after successful order processing"""
    
    def handle(self, order: Order) -> Order:
        print(f"Updating inventory for order {order.order_id}")
        # In a real system, this would update a database
        
        for item_id, quantity in order.items.items():
            print(f"Decreasing stock of item {item_id} by {quantity}")
        
        return self.next(order)


class OrderConfirmationSender(OrderHandler):
    """Sends order confirmation to the customer"""
    
    def handle(self, order: Order) -> Order:
        print(f"Sending order confirmation for order {order.order_id}")
        # In a real system, this would send an email or notification
        
        order.validated = True
        return self.next(order)


def process_order(order: Order) -> Order:
    """Process an order through the chain of handlers"""
    # Create the chain
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
    
    # Process the order through the chain
    return inventory_validator.handle(order)
