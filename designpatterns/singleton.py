class Singleton:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      print("Instance creating")
      cls._instance = super(Singleton, cls).__new__(cls)
    return cls._instance


cl1 = Singleton()
cl2 = Singleton()
cl3 = Singleton()

print(cl1 is cl2)
print(cl2 is cl3)