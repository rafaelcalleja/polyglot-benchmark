from typing import Dict, Any, Optional


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


class OrderValidator:
    """A large class handling all order processing responsibilities"""
    
    def process_order(self, order: Order) -> Order:
        """
        Process an order through all validation and processing steps

        Args:
            order: The order to process

        Returns:
            The processed order with updated total and validated status
        """
        # This is a large method with multiple responsibilities
        
        # Inventory validation
        print(f"Validating inventory for order {order.order_id}")
        # In a real system, this would check against a database
        # Assuming all items are in stock for this example
        
        # Tax calculation
        print(f"Calculating taxes for order {order.order_id}")
        if order.region == "EU":
            order.total *= 1.21  # 21% VAT
        elif order.region == "US":
            order.total *= 1.08  # 8% sales tax
        # Other regions could be added here
        
        # Promotion application
        print(f"Checking for promotions on order {order.order_id}")
        if order.promo_code == "SUMMER23":
            print("Applying 10% summer discount")
            order.total *= 0.9
        elif order.promo_code == "WELCOME":
            print("Applying 15% welcome discount")
            order.total *= 0.85
        # Other promo codes could be added here
        
        # Payment processing
        print(f"Processing payment of ${order.total:.2f} for order {order.order_id}")
        # In a real system, this would interact with a payment gateway
        
        # Inventory update
        print(f"Updating inventory for order {order.order_id}")
        for item_id, quantity in order.items.items():
            print(f"Decreasing stock of item {item_id} by {quantity}")
        
        # Order confirmation
        print(f"Sending order confirmation for order {order.order_id}")
        # In a real system, this would send an email or notification
        
        order.validated = True
        return order
