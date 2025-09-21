from importlib.metadata import entry_points, EntryPoints
from typing import Any

from fastapi import FastAPI
from sqlalchemy import Engine


class ModuleManager:
    """
    Manages the loading and registration of application modules.

    This class is responsible for discovering modules via entry points,
    instantiating them with the application context and engine, and
    registering them.

    Attributes:
        app: The main application instance.
        engine: The database engine so the modules can interact with the database.
        modules (list): A list of loaded module instances.
    """

    def __init__(self, app: FastAPI, engine: Engine) -> None:
        """
        Initializes the ModuleManager with the application and engine.

        Args:
            app: The main FastAPI application instance.
            engine: The SQLAlchemy database engine.
        """
        self.app: FastAPI = app
        self.engine: Engine = engine
        self.modules: list[Any] = []

    def load_modules(self) -> None:
        """
        Loads modules registered under the 'personal_suite.modules' entry point.

        Discovers all entry points in the 'personal_suite.modules' group,
        instantiates each module class with the application and engine,
        and stores the instances in the 'modules' list.

        Raises:
            ImportError: If a module class cannot be loaded.
        """
        eps: EntryPoints = entry_points(group="personal_suite.modules")
        for ep in eps:
            module_class: Any = ep.load()
            module_instance: Any = module_class(self.app, self.engine)
            self.modules.append(module_instance)

    def register_modules(self) -> None:
        """
        Registers all loaded modules.

        Iterates through all module instances in the 'modules' list and calls
        their 'register' method to integrate them into the application.

        Raises:
            AttributeError: If a module does not have a 'register' method.
        """
        for module in self.modules:
            module.register()

    def list_loaded(self):
        return [m.name for m in self.modules]