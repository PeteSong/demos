from functools import wraps


class SingletonCls:
    """to create a singleton class"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class LazySingletonCls:
    """to create a lazy singleton class, use .get_instance() to get the instance"""

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


def singleton(cls):
    """a decorator to create a singleton class"""
    _instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


class SingletonMetaclass(type):
    """a metaclass to create a singleton class"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


def main() -> None:  # pragma: no cover
    cl1 = SingletonCls()
    cl2 = SingletonCls()
    print(f"{id(cl1)=}, {id(cl2)=}, {(cl1 is cl2)=}")

    lcl1 = LazySingletonCls.get_instance()
    lcl2 = LazySingletonCls.get_instance()
    print(f"{id(lcl1)=}, {id(lcl2)=}, {(lcl1 is lcl2)=}")

    @singleton
    class SingletonClsDecTest:
        pass

    cld1 = SingletonClsDecTest()
    cld2 = SingletonClsDecTest()
    print(f"{id(cld1)=}, {id(cld2)=}, {(cld1 is cld2)=}")

    class SingletonClsMetaTest(metaclass=SingletonMetaclass):
        pass

    clm1 = SingletonClsMetaTest()
    clm2 = SingletonClsMetaTest()
    print(f"{id(clm1)=}, {id(clm2)=}, {(clm1 is clm2)=}")


if __name__ == "__main__":
    main()
