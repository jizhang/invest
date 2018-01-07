# -*- coding: utf-8 -*-

import pkgutil
import importlib


def import_submodules(package):
    package = importlib.import_module(package)
    for loader, name, is_pkg in pkgutil.iter_modules(package.__path__):
        importlib.import_module(package.__name__ + '.' + name)
