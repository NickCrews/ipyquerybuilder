import dataclasses
from pathlib import Path
from typing import Any, Iterable, Literal

import ipyreact
import traitlets


@dataclasses.dataclass(frozen=True)
class Field:
    """Describes a field in a database table, and possible ways to filter on that field.

    Wrapper around the Field interface from `react-querybuilder`:
    https://react-querybuilder.js.org/docs/typescript#fields
    """

    name: str
    label: str
    operators: list[dict[str, Any]] | None = None
    value_editor_type: Literal[
        "text",
        "select",
        "checkbox",
        "radio",
        "textarea",
        "multiselect",
        "date",
        "datetime-local",
        "time",
        "field",
    ] | None = None
    input_type: Literal[
        "button",
        "checkbox",
        "color",
        "date",
        "datetime-local",
        "email",
        "file",
        "hidden",
        "image",
        "month",
        "number",
        "password",
        "radio",
        "range",
        "reset",
        "search",
        "submit",
        "tel",
        "text",
        "time",
        "url",
        "week",
    ] | None = None
    """@type attribute for the <input /> rendered by ValueEditor, e.g. 'text', 'number', or 'date'"""  # noqa
    values: list[Any] | None = None
    """Array of value options, applicable when valueEditorType is 'select', 'radio', or 'multiselect'"""  # noqa
    default_operator: str | None = None
    default_value: Any | None = None
    placeholder: str | None = None
    """Placeholder text for the value editor when this field is selected"""

    def to_dict(self):
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, d):
        if isinstance(d, cls):
            return d
        return cls(**d)


class QueryBuilder(ipyreact.ReactWidget):
    """An ipyreact widget wrapping the JS `react-querybuilder` component."""

    _esm = Path(__file__).parent / "_qb.jsx"

    _fields = traitlets.List(traitlets.Dict()).tag(sync=True)
    _query = traitlets.Dict().tag(sync=True)
    show_not_toggle = traitlets.Bool(False).tag(sync=True)

    def __init__(
        self,
        fields: Iterable[Field],
        *,
        query: dict[str, Any] = None,
        show_not_toggle: bool = True,
    ):
        super().__init__()
        self.fields = fields
        self.query = query
        self.show_not_toggle = show_not_toggle

    @property
    def fields(self) -> list[Field]:
        """List of Field definitions for the QueryBuilder component."""
        return [Field.from_dict(d) for d in self._fields]

    @fields.setter
    def fields(self, fields: list[Field]):
        self._fields = [Field.from_dict(f).to_dict() for f in fields]

    @property
    def query(self) -> dict[str, Any]:
        return self._query

    @query.setter
    def query(self, query: dict[str, Any]):
        self._query = query
