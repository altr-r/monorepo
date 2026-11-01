class Singleton:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      print("creating the instance")
      cls._instance = super(Singleton, cls).__new__(cls)

    return cls._instance

client1 = Singleton()
client2 = Singleton()
client3 = Singleton()

print(client1)
print(client2)
print(client3)