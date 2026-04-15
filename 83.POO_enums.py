from enum import Enum
from dataclasses import dataclass

class OrderStatus(Enum):
  PAID = "paid"
  CANCELLED = "cancelled"
  PENDING = "pending"


@dataclass
class Order:
  id:int
  status:OrderStatus

def process_order(order:Order) -> str:
  match order.status:
    case OrderStatus.PENDING:
      return "orden pendiente..."
    
    case OrderStatus.PAID:
      return "orden pagada"
    
    case OrderStatus.CANCELLED:
      return "orden cancelada"
    
orders = [
  {
    "id":1,
    "status":OrderStatus.PAID
  },
  {
    "id":2,
    "status":OrderStatus.CANCELLED
  },
  {
    "id":3,
    "status":OrderStatus.PENDING
  },
]

list_orders = [Order(order["id"], order["status"])  for order in orders]

for order in list_orders:
  print(process_order(order))