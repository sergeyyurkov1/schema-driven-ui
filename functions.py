import glob
import os
import pathlib
import sys
from importlib.machinery import SourceFileLoader

from ruamel.yaml import YAML

yaml = YAML()

PATH = pathlib.Path(__file__).parent


def get_settings_schemas() -> list[dict]:
    settings_schemas = []

    for i in glob.glob(os.path.join("plugins", "*", "main.py")):
        plugin_name = os.path.dirname(i).split(os.sep)[-1]

        settings_schema = SourceFileLoader(plugin_name, i).load_module().settings_schema

        settings_schemas.append({plugin_name: settings_schema})

    return settings_schemas


def read_yaml(path: str = PATH / "settings.yaml") -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.load(f) or dict()  # if yaml.load(f) returns None
    except FileNotFoundError:
        return dict()


def write_yaml(
    data: dict,
    path: str = PATH / "settings.yaml",
) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(data, f)
    except Exception as e:
        print(str(e))
        sys.exit()


class SettingsMixin:
    """Provides the ability to read and write settings. To be used with Screen, App, or Widget Textual classes"""

    def write_settings(self, key: str, value: str, namespace: str) -> None:
        settings = read_yaml()

        try:
            settings[namespace][key] = value
        except KeyError:
            print("Setting not found. Please check namespace or key.")
        else:
            write_yaml(settings)

    def read_settings(self, key: str, namespace: str) -> any:
        settings = read_yaml()

        try:
            value = settings.get(namespace).get(key)
        except AttributeError:
            print("Setting not found. Please check namespace or key.")
        else:
            return value

    def register_settings(self, new_settings: dict, namespace: str) -> None:
        """Writes (and overwrites) default settings"""

        settings = read_yaml()

        if (
            namespace not in settings  # post new settings
            or len(settings[namespace]) != len(new_settings)  # update old settings
            or settings[namespace].keys() != new_settings.keys()  # update old settings
        ):
            settings.update({namespace: new_settings})

        write_yaml(settings)
