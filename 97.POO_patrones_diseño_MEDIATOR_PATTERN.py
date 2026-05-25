class ChatRoom:
  def __init__(self):
    self.usuarios = []

  def register_user(self, usuario):
    self.usuarios.append(usuario)

  def send_message(self,sender,message):
    for usuario in self.usuarios:
      if usuario != sender:
        usuario.recive(sender,message)


class Usuario:
  def __init__(self,name,chat):
    self.name = name
    self.chat = chat

  def send_message(self,message):
    self.chat.send_message(self,message)

  def recive(self, sender, message):
    print(f"{self.name} recibe un mensaje de {sender.name}: {message}")

chat = ChatRoom()

u1 = Usuario("Andres",chat)
u2 = Usuario("Ana",chat)
u3 = Usuario("Jhon", chat)

chat.register_user(u1)
chat.register_user(u2)
chat.register_user(u3)

u1.send_message("Hola de nuevo!!!")


# u1.add_friend(u2)
# u1.add_friend(u3)

# u2.add_friend(u1)
# u2.add_friend(u3)

# u3.add_friend(u1)
# u3.add_friend(u2)

# u1.send_message("Hola a todos!!")
