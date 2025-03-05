Exercism es una plataforma que ofrece ejercicios prácticos para mejorar habilidades de programación a través de desafíos estructurados y retroalimentación de la comunidad. A continuación, presento un ejemplo completo de cómo crear un nuevo ejercicio de práctica para el track de Python en Exercism, siguiendo los requisitos del proyecto.

## Estructura Básica de un Ejercicio

Para crear un ejercicio de práctica efectivo para el repositorio de Exercism Python, debemos seguir una estructura específica que permita la integración con la plataforma y proporcione una experiencia de aprendizaje completa.

### Paso 1: Creación de la Estructura de Directorios

Primero, necesitamos crear la estructura de directorios adecuada dentro del repositorio:

```
exercises/practice/mi-ejercicio/
├── .meta/
│   ├── config.json
│   ├── example.py
│   └── tests.toml
├── mi_ejercicio.py
└── mi_ejercicio_test.py
```


### Paso 2: Definición del Archivo de Configuración

El archivo `config.json` en el directorio `.meta` define los metadatos del ejercicio:

```json
{
  "blurb": "Aprende a manipular listas y diccionarios resolviendo un problema de inventario.",
  "authors": ["tu-nombre-de-usuario"],
  "contributors": [],
  "files": {
    "solution": ["mi_ejercicio.py"],
    "test": ["mi_ejercicio_test.py"],
    "example": [".meta/example.py"]
  },
  "source": "Inspirado en problemas reales de gestión de inventario",
  "source_url": "https://github.com/exercism/python"
}
```


### Paso 3: Creación del Archivo de Solución Ejemplo

El archivo `example.py` contiene una implementación de referencia que pasa todas las pruebas:

```python
def add_item(inventory, item, quantity):
    """Añade un ítem al inventario con la cantidad especificada."""
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory

def remove_item(inventory, item, quantity):
    """Remueve una cantidad específica de un ítem del inventario."""
    if item not in inventory:
        return inventory
    
    inventory[item] -= quantity
    if inventory[item] <= 0:
        del inventory[item]
    return inventory

def get_items_count(inventory):
    """Devuelve el número total de ítems diferentes en el inventario."""
    return len(inventory)

def get_item_quantity(inventory, item):
    """Devuelve la cantidad de un ítem específico en el inventario."""
    return inventory.get(item, 0)

def get_most_stocked_item(inventory):
    """Devuelve el ítem con mayor cantidad en el inventario."""
    if not inventory:
        return None
    return max(inventory.items(), key=lambda x: x[^1])[^0]
```


### Paso 4: Creación del Archivo de Plantilla para el Estudiante

El archivo `mi_ejercicio.py` es la plantilla que los estudiantes completarán:

```python
def add_item(inventory, item, quantity):
    """Añade un ítem al inventario con la cantidad especificada."""
    pass

def remove_item(inventory, item, quantity):
    """Remueve una cantidad específica de un ítem del inventario."""
    pass

def get_items_count(inventory):
    """Devuelve el número total de ítems diferentes en el inventario."""
    pass

def get_item_quantity(inventory, item):
    """Devuelve la cantidad de un ítem específico en el inventario."""
    pass

def get_most_stocked_item(inventory):
    """Devuelve el ítem con mayor cantidad en el inventario."""
    pass
```


### Paso 5: Creación de los Tests

El archivo `mi_ejercicio_test.py` contiene las pruebas para validar la solución del estudiante:

```python
import unittest
import pytest
from mi_ejercicio import (
    add_item,
    remove_item,
    get_items_count,
    get_item_quantity,
    get_most_stocked_item
)

class InventoryManagementTest(unittest.TestCase):
    
    def test_add_new_item(self):
        inventory = {}
        updated = add_item(inventory, "manzana", 5)
        self.assertEqual(updated, {"manzana": 5})
        
    def test_add_existing_item(self):
        inventory = {"manzana": 5}
        updated = add_item(inventory, "manzana", 3)
        self.assertEqual(updated, {"manzana": 8})
        
    def test_remove_existing_item_partial(self):
        inventory = {"manzana": 5}
        updated = remove_item(inventory, "manzana", 3)
        self.assertEqual(updated, {"manzana": 2})
        
    def test_remove_existing_item_complete(self):
        inventory = {"manzana": 5}
        updated = remove_item(inventory, "manzana", 5)
        self.assertEqual(updated, {})
        
    def test_remove_nonexistent_item(self):
        inventory = {"manzana": 5}
        updated = remove_item(inventory, "pera", 3)
        self.assertEqual(updated, {"manzana": 5})
        
    def test_get_items_count(self):
        inventory = {"manzana": 5, "pera": 3, "naranja": 7}
        count = get_items_count(inventory)
        self.assertEqual(count, 3)
        
    def test_get_item_quantity_existing(self):
        inventory = {"manzana": 5, "pera": 3}
        quantity = get_item_quantity(inventory, "pera")
        self.assertEqual(quantity, 3)
        
    def test_get_item_quantity_nonexistent(self):
        inventory = {"manzana": 5, "pera": 3}
        quantity = get_item_quantity(inventory, "naranja")
        self.assertEqual(quantity, 0)
        
    def test_get_most_stocked_item(self):
        inventory = {"manzana": 5, "pera": 3, "naranja": 7}
        most_stocked = get_most_stocked_item(inventory)
        self.assertEqual(most_stocked, "naranja")
        
    def test_get_most_stocked_item_empty(self):
        inventory = {}
        most_stocked = get_most_stocked_item(inventory)
        self.assertIsNone(most_stocked)

if __name__ == "__main__":
    unittest.main()
```


### Paso 6: Creación del Archivo tests.toml

El archivo `tests.toml` en el directorio `.meta` define metadatos para las pruebas:

```toml
[canonical-tests]

# Prueba añadir un nuevo ítem al inventario
"add-new-item" = { task_id = 1, include = true }

# Prueba añadir un ítem existente al inventario
"add-existing-item" = { task_id = 2, include = true }

# Prueba remover parcialmente un ítem existente
"remove-existing-item-partial" = { task_id = 3, include = true }

# Prueba remover completamente un ítem existente
"remove-existing-item-complete" = { task_id = 4, include = true }

# Prueba remover un ítem no existente
"remove-nonexistent-item" = { task_id = 5, include = true }

# Prueba obtener cantidad de ítems diferentes
"get-items-count" = { task_id = 6, include = true }

# Prueba obtener cantidad de un ítem existente
"get-item-quantity-existing" = { task_id = 7, include = true }

# Prueba obtener cantidad de un ítem no existente
"get-item-quantity-nonexistent" = { task_id = 8, include = true }

# Prueba obtener el ítem con mayor cantidad
"get-most-stocked-item" = { task_id = 9, include = true }

# Prueba obtener el ítem con mayor cantidad en inventario vacío
"get-most-stocked-item-empty" = { task_id = 10, include = true }
```


## Documentación del Ejercicio

Además de los archivos de código, es importante proporcionar documentación clara para el ejercicio. Esto incluye un archivo `README.md` en el directorio del ejercicio que explique:

1. El contexto del problema
2. Los requisitos específicos
3. Ejemplos de uso
4. Pistas para la solución
5. Enlaces a recursos adicionales

## Integración con el Proyecto Principal

Para integrar este ejercicio en el repositorio principal de Exercism Python, debes:

1. Actualizar el archivo `config.json` en la raíz del repositorio para incluir tu ejercicio
2. Asegurar que todos los tests pasen utilizando la solución de ejemplo
3. Seguir las pautas de estilo de código de Python (PEP 8)
4. Enviar un Pull Request al repositorio principal

Este ejemplo muestra cómo crear un ejercicio de gestión de inventario, un problema práctico que ayuda a los estudiantes a trabajar con estructuras de datos fundamentales en Python como diccionarios y listas, a la vez que resuelven un problema del mundo real[^8].

Al desarrollar ejercicios para Exercism, recuerda que el objetivo principal es facilitar el aprendizaje a través de la práctica, proporcionando desafíos interesantes y retroalimentación útil[^5]. Los ejercicios bien diseñados pueden ayudar significativamente a mejorar las habilidades de programación de los estudiantes, como lo demuestra la popularidad de la plataforma con más de 526,000 estudiantes y millones de soluciones enviadas.

<div style="text-align: center">⁂</div>

[^1]: https://campusvirtual.ull.es/ocw/mod/url/view.php?id=11184

[^2]: https://www.youtube.com/watch?v=PN668AU1vJw

[^3]: https://github.com/makeitrealcamp/ejercicios-javascript

[^4]: https://www.youtube.com/watch?v=CpxNW-eDgaQ

[^5]: https://github.com/ASJordi/exercism

[^6]: https://www.woah.org/app/uploads/2024/08/simulation-exercises-vesp-revised-1st-edition.pdf

[^7]: https://www.youtube.com/watch?v=b4oWaglienY

[^8]: https://programacion.net/noticia/aprende-a-programar-haciendo-ejercicios-con-exercism-io_2181

[^9]: https://exercism.org/tracks/python

[^10]: https://www.youtube.com/watch?v=GyWTQCOGDbY

[^11]: https://es.linkedin.com/posts/xavier-reyes-ochoa_programacion-desarrolloweb-python-activity-7260645537454927872--S5P

[^12]: https://retosdeprogramacion.com/ejercicios

[^13]: https://www.youtube.com/watch?v=_iPlG-yui5Q

[^14]: https://www.youtube.com/watch?v=P-OzjJ2Aumg

[^15]: https://www.youtube.com/watch?v=O7t7UNKyp8s

[^16]: https://www.youtube.com/watch?v=hmR5irWINEs

[^17]: https://www.neoteo.com/exercism-mas-de-60-lenguajes-para-aprender-a-programar-gratis/

[^18]: https://www.youtube.com/watch?v=U7Og8VVLugI

[^19]: https://exercism.org/tracks/python/exercises

[^20]: https://www.youtube.com/watch?v=FW5A4H8LE6o
