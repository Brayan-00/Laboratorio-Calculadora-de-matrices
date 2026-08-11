# Laboratorio-Calculadora-de-matrices


## Descripción del Proyecto

Esta calculadora implementa las siguientes operaciones para matrices: Suma, Multiplicación, Inversa de dos Matrices, Determinante de dos Matrices.

Se espera que el usuario interactúe con esta calculadora mediante una interfaz de comandos (CLI). Para ingresar las matrices sobre las que se aplicarán las operaciones se espera que el usuario aporte un archivo JSON.



## Diagrama del diseño

### Diagrama de Flujo

![Diagrama de Flujo]("Diagrama de Flujo.png")


### Diagrama de Clases

![Diagrama de Clases]("Diagrama de Clases.png")

## Instrucciones para instalación

### Instalación de uv

Para Linux y macOS:
```bash
curl -LsSf https://astral.sh | sh
```
Para Windows:

```PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh | iex"
```





## Instrucciones de utilización

### Formato JSON

``` JSON
{
 " matrixA " : {
    " rows " : 2 ,
    " cols " : 3 ,
    " data " : [
        [ 1 . 2 5 , 2 . 5 0 , 3 . 7 5 ] ,
        [ 4 . 0 0 , 5 . 1 0 , 6 . 2 0 ]
    ]
    } ,
    " matrixB " : {
        " rows " : 3 ,
        " cols " : 2 ,
        " data " : [
            [ 1 0 . 0 , 1 1 . 0 ] ,
            [ 1 2 . 0 , 1 3 . 0 ] ,
            [ 1 4 . 0 , 1 5 . 0 ]
        ]
    }
  }
```


## Ejemplos de utilización


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
