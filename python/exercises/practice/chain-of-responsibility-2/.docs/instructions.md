# Chain of Responsibility: Email Processor

## Instructions

In this exercise, you'll implement an email processing system using the Chain of Responsibility pattern.

The Chain of Responsibility pattern is a behavioral design pattern that passes requests along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain.

You will create an email processor with various handlers that can:
1. Filter spam
2. Validate email format
3. Add legal disclaimers
4. Log email processing

## Requirements

1. Create an abstract `Handler` class with:
   - A method to set the next handler in the chain
   - An abstract `handle` method for processing emails

2. Implement the following concrete handlers:
   - `SpamHandler`: Detects and removes spam content
   - `ValidatorHandler`: Validates email format (must contain '@')
   - `DisclaimerHandler`: Adds a legal disclaimer to emails
   - `LoggerHandler`: Simulates logging email activities

3. Create an `EmailProcessor` class that:
   - Maintains a chain of handlers
   - Provides a method to add handlers to the chain
   - Processes emails through the chain

## Example

```
# Create the processor and chain of handlers
processor = EmailProcessor()
processor.add_handler(SpamHandler())
         .add_handler(ValidatorHandler())
         .add_handler(DisclaimerHandler())
         .add_handler(LoggerHandler())

# Process a legitimate email
result = processor.process("Hello, this is a valid message")

# Process a spam email
spam_result = processor.process("Buy cheap pills!")
```

## Key Concepts

- **Single Responsibility Principle**: Each handler has one specific responsibility
- **Open/Closed Principle**: You can add new handlers without modifying existing code
- **Chain Construction**: Handlers can be added in any order to create different processing flows
- **Request Handling**: Each handler can either process the request and pass it on, or stop the chain

## Notes

- Focus on implementing a clean, flexible design
- Consider how the order of handlers affects processing results
- Think about how you might extend the system with new handlers
