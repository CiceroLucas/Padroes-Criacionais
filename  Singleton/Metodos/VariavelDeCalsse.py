class Singleton:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Usando o singleton
instance = Singleton()
print(instance)

# Tentativa de criar outra instância
instance2 = Singleton()
print(instance2)
