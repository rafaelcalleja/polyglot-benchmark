# Order Validator

Welcome to the Order Validator refactoring exercise!

## Introduction

This exercise focuses on refactoring a monolithic class that has grown too large and has too many responsibilities.

You will convert a large "God Class" into a series of smaller, focused classes using the Chain of Responsibility design pattern.

## The Problem

The `OrderValidator` class has grown to handle multiple validation responsibilities:
- Authentication checking
- Authorization validation
- Data sanitization
- Brute force protection
- Request caching

This violates the Single Responsibility Principle and makes the code hard to maintain, test, and extend.

## Your Task

Refactor the monolithic `OrderValidator` class into a series of handler classes following the Chain of Responsibility pattern:

1. Create a base `Handler` abstract class with:
   - Method to set the next handler in the chain
   - Abstract `handle` method

2. Implement concrete handlers for each responsibility:
   - `AuthenticationHandler`
   - `AuthorizationHandler`
   - `SanitizationHandler`
   - `BruteForceHandler`
   - `CacheHandler`

3. Chain the handlers together to process orders in sequence

## Example

Instead of:

```
class OrderValidator:
    def validate(self, order, user):
        # Authentication
        if not user.is_authenticated:
            return {"error": "User not authenticated"}

        # Authorization
        if not user.has_permission("place_order"):
            return {"error": "User not authorized"}

        # Many more validations...
```

Create:

```
class AuthenticationHandler(Handler):
    def handle(self, request):
        if not request.user.is_authenticated:
            return {"error": "User not authenticated"}
        return super().handle(request)

class AuthorizationHandler(Handler):
    def handle(self, request):
        if not request.user.has_permission("place_order"):
            return {"error": "User not authorized"}
        return super().handle(request)

# Chain them together
auth_handler = AuthenticationHandler()
auth_handler.set_next(AuthorizationHandler())
result = auth_handler.handle(request)
```

## Note

The Chain of Responsibility pattern enables you to:
- Process requests through a chain of handlers
- Each handler decides whether to process the request and/or pass it to the next handler
- Easily add or remove responsibilities without changing existing code
- Follow the Open/Closed Principle

Good luck with your refactoring!
