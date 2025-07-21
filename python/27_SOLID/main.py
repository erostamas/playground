SOLID Principles
S — Single Responsibility Principle (SRP)
A class should have only one reason to change.
Each class should do one thing and do it well.

Example:
Instead of one big class handling both data processing and file saving, split into two classes:

DataProcessor

FileSaver

O — Open/Closed Principle (OCP)
Software entities (classes, functions, modules) should be open for extension but closed for modification.

You should be able to add new features without changing existing code.

Achieved by using abstractions (interfaces/base classes).

L — Liskov Substitution Principle (LSP)
Subtypes must be substitutable for their base types without altering correctness.

Derived classes should work as expected wherever base classes are used.

Avoid breaking behavior in subclasses.

I — Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use.

Prefer many small, specific interfaces over a large, general-purpose interface.

Keeps classes focused and decoupled.

D — Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules; both should depend on abstractions.

Depend on interfaces or abstract classes, not concrete implementations.

This promotes loose coupling and easier testing.