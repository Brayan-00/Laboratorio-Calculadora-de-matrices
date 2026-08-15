# Laboratorio-Calculadora-de-matrices

## Descripción del Proyecto

Este proyecto consiste en una **calculadora de matrices** desarrollada en **Python**, capaz de realizar las operaciones de **suma, multiplicación, cálculo del determinante e inversa de matrices**.

La aplicación permite al usuario interactuar mediante una **interfaz de línea de comandos (CLI)**. Las matrices de entrada se proporcionan a través de un archivo en formato **JSON**, en el cual se especifican sus dimensiones y los datos correspondientes. A partir de esta información, el usuario puede seleccionar la operación que desea ejecutar y obtener el resultado desde la terminal.

## Diagrama del diseño

### Diagrama de Flujo

![Diagrama de Flujo](Diagrama%20de%20Flujo.png)

### Diagrama de Clases

![Diagrama de Clases](Diagrama%20de%20Clases.png)

## Instrucciones de instalación

Este proyecto utiliza `uv` para gestionar el entorno virtual, las dependencias y la ejecución de la calculadora. Por lo tanto, antes de continuar, verifique que `uv` se encuentre instalado en su sistema. Si no lo tiene instalado, siga las instrucciones correspondientes a su sistema operativo.

### 1. Verificar la instalación de `uv`

Antes de preparar el proyecto, verifique que `uv` se encuentre instalado en el sistema ejecutando:

```bash
uv --version
```

Si el comando muestra la versión instalada de `uv`, puede continuar directamente con la instalación del proyecto.

Si `uv` no se encuentra instalado, puede instalarlo mediante uno de los siguientes comandos, según su sistema operativo:

#### Linux y macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Preparar el proyecto

Desde la terminal, diríjase a la carpeta raíz del proyecto, donde se encuentra el archivo `pyproject.toml` y ejecute:

```bash
uv sync
```

El comando `uv sync` prepara el entorno necesario para ejecutar el proyecto. Durante este proceso, `uv` crea el entorno virtual `.venv`.

### 3. Comprobar la instalación

Para comprobar que la aplicación se encuentra disponible en el entorno del proyecto, ejecute:

```bash
uv run matrix-calc --help
```

Si el comando muestra la información de ayuda de `matrix-calc`, la instalación y preparación del proyecto se realizaron correctamente.

## Instrucciones de utilización

### Formato del archivo de entrada

Las matrices sobre las que se realizarán las operaciones deben proporcionarse mediante un archivo en formato **JSON**.

El archivo debe contener dos matrices, identificadas como `matrixA` y `matrixB`. Para cada matriz se deben especificar sus dimensiones y los datos correspondientes mediante los siguientes campos:

* `rows`: número de filas de la matriz.
* `cols`: número de columnas de la matriz.
* `data`: valores que conforman la matriz, organizados por filas.

Por ejemplo, para ingresar dos matrices de dimensiones $2 \cdot 2$, el archivo JSON puede tener la siguiente estructura:

```json
{
  "matrixA": {
    "rows": 2,
    "cols": 2,
    "data": [
      [1.0, 2.0],
      [3.0, 4.0]
    ]
  },
  "matrixB": {
    "rows": 2,
    "cols": 2,
    "data": [
      [5.0, 6.0],
      [7.0, 8.0]
    ]
  }
}
```

Las dimensiones indicadas en `rows` y `cols` deben coincidir con la cantidad de filas y columnas presentes en `data`.

Por ejemplo, si una matriz se define con:

```json
"rows": 2,
"cols": 2
```

el campo `data` debe contener dos filas con dos valores cada una.

El archivo puede guardarse, por ejemplo, con el nombre:

```text
matrices.json
```

### Ejecución de operaciones desde la terminal

Una vez preparado el proyecto y definido el archivo JSON con las matrices de entrada, la calculadora puede ejecutarse desde la terminal utilizando la siguiente estructura:

```bash
uv run matrix-calc run <operación> --input <archivo.json>
```

En este comando:

* `<operación>` corresponde a la operación matricial que se desea realizar.
* `<archivo.json>` corresponde al archivo que contiene las matrices de entrada.

Las operaciones disponibles son:

* `add`: suma de matrices.
* `mul`: multiplicación de matrices.
* `det`: cálculo del determinante.
* `inv`: cálculo de la inversa.

La opción `--input` permite indicar el archivo JSON que contiene `matrixA` y `matrixB`.

### Ejemplos de utilización

En los siguientes ejemplos se utiliza un archivo llamado `matrices.json` como entrada.

#### Suma de matrices

Para realizar la suma de `matrixA` y `matrixB`, ejecute:

```bash
uv run matrix-calc run add --input matrices.json
```

El comando `add` indica que se debe realizar la suma de las dos matrices.

#### Multiplicación de matrices

Para realizar la multiplicación de `matrixA` por `matrixB`, ejecute:

```bash
uv run matrix-calc run mul --input matrices.json
```

El comando `mul` selecciona la operación de multiplicación matricial.

#### Determinante

Para calcular el determinante de las matrices proporcionadas, ejecute:

```bash
uv run matrix-calc run det --input matrices.json
```

El comando `det` calcula el determinante de cada una de las matrices de entrada.

#### Inversa

Para calcular la inversa de las matrices proporcionadas, ejecute:

```bash
uv run matrix-calc run inv --input matrices.json
```

El comando `inv` calcula la matriz inversa de cada una de las matrices de entrada, siempre que se cumplan las condiciones para que la operación pueda realizarse.

## Instrucciones para ejecutar las pruebas

El proyecto cuenta con una suite de **pruebas automatizadas** para verificar el funcionamiento de los diferentes componentes de la calculadora y la integración entre ellos.

### Ejecución de las pruebas

Para ejecutar todos los tests del proyecto, utilice:

```bash
uv run pytest
```

La suite completa contiene actualmente **22 pruebas**, todas las cuales deben ejecutarse correctamente.

### Pruebas de integración de la CLI

Las pruebas de integración verifican la interacción entre la interfaz de línea de comandos y los diferentes componentes de la calculadora de matrices.

Estas pruebas incluyen:

* Verificación de que el comando `ops` muestra todas las operaciones soportadas.
* Suma de matrices utilizando un archivo JSON como entrada.
* Multiplicación de matrices utilizando un archivo JSON como entrada.
* Cálculo del determinante utilizando un archivo JSON como entrada.
* Cálculo de la inversa utilizando un archivo JSON como entrada.
* Generación de archivos de salida mediante la opción `--output`.

La prueba de generación de archivos de salida verifica tanto que el archivo JSON sea creado correctamente como que su contenido coincida con el resultado esperado de la operación.

### Pruebas de los componentes

Además de las pruebas de integración de la CLI, el proyecto incluye pruebas específicas para los principales componentes de la aplicación:

* **CLI:** verifica el funcionamiento de la interfaz de línea de comandos.
* **JSON Adapter:** verifica la lectura, validación y procesamiento de los datos de entrada.
* **Suma:** verifica el funcionamiento de la suma de matrices.
* **Multiplicación:** verifica el funcionamiento de la multiplicación de matrices.
* **Determinante:** verifica el cálculo del determinante.
* **Inversa:** verifica el cálculo de la matriz inversa.

### Verificación del código

Además de las pruebas funcionales, se utiliza **Ruff** para verificar la calidad, formato y estilo del código.

Para comprobar el estilo del código, ejecute:

```bash
uv run ruff check .
```

Para verificar el formato:

```bash
uv run ruff format --check .
```

El proyecto debe mantener todas las pruebas exitosas y cumplir con las reglas de estilo definidas para el desarrollo.

## Uso de la Inteligencia Artificial

Se hizo uso de herramientas de Inteligencia Artificial principalmente en áreas de documentación, implementación y redacción, incluyendo issues y el presente documento.

### Conversaciones 

Se adjuntan links de las conversaciones como método de transparencia.

[Conversación 1](https://chatgpt.com/share/6a7fd8c9-49d0-83e8-92fc-3cddc66d7e84)
[Conversación 2](https://chatgpt.com/share/6a7fda78-7130-83e8-b975-9f30e66915c9)


## Integrantes, curso y profesor

### Integrantes

1. Fiorela Chavarría Castrillo
2. Fabián Parreaguirre Hidalgo
3. Brayan Rodríguez Villalobos
4. Yonaikel Tencio Valverde

### Curso

Introducción a la Computación Heterogénea - EL-5859

### Profesor

Dr. Luis G. León-Vega

