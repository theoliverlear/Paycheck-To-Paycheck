from typing import Type, TypeVar

from injector import Injector

T = TypeVar("T")

def injectable(cls: Type[T]):
    def factory(cls: Type[T], injector: Injector) -> T:
        constructor_args = cls.__init__.__annotations__
        dependencies = {}
        for arg_name, arg_type in constructor_args.items():
            if arg_name != 'return':
                dependencies[arg_name] = injector.get(arg_type)
        return cls(**dependencies)
    cls.factory = classmethod(factory)
    return cls