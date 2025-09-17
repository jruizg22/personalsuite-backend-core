from importlib.metadata import entry_points

class ModuleManager:
    def __init__(self, app, engine):
        self.app = app
        self.engine = engine
        self.modules = []

    def load_modules(self):
        eps = entry_points(group="personal_suite.modules")
        for ep in eps:
            module_class = ep.load()
            module_instance = module_class(self.app, self.engine)
            self.modules.append(module_instance)

    def register_modules(self):
        for module in self.modules:
            module.register()