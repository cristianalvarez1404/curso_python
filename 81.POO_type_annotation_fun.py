from typing import Union,Optional,Callable

num:int = 10
name:str = "ana"
cifra:float = 5.2
es_correcto:bool = False

def operacion(a:int, b:int) -> int:
  return a + b

operacion(1,2)

var1:Optional[str] = "string"
var2:Union[str,float] = 10.2
var3: str | float = 10.2

def sumar(a:int | float, b:int | float) -> int | float:
  return a + b

def crear_usuario(name:str, edad:int | str) -> dict[str,int | str]:
  return {"name":name, "edad":edad}


# u1 = crear_usuario("Jhon",45)
# print(u1)

def generar_numeros() -> list[int | str]:
  return [1,2,3,4]

# print(generar_numeros())

def sumar(a:int, b:int) -> int:
  return a + b

def generar_suma(a:int, b:int, operacion:Callable[[int,int],int]):
  return operacion(a,b)

print(generar_suma(4,5,sumar))

