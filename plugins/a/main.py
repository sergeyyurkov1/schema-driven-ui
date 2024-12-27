from api.widgets.settings import MyRadioSet, MySelect

settings_schema = {
    "test1": {
        "default_value": 1,
        "type": MySelect,
        "options": [1, 2, 3],
    },
    "test2": {
        "default_value": "t1",
        "type": MyRadioSet,
        "options": ["t1", "t2", "t3"],
    },
}
