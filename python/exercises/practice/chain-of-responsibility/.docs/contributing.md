# Chain of Responsibility Contribution Guide

## Real-World Implementation Context

Implement a data processing pipeline for secure message transmission that:

1. **Sanitizes** input (remove special characters)
2. **Validates** message format
3. **Encrypts** sensitive data
4. **Logs** transmission attempts

```
# Example Security Pipeline
class SecureMessageHandler(Handler):
    def handle(self, payload):
        processing_chain = SanitizerHandler()\
            .set_next(ValidatorHandler())\
            .set_next(EncryptorHandler())\
            .set_next(LoggerHandler())
        return processing_chain.handle(payload)
```

## Core Requirements

### Handler Implementation
1. Inherit from `Handler` ABC as shown in `.meta/example.py`
2. Maintain fluent interface for chain composition
3. Preserve the base `set_next()` implementation

### Validation Rules
```
class ValidatorHandler(Handler):
    def handle(self, message):
        if not message.startswith("SECURE:"):
            return super().handle(f"SECURE:{message}")
        return super().handle(message)
```

### Testing Standards
1. 100% handler coverage
2. Parameterized tests for chain permutations
3. Verify chain break conditions

```
def test_encrypted_logging():
    chain = SanitizerHandler().set_next(EncryptorHandler()).set_next(LoggerHandler())
    assert chain.handle("Sensitive!") == "ENCRYPTED:Sensitive"
    # Verify log output contains encrypted string
```

## Forbidden Patterns
❌ No external cryptography libraries  
❌ Never store chain state between requests  
❌ Avoid branching logic within handlers

## Implementation Checklist

1. Create base handler hierarchy
2. Implement concrete handlers:
   - `SanitizerHandler` (strip special chars)
   - `ValidatorHandler` (add SECURE: prefix)
   - `EncryptorHandler` (prepend ENCRYPTED:)
   - `LoggerHandler` (console output)
3. Test chain permutations
4. Document handler execution order

## Style Priorities
1. Consistent handler signatures
2. Clear failure messages
3. Minimal inter-handler coupling

> Maintain compatibility with Python 3.7+  
> Follow PEP8 with 120 char line limit  
> Validate using flake8 and pylint configs

See [main contributing guidelines](../../../docs/contributing.md) for detailed Python track standards.
# Chain of Responsibility Pattern Exercise (Payment Processor)

## Contexto del Ejercicio

Implementar un sistema de procesamiento de pagos usando Chain of Responsibility que:

1. Valide los datos de la tarjeta
2. Verifique fondos disponibles
3. Realice la transacción
4. Genere registro de auditoría

```
# Ejemplo de uso requerido
class PaymentProcessor(Handler):
    def handle_payment(self, request):
        chain = ValidationHandler()\
            .set_next(FraudCheckHandler())\
            .set_next(PaymentGatewayHandler())\
            .set_next(AuditLoggerHandler())
        return chain.handle(request)
```

## Requisitos Principales

### Implementación del Handler
1. Clase base `PaymentHandler` que herede de ABC
2. Método `set_next()` para encadenamiento fluido
3. Manejo condicional basado en tipo de pago

```
class FraudCheckHandler(PaymentHandler):
    def handle(self, transaction):
        if transaction.amount > 10000:
            raise FraudDetectionError()
        return super().handle(transaction)
```

### Casos de Prueba Obligatorios
```
def test_full_payment_flow():
    transaction = PaymentRequest(amount=150, card="4111111111111111")
    result = PaymentProcessor().handle_payment(transaction)
    assert result.status == "APPROVED"
    assert audit_log_contains(transaction.id)
```

## Patrones Prohibidos
❌ No usar bibliotecas externas de procesamiento de pagos  
❌ No almacenar estado entre solicitudes  
❌ No usar herencia múltiple en los handlers

## Checklist de Implementación

1. Crear jerarquía base de handlers
2. Implementar handlers concretos:
   - `ValidationHandler` (valida formato tarjeta)
   - `FraudCheckHandler` (detecta transacciones sospechosas)
   - `PaymentGatewayHandler` (simula conexión con banco)
   - `AuditLoggerHandler` (registra en archivo)
3. Pruebas para flujos alternativos (fraude detectado, fondos insuficientes)
4. Documentar secuencia de procesamiento

## Estilo Requerido
1. Métodos con type hints
2. Mensajes de error descriptivos
3. Encadenamiento fluido en composición

> Versión mínima: Python 3.8  
> Usar dataclasses para objetos de transacción  
> Seguir configuración flake8 del proyecto

Ejemplo completo en [example.py](.meta/example.py). Consulte las [guías principales](../../../docs/contributing.md) para estándares de documentación.
