from api.widgets.settings import MySelectionList

settings_schema = {
    "test1": {
        "default_value": [1],
        "type": MySelectionList,
        "options": [1, 2, 3],
    },
}
