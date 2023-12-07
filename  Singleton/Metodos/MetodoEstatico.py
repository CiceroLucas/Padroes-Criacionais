class Singleton:

    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance


# Usando o singleton
instance = Singleton.getInstance()
print(instance)


# Tentativa de criar outra instância
instance2 = Singleton.getInstance()
print(instance2)
