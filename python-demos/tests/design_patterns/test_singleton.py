from design_patterns.singleton import LazySingletonCls, SingletonCls, SingletonMetaclass, singleton


def test_singleton_cls() -> None:
    cl1 = SingletonCls()
    cl2 = SingletonCls()
    assert id(cl1) == id(cl2)
    assert cl1 is cl2


def test_lazy_singleton_cls() -> None:
    lcl1 = LazySingletonCls.get_instance()
    lcl2 = LazySingletonCls.get_instance()
    assert id(lcl1) == id(lcl2)
    assert lcl1 is lcl2


def test_singleton_decorator() -> None:
    @singleton
    class SingletonClsDecTest:
        pass

    cl1 = SingletonClsDecTest()
    cl2 = SingletonClsDecTest()
    assert id(cl1) == id(cl2)
    assert cl1 is cl2


def test_singleton_metaclass() -> None:
    class SingletonClsMet(metaclass=SingletonMetaclass):
        pass

    cl1 = SingletonClsMet()
    cl2 = SingletonClsMet()
    assert id(cl1) == id(cl2)
    assert cl1 is cl2
