from dataclasses import dataclass
from typing import Optional, Union

"""
int
str
float
"""

num1:int = 51 
nombre:str = "Carlos"
decimal:float = 1.2
lista_str:list[str] = ["ob1","ob2"]
lista_str:list[int] = [1,2,3,4]
lista_str:list[bool] = [True,False,True]

diccionario:dict[str,int] = {"prop1":1}

def sumar(a:int, b:int) -> int:
  return a + b

print(sumar(5,2))

@dataclass
class Usuario:
  nombre:str = "Ana"
  edad:int = 42

opcional:Optional[int] = "Carlos"
opcional:Optional[str] = 48

var1:Union[int, str] = 87
