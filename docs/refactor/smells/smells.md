# Code Smells

— What? How can code "smell"??  
— Well it doesn't have a nose... but it definitely can stink!

## Bloaters

**Bloaters** are code, methods, and classes that have increased to such gargantuan proportions that they are hard to work with. Usually, these smells do not crop up right away, rather they accumulate over time as the program evolves (and especially when nobody makes an effort to eradicate them).

- [Long Method](/smells/long-method)
- [Large Class](/smells/large-class)
- [Primitive Obsession](/smells/primitive-obsession)
- [Long Parameter List](/smells/long-parameter-list)
- [Data Clumps](/smells/data-clumps)

## Object-Orientation Abusers

All these smells are incomplete or incorrect application of object-oriented programming principles.

- [Alternative Classes with Different Interfaces](/smells/alternative-classes-with-different-interfaces)
- [Refused Bequest](/smells/refused-bequest)
- [Switch Statements](/smells/switch-statements)
- [Temporary Field](/smells/temporary-field)

## Change Preventers

These smells mean that if you need to change something in one place in your code, you have to make many changes in other places too. Program development becomes much more complicated and expensive as a result.

- [Divergent Change](/smells/divergent-change)
- [Parallel Inheritance Hierarchies](/smells/parallel-inheritance-hierarchies)
- [Shotgun Surgery](/smells/shotgun-surgery)

## Dispensables

A **dispensable** is something pointless and unneeded whose absence would make the code cleaner, more efficient, and easier to understand.

- [Comments](/smells/comments)
- [Duplicate Code](/smells/duplicate-code)
- [Data Class](/smells/data-class)
- [Dead Code](/smells/dead-code)
- [Lazy Class](/smells/lazy-class)
- [Speculative Generality](/smells/speculative-generality)

## Couplers

All the smells in this group contribute to excessive coupling between classes or show what happens if coupling is replaced by excessive delegation.

- [Feature Envy](/smells/feature-envy)
- [Inappropriate Intimacy](/smells/inappropriate-intimacy)
- [Incomplete Library Class](/smells/incomplete-library-class)
- [Message Chains](/smells/message-chains)
- [Middle Man](/smells/middle-man)

