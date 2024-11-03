import importlib
from pathlib import Path

def load_plugins(client):
    plugins_dir = Path(__file__).parent
    for plugin in plugins_dir.glob('*.py'):
        if plugin.name != '__init__.py':
            mod = importlib.import_module(f'plugins.{plugin.stem}')
            if hasattr(mod, 'register'):
                mod.register(client)
