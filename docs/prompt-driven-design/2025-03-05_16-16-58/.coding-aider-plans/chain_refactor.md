## Overview
Implement a Python exercise demonstrating refactoring from a Large Class to Chain of Responsibility pattern. The exercise will guide students through restructuring a monolithic validation class into handler classes following the Chain of Responsibility pattern.

## Problem Description
A legacy `OrderValidator` class has grown too large, handling multiple validation responsibilities:
- Authentication
- Authorization
- Data sanitization
- Brute force protection
- Request caching

Students will refactor this into separate handler classes chained together.

## Goals
1. Create base `Handler` interface with `set_next` and `handle` methods
2. Implement concrete handlers for each validation responsibility
3. Update tests to verify chain behavior
4. Provide example implementation using Chain of Responsibility
5. Create instructions explaining the refactoring process

## Additional Notes and Constraints
- Must follow Exercism's practice exercise structure
- Use Python 3.10+ features
- Include type hints
- Maintain 100% test coverage
- Follow PEP8 guidelines

## References
- [Chain of Responsibility Documentation](/docs/chain_of_responsability.md)
- [Large Class Smell](/docs/refactor/smells/large-class.md)
- [Exercism Practice Exercises](/docs/practice-exercises.md)
