from textual.app import ComposeResult, Widget
from textual.widgets import (
    Input,
    RadioButton,
    RadioSet,
    Select,
    SelectionList,
    Switch,
)

from functions import SettingsMixin


class MyInput(Input, SettingsMixin):
    def __init__(self, options, *args, **kwargs):
        super().__init__(*args, **kwargs)

        namespace, key = self.name.split(".")
        self.value = self.read_settings(key=key, namespace=namespace)

    def on_mount(self):
        print(self.name)

    def on_input_submitted(self, event):
        namespace, key = self.name.split(".")
        self.write_settings(key=key, value=event.value, namespace=namespace)
        self.notify("Saved.")


class MySwitch(Switch, SettingsMixin):
    def __init__(self, options, *args, **kwargs):
        super().__init__(*args, **kwargs)

        namespace, key = self.name.split(".")
        self.value = self.read_settings(key=key, namespace=namespace)

    def on_mount(self):
        print(self.name)

    def on_switch_changed(self, event):
        namespace, key = self.name.split(".")
        self.write_settings(key=key, value=event.value, namespace=namespace)
        self.notify("Saved.")


class MyRadioSet(Widget, SettingsMixin):
    def __init__(
        self,
        options: list,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        namespace, key = self.name.split(".")
        self.value = self.read_settings(key=key, namespace=namespace)
        self.options = options

    def compose(self) -> ComposeResult:
        with RadioSet():
            index = self.options.index(self.value)
            for e, i in enumerate(self.options):
                if e == index:
                    yield RadioButton(str(i), value=True)
                else:
                    yield RadioButton(str(i))

    def on_mount(self):
        print(self.name)

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        namespace, key = self.name.split(".")
        self.write_settings(
            key=key,
            value=self.options[event.radio_set.pressed_index],
            namespace=namespace,
        )
        self.notify("Saved.")


class MySelectionList(Widget, SettingsMixin):
    def __init__(
        self,
        options: list,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        namespace, key = self.name.split(".")
        self.value = self.read_settings(key=key, namespace=namespace)
        self.options = options

    def compose(self) -> ComposeResult:
        indexes = [self.options.index(i) for i in self.value]
        selection_list = []
        for e, i in enumerate(self.options):
            if e in indexes:
                selection_list.append((str(i), e, True))
            else:
                selection_list.append((str(i), e))
        yield SelectionList(*selection_list)

    def on_mount(self):
        print(self.name)

    def on_selection_list_selected_changed(self):
        namespace, key = self.name.split(".")
        value = [self.options[i] for i in self.query_one(SelectionList).selected]
        self.write_settings(
            key=key,
            value=value,
            namespace=namespace,
        )
        self.notify("Saved.")


class MySelect(Select, SettingsMixin):
    def __init__(self, options: list, *args, **kwargs):
        options = [(str(option), option) for option in options]
        super().__init__(*args, options=options, **kwargs)

        namespace, key = self.name.split(".")
        self.value = self.read_settings(key=key, namespace=namespace)
        self.prompt = str(self.value)

    def on_mount(self):
        print(self.name)

    def on_show(self):
        self.prompt = "Select"

    def on_select_changed(self, event: Select.Changed):
        if event.value == Select.BLANK:
            return
        namespace, key = self.name.split(".")
        self.write_settings(key=key, value=event.value, namespace=namespace)
        self.notify("Saved.")
