import importlib


def resolve_class(module: str, class_name: str):
    module = importlib.import_module(module)
    return getattr(module, class_name)