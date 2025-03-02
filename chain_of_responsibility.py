from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging

@dataclass
class Order:
    items: list
    total: float
    region: str
    promo_code: str = None

class OrderHandler(ABC):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, order):
        if self._next_handler:
            return self._next_handler.handle(order)
        return order

class InventoryValidator(OrderHandler):
    def handle(self, order):
        logging.info("Validating inventory levels")
        # Validation logic would go here
        return super().handle(order)

class TaxCalculator(OrderHandler):
    def handle(self, order):
        if order.region == "EU":
            order.total *= 1.21
        elif order.region == "US":
            order.total *= 1.08
        return super().handle(order)

class PromotionApplier(OrderHandler):
    def handle(self, order):
        if order.promo_code == "SUMMER23":
            order.total *= 0.9
        return super().handle(order)

class PaymentProcessor(OrderHandler):
    def handle(self, order):
        logging.info(f"Processing payment of ${order.total:.2f}")
        # Payment processing logic would go here
        return super().handle(order)

class InventoryUpdater(OrderHandler):
    def handle(self, order):
        logging.info("Updating inventory levels")
        # Inventory update logic would go here
        return super().handle(order)

class OrderConfirmationSender(OrderHandler):
    def handle(self, order):
        logging.info("Sending order confirmation")
        # Email sending logic would go here
        return super().handle(order)

class OrderProcessor:
    def __init__(self):
        # Create and chain handlers
        self.handler_chain = (
            InventoryValidator()
            .set_next(TaxCalculator())
            .set_next(PromotionApplier())
            .set_next(PaymentProcessor())
            .set_next(InventoryUpdater())
            .set_next(OrderConfirmationSender())
        )
    
    def process_order(self, order):
        return self.handler_chain.handle(order)
