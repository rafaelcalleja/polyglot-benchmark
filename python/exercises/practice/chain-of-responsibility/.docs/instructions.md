# Chain of Responsibility

Implementa una cadena de procesamiento de solicitudes donde cada handler puede manejar o pasar la solicitud al siguiente.

## Ejemplo

Crear 3 handlers:
1. **SanitizerHandler**: Elimina caracteres especiales
2. **ValidatorHandler**: Verifica formato válido
3. **LoggerHandler**: Registra la solicitud procesada

Cada handler debe decidir si puede procesar la solicitud o pasarla al siguiente en la cadena.
