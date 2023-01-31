import itertools
import re
from dataclasses import dataclass
from functools import cached_property
from typing import Any, Dict, List, Sequence, Tuple, Union, cast

ParamValueType = Union[str, int, float, None, List]
ParamsType = Dict[str, ParamValueType]
QueryFragmentLike = Union["QueryFragment", "UniqueName", str]

unique_sequence = itertools.count()


@dataclass
class QueryFragment:
    sql: str
    params: ParamsType

    def __init__(self, sql: Union[str, "QueryFragment", Tuple[str, Any]], params: ParamsType = {}):
        if isinstance(sql, str):
            self.sql = sql
            self._params = params
        elif isinstance(sql, QueryFragment):
            self.sql = sql.sql
            self._params = cast(ParamsType, sql.params)
        else:
            self.sql, self._params = sql

        self._update_sql_with_unique_param_names()

    def format(self, **fragments: QueryFragmentLike) -> "QueryFragment":
        new_params = {**self.params}
        for fragment in fragments.values():
            if isinstance(fragment, QueryFragment):
                new_params.update(fragment.params)

        return QueryFragment(
            self.sql.format(**{key: _get_sql(fragment) for key, fragment in fragments.items()}), new_params
        )

    @staticmethod
    def join(by: str, fragments: Sequence[QueryFragmentLike]) -> "QueryFragment":
        indexed = {f"k{key}": fragment for key, fragment in enumerate(fragments)}
        unformatted_sql = by.join("{" + key + "}" for key in indexed.keys())
        return QueryFragment(unformatted_sql).format(**indexed)

    def _update_sql_with_unique_param_names(self):
        self.params = {}
        for key, value in self._params.items():
            if isinstance(key, UniqueName):
                self.sql = re.sub(f"\\b{re.escape(key.name)}\\b", key.unique_name, self.sql)
                self.params[key.unique_name] = value
            else:
                self.params[key] = value

    def __repr__(self):
        return f"QueryFragment({repr(self.sql)}, {repr(self.params)})"


@dataclass(frozen=True)
class UniqueName(str):
    # :CONVENTION: Prefix these variable names with __ to avoid collisions in sql.
    name: str

    @cached_property
    def unique_name(self):
        return f"{self.name}_{next(unique_sequence)}"


def reset_unique_sequence():
    global unique_sequence
    unique_sequence = itertools.count()


def _get_sql(fragment: QueryFragmentLike) -> str:
    if isinstance(fragment, QueryFragment):
        return fragment.sql
    elif isinstance(fragment, UniqueName):
        return fragment.unique_name
    else:
        return fragment
