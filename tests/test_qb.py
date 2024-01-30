from ipyquerybuilder import Field, QueryBuilder


def test_default():
    fields = [
        Field(
            name="firstName",
            label="First Name",
            value_editor_type="text",
        ),
        Field(
            name="instrument",
            label="Plays",
            value_editor_type="multiselect",
            values=["Guitar", "Drums", "Bass", "Other"],
        ),
    ]
    starting_query = {
        "combinator": "and",
        "rules": [
            {"field": "firstName", "operator": "contains", "value": "Steve"},
            {"field": "instrument", "operator": "=", "value": "Guitar"},
        ],
    }
    QueryBuilder(fields=fields, query=starting_query)
