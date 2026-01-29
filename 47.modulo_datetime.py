from datetime import datetime

fecha = datetime.now()

print(fecha.day)
print(fecha.hour)
print(fecha.minute)
print(fecha.second)

print(fecha.strftime("%a %b %p"))