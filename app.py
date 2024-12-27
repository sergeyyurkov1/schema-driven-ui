from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import (
    Label,
    Rule,
    Static,
)

from api.widgets.settings import MyInput, MySwitch
from functions import SettingsMixin, get_settings_schemas

# 主应用的schema
settings_schema = {
    "main": {
        "test1": {"default_value": False, "type": MySwitch},
        "test2": {"default_value": "test", "type": MyInput},
    },
}


class Demo(App, SettingsMixin):
    CSS_PATH = "app.tcss"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_load(self):
        # 插件的schemas
        settings_schemas = get_settings_schemas()
        for i in settings_schemas:
            settings_schema.update(i)

        for namespace, settings in settings_schema.items():
            default_values = {k: v["default_value"] for k, v in settings.items()}
            self.register_settings(default_values, namespace)

    def compose(self) -> ComposeResult:
        for namespace, settings in settings_schema.items():
            yield Rule()
            yield Label(namespace.upper().replace("_", " "))
            for setting_name, setting in settings.items():
                yield Horizontal(
                    Container(
                        Static(
                            setting_name.split(".")[-1].capitalize().replace("_", " "),
                            classes="label",
                        ),
                        classes="container-1_2",
                    ),
                    Container(
                        setting["type"](
                            options=setting.get("options"),
                            name=f"{namespace}.{setting_name}",
                        ),
                        classes="container-1_2",
                    ),
                    classes="container",
                )


if __name__ == "__main__":
    app = Demo()
    app.run(mouse=True)
