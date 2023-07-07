# generated by datamodel-codegen:
#   filename:  schema.json

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Extra, Field


class MathGroupTypeIndex(float, Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2
    number_3 = 3
    number_4 = 4


class AggregationAxisFormat(str, Enum):
    numeric = "numeric"
    duration = "duration"
    duration_ms = "duration_ms"
    percentage = "percentage"
    percentage_scaled = "percentage_scaled"


class BaseMathType(str, Enum):
    total = "total"
    dau = "dau"
    weekly_active = "weekly_active"
    monthly_active = "monthly_active"
    unique_session = "unique_session"


class BreakdownAttributionType(str, Enum):
    first_touch = "first_touch"
    last_touch = "last_touch"
    all_events = "all_events"
    step = "step"


class BreakdownType(str, Enum):
    cohort = "cohort"
    person = "person"
    event = "event"
    group = "group"
    session = "session"


class ChartDisplayType(str, Enum):
    ActionsLineGraph = "ActionsLineGraph"
    ActionsLineGraphCumulative = "ActionsLineGraphCumulative"
    ActionsAreaGraph = "ActionsAreaGraph"
    ActionsTable = "ActionsTable"
    ActionsPie = "ActionsPie"
    ActionsBar = "ActionsBar"
    ActionsBarValue = "ActionsBarValue"
    WorldMap = "WorldMap"
    BoldNumber = "BoldNumber"


class CohortPropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: str = Field("id", const=True)
    label: Optional[str] = None
    type: str = Field("cohort", const=True)
    value: float


class CountPerActorMathType(str, Enum):
    avg_count_per_actor = "avg_count_per_actor"
    min_count_per_actor = "min_count_per_actor"
    max_count_per_actor = "max_count_per_actor"
    median_count_per_actor = "median_count_per_actor"
    p90_count_per_actor = "p90_count_per_actor"
    p95_count_per_actor = "p95_count_per_actor"
    p99_count_per_actor = "p99_count_per_actor"


class DatabaseSchemaQueryResponseField(BaseModel):
    class Config:
        extra = Extra.forbid

    chain: Optional[List[str]] = None
    fields: Optional[List[str]] = None
    key: str
    table: Optional[str] = None
    type: str


class DateRange(BaseModel):
    class Config:
        extra = Extra.forbid

    date_from: Optional[str] = None
    date_to: Optional[str] = None


class Key(str, Enum):
    tag_name = "tag_name"
    text = "text"
    href = "href"
    selector = "selector"


class ElementType(BaseModel):
    class Config:
        extra = Extra.forbid

    attr_class: Optional[List[str]] = None
    attr_id: Optional[str] = None
    attributes: Dict[str, str]
    href: Optional[str] = None
    nth_child: Optional[float] = None
    nth_of_type: Optional[float] = None
    order: Optional[float] = None
    tag_name: str
    text: Optional[str] = None


class EmptyPropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: Optional[Any] = None
    operator: Optional[Any] = None
    type: Optional[Any] = None
    value: Optional[Any] = None


class EntityType(str, Enum):
    actions = "actions"
    events = "events"
    new_entity = "new_entity"


class Person(BaseModel):
    class Config:
        extra = Extra.forbid

    distinct_ids: List[str]
    is_identified: Optional[bool] = None
    properties: Dict[str, Any]


class EventType(BaseModel):
    class Config:
        extra = Extra.forbid

    distinct_id: str
    elements: List[ElementType]
    elements_chain: Optional[str] = None
    event: str
    id: str
    person: Optional[Person] = None
    properties: Dict[str, Any]
    timestamp: str
    uuid: Optional[str] = None


class MathGroupTypeIndex1(float, Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2
    number_3 = 3
    number_4 = 4


class Response(BaseModel):
    class Config:
        extra = Extra.forbid

    next: Optional[str] = None
    results: List[EventType]


class EventsQueryResponse(BaseModel):
    class Config:
        extra = Extra.forbid

    columns: List
    hasMore: Optional[bool] = None
    results: List[List]
    types: List[str]


class FilterLogicalOperator(str, Enum):
    AND = "AND"
    OR = "OR"


class FunnelConversionWindowTimeUnit(str, Enum):
    second = "second"
    minute = "minute"
    hour = "hour"
    day = "day"
    week = "week"
    month = "month"


class FunnelLayout(str, Enum):
    horizontal = "horizontal"
    vertical = "vertical"


class FunnelPathType(str, Enum):
    funnel_path_before_step = "funnel_path_before_step"
    funnel_path_between_steps = "funnel_path_between_steps"
    funnel_path_after_step = "funnel_path_after_step"


class FunnelStepRangeEntityFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    custom_name: Optional[str] = None
    funnel_from_step: Optional[float] = None
    funnel_to_step: Optional[float] = None
    id: Optional[Union[str, float]] = None
    index: Optional[float] = None
    name: Optional[str] = None
    order: Optional[float] = None
    type: Optional[EntityType] = None


class FunnelStepReference(str, Enum):
    total = "total"
    previous = "previous"


class FunnelVizType(str, Enum):
    steps = "steps"
    time_to_convert = "time_to_convert"
    trends = "trends"


class FunnelCorrelationPersonConverted(str, Enum):
    true = "true"
    false = "false"


class HogQLNotice(BaseModel):
    class Config:
        extra = Extra.forbid

    end: Optional[float] = None
    fix: Optional[str] = None
    message: str
    start: Optional[float] = None


class HogQLQueryResponse(BaseModel):
    class Config:
        extra = Extra.forbid

    clickhouse: Optional[str] = None
    columns: Optional[List] = None
    hogql: Optional[str] = None
    query: Optional[str] = None
    results: Optional[List] = None
    types: Optional[List] = None


class IntervalType(str, Enum):
    hour = "hour"
    day = "day"
    week = "week"
    month = "month"


class LifecycleToggle(str, Enum):
    new = "new"
    resurrecting = "resurrecting"
    returning = "returning"
    dormant = "dormant"


class PathCleaningFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    alias: Optional[str] = None
    regex: Optional[str] = None


class PathType(str, Enum):
    field_pageview = "$pageview"
    field_screen = "$screen"
    custom_event = "custom_event"
    hogql = "hogql"


class PathsFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    edge_limit: Optional[float] = None
    end_point: Optional[str] = None
    exclude_events: Optional[List[str]] = None
    funnel_filter: Optional[Dict[str, Any]] = None
    funnel_paths: Optional[FunnelPathType] = None
    include_event_types: Optional[List[PathType]] = None
    local_path_cleaning_filters: Optional[List[PathCleaningFilter]] = None
    max_edge_weight: Optional[float] = None
    min_edge_weight: Optional[float] = None
    path_dropoff_key: Optional[str] = None
    path_end_key: Optional[str] = None
    path_groupings: Optional[List[str]] = None
    path_replacements: Optional[bool] = None
    path_start_key: Optional[str] = None
    path_type: Optional[PathType] = None
    paths_hogql_expression: Optional[str] = None
    start_point: Optional[str] = None
    step_limit: Optional[float] = None


class PropertyMathType(str, Enum):
    avg = "avg"
    sum = "sum"
    min = "min"
    max = "max"
    median = "median"
    p90 = "p90"
    p95 = "p95"
    p99 = "p99"


class PropertyOperator(str, Enum):
    exact = "exact"
    is_not = "is_not"
    icontains = "icontains"
    not_icontains = "not_icontains"
    regex = "regex"
    not_regex = "not_regex"
    gt = "gt"
    gte = "gte"
    lt = "lt"
    lte = "lte"
    is_set = "is_set"
    is_not_set = "is_not_set"
    is_date_exact = "is_date_exact"
    is_date_before = "is_date_before"
    is_date_after = "is_date_after"
    between = "between"
    not_between = "not_between"
    min = "min"
    max = "max"


class RecentPerformancePageViewNode(BaseModel):
    class Config:
        extra = Extra.forbid

    dateRange: DateRange
    kind: str = Field("RecentPerformancePageViewNode", const=True, description="Performance")
    response: Optional[Dict[str, Any]] = Field(None, description="Cached query response")


class RecordingDurationFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: str = Field("duration", const=True)
    label: Optional[str] = None
    operator: PropertyOperator
    type: str = Field("recording", const=True)
    value: float


class RetentionReference(str, Enum):
    total = "total"
    previous = "previous"


class RetentionPeriod(str, Enum):
    Hour = "Hour"
    Day = "Day"
    Week = "Week"
    Month = "Month"


class RetentionType(str, Enum):
    retention_recurring = "retention_recurring"
    retention_first_time = "retention_first_time"


class SavedInsightNode(BaseModel):
    class Config:
        extra = Extra.forbid

    kind: str = Field("SavedInsightNode", const=True)
    shortId: str


class SessionPropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: str = Field("$session_duration", const=True)
    label: Optional[str] = None
    operator: PropertyOperator
    type: str = Field("session", const=True)
    value: Optional[Union[str, float, List[Union[str, float]]]] = None


class ShownAsValue(str, Enum):
    Volume = "Volume"
    Stickiness = "Stickiness"
    Lifecycle = "Lifecycle"


class StepOrderValue(str, Enum):
    strict = "strict"
    unordered = "unordered"
    ordered = "ordered"


class StickinessFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    compare: Optional[bool] = None
    display: Optional[ChartDisplayType] = None
    hidden_legend_indexes: Optional[List[float]] = None
    show_legend: Optional[bool] = None
    show_values_on_series: Optional[bool] = None
    shown_as: Optional[ShownAsValue] = None
    stickiness_days: Optional[float] = None


class TimeToSeeDataSessionsQueryResponse(BaseModel):
    class Config:
        extra = Extra.forbid

    results: List[Dict[str, Any]]


class TrendsFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    aggregation_axis_format: Optional[AggregationAxisFormat] = None
    aggregation_axis_postfix: Optional[str] = None
    aggregation_axis_prefix: Optional[str] = None
    breakdown_histogram_bin_count: Optional[float] = None
    compare: Optional[bool] = None
    display: Optional[ChartDisplayType] = None
    formula: Optional[str] = None
    hidden_legend_indexes: Optional[List[float]] = None
    show_legend: Optional[bool] = None
    show_values_on_series: Optional[bool] = None
    shown_as: Optional[ShownAsValue] = None
    smoothing_intervals: Optional[float] = None


class Breakdown(BaseModel):
    class Config:
        extra = Extra.forbid

    normalize_url: Optional[bool] = None
    property: Union[str, float]
    type: BreakdownType


class BreakdownFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    breakdown: Optional[Union[str, float, List[Union[str, float]]]] = None
    breakdown_group_type_index: Optional[float] = None
    breakdown_histogram_bin_count: Optional[float] = None
    breakdown_normalize_url: Optional[bool] = None
    breakdown_type: Optional[BreakdownType] = None
    breakdowns: Optional[List[Breakdown]] = None


class ElementPropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: Key
    label: Optional[str] = None
    operator: PropertyOperator
    type: str = Field("element", const=True)
    value: Optional[Union[str, float, List[Union[str, float]]]] = None


class EventPropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: str
    label: Optional[str] = None
    operator: PropertyOperator
    type: str = Field("event", const=True, description="Event properties")
    value: Optional[Union[str, float, List[Union[str, float]]]] = None


class FeaturePropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: str
    label: Optional[str] = None
    operator: PropertyOperator
    type: str = Field("feature", const=True, description='Event property with "$feature/" prepended')
    value: Optional[Union[str, float, List[Union[str, float]]]] = None


class FunnelsFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    bin_count: Optional[Union[float, str]] = None
    breakdown_attribution_type: Optional[BreakdownAttributionType] = None
    breakdown_attribution_value: Optional[float] = None
    drop_off: Optional[bool] = None
    entrance_period_start: Optional[str] = None
    exclusions: Optional[List[FunnelStepRangeEntityFilter]] = None
    funnel_advanced: Optional[bool] = None
    funnel_aggregate_by_hogql: Optional[str] = None
    funnel_correlation_person_converted: Optional[FunnelCorrelationPersonConverted] = None
    funnel_correlation_person_entity: Optional[Dict[str, Any]] = None
    funnel_custom_steps: Optional[List[float]] = None
    funnel_from_step: Optional[float] = None
    funnel_order_type: Optional[StepOrderValue] = None
    funnel_step: Optional[float] = None
    funnel_step_breakdown: Optional[Union[str, List[float], float]] = None
    funnel_step_reference: Optional[FunnelStepReference] = None
    funnel_to_step: Optional[float] = None
    funnel_viz_type: Optional[FunnelVizType] = None
    funnel_window_interval: Optional[float] = None
    funnel_window_interval_unit: Optional[FunnelConversionWindowTimeUnit] = None
    hidden_legend_breakdowns: Optional[List[str]] = None
    layout: Optional[FunnelLayout] = None


class GroupPropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    group_type_index: Optional[float] = None
    key: str
    label: Optional[str] = None
    operator: PropertyOperator
    type: str = Field("group", const=True)
    value: Optional[Union[str, float, List[Union[str, float]]]] = None


class HogQLMetadataResponse(BaseModel):
    class Config:
        extra = Extra.forbid

    errors: List[HogQLNotice]
    inputExpr: Optional[str] = None
    inputSelect: Optional[str] = None
    isValid: Optional[bool] = None
    notices: List[HogQLNotice]
    warnings: List[HogQLNotice]


class HogQLPropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: str
    label: Optional[str] = None
    type: str = Field("hogql", const=True)
    value: Optional[Union[str, float, List[Union[str, float]]]] = None


class HogQLQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    kind: str = Field("HogQLQuery", const=True)
    query: str
    response: Optional[HogQLQueryResponse] = Field(None, description="Cached query response")


class LifecycleFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    show_values_on_series: Optional[bool] = None
    shown_as: Optional[ShownAsValue] = None
    toggledLifecycles: Optional[List[LifecycleToggle]] = None


class PersonPropertyFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    key: str
    label: Optional[str] = None
    operator: PropertyOperator
    type: str = Field("person", const=True, description="Person properties")
    value: Optional[Union[str, float, List[Union[str, float]]]] = None


class RetentionFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    period: Optional[RetentionPeriod] = None
    retention_reference: Optional[RetentionReference] = None
    retention_type: Optional[RetentionType] = None
    returning_entity: Optional[Dict[str, Any]] = None
    target_entity: Optional[Dict[str, Any]] = None
    total_intervals: Optional[float] = None


class TimeToSeeDataSessionsQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    dateRange: Optional[DateRange] = Field(None, description="Date range for the query")
    kind: str = Field("TimeToSeeDataSessionsQuery", const=True)
    response: Optional[TimeToSeeDataSessionsQueryResponse] = Field(None, description="Cached query response")
    teamId: Optional[float] = Field(None, description="Project to filter on. Defaults to current project")


class DatabaseSchemaQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    kind: str = Field("DatabaseSchemaQuery", const=True)
    response: Optional[Dict[str, List[DatabaseSchemaQueryResponseField]]] = Field(
        None, description="Cached query response"
    )


class EventsNode(BaseModel):
    class Config:
        extra = Extra.forbid

    custom_name: Optional[str] = None
    event: Optional[str] = Field(None, description="The event or `null` for all events.")
    fixedProperties: Optional[
        List[
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ]
        ]
    ] = Field(
        None,
        description="Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
    )
    kind: str = Field("EventsNode", const=True)
    limit: Optional[float] = None
    math: Optional[Union[BaseMathType, PropertyMathType, CountPerActorMathType, str, str]] = None
    math_group_type_index: Optional[MathGroupTypeIndex1] = None
    math_hogql: Optional[str] = None
    math_property: Optional[str] = None
    name: Optional[str] = None
    orderBy: Optional[List[str]] = Field(None, description="Columns to order by")
    properties: Optional[
        List[
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ]
        ]
    ] = Field(None, description="Properties configurable in the interface")
    response: Optional[Response] = Field(None, description="Return a limited set of data")


class EventsQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    actionId: Optional[int] = Field(None, description="Show events matching a given action")
    after: Optional[str] = Field(None, description="Only fetch events that happened after this timestamp")
    before: Optional[str] = Field(None, description="Only fetch events that happened before this timestamp")
    event: Optional[str] = Field(None, description="Limit to events matching this string")
    fixedProperties: Optional[
        List[
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ]
        ]
    ] = Field(
        None,
        description="Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
    )
    kind: str = Field("EventsQuery", const=True)
    limit: Optional[int] = Field(None, description="Number of rows to return")
    offset: Optional[int] = Field(None, description="Number of rows to skip before returning rows")
    orderBy: Optional[List[str]] = Field(None, description="Columns to order by")
    personId: Optional[str] = Field(None, description="Show events for a given person")
    properties: Optional[
        List[
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ]
        ]
    ] = Field(None, description="Properties configurable in the interface")
    response: Optional[EventsQueryResponse] = Field(None, description="Cached query response")
    select: List[str] = Field(..., description="Return a limited set of data. Required.")
    where: Optional[List[str]] = Field(None, description="HogQL filters to apply on returned data")


class HogQLMetadata(BaseModel):
    class Config:
        extra = Extra.forbid

    expr: Optional[str] = None
    kind: str = Field("HogQLMetadata", const=True)
    response: Optional[HogQLMetadataResponse] = Field(None, description="Cached query response")
    select: Optional[str] = None


class PersonsNode(BaseModel):
    class Config:
        extra = Extra.forbid

    cohort: Optional[float] = None
    distinctId: Optional[str] = None
    fixedProperties: Optional[
        List[
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ]
        ]
    ] = Field(
        None,
        description="Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
    )
    kind: str = Field("PersonsNode", const=True)
    limit: Optional[float] = None
    offset: Optional[float] = None
    properties: Optional[
        List[
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ]
        ]
    ] = Field(None, description="Properties configurable in the interface")
    response: Optional[Dict[str, Any]] = Field(None, description="Cached query response")
    search: Optional[str] = None


class PropertyGroupFilterValue(BaseModel):
    class Config:
        extra = Extra.forbid

    type: FilterLogicalOperator
    values: List[
        Union[
            PropertyGroupFilterValue,
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ],
        ]
    ]


class ActionsNode(BaseModel):
    class Config:
        extra = Extra.forbid

    custom_name: Optional[str] = None
    fixedProperties: Optional[
        List[
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ]
        ]
    ] = Field(
        None,
        description="Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
    )
    id: float
    kind: str = Field("ActionsNode", const=True)
    math: Optional[Union[BaseMathType, PropertyMathType, CountPerActorMathType, str, str]] = None
    math_group_type_index: Optional[MathGroupTypeIndex] = None
    math_hogql: Optional[str] = None
    math_property: Optional[str] = None
    name: Optional[str] = None
    properties: Optional[
        List[
            Union[
                EventPropertyFilter,
                PersonPropertyFilter,
                ElementPropertyFilter,
                SessionPropertyFilter,
                CohortPropertyFilter,
                RecordingDurationFilter,
                GroupPropertyFilter,
                FeaturePropertyFilter,
                HogQLPropertyFilter,
                EmptyPropertyFilter,
            ]
        ]
    ] = Field(None, description="Properties configurable in the interface")
    response: Optional[Dict[str, Any]] = Field(None, description="Cached query response")


class DataTableNode(BaseModel):
    class Config:
        extra = Extra.forbid

    allowSorting: Optional[bool] = Field(
        None, description="Can the user click on column headers to sort the table? (default: true)"
    )
    columns: Optional[List[str]] = Field(
        None, description="Columns shown in the table, unless the `source` provides them."
    )
    expandable: Optional[bool] = Field(None, description="Can expand row to show raw event data (default: true)")
    full: Optional[bool] = Field(None, description="Show with most visual options enabled. Used in scenes.")
    hiddenColumns: Optional[List[str]] = Field(
        None, description="Columns that aren't shown in the table, even if in columns or returned data"
    )
    kind: str = Field("DataTableNode", const=True)
    propertiesViaUrl: Optional[bool] = Field(None, description="Link properties via the URL (default: false)")
    showActions: Optional[bool] = Field(None, description="Show the kebab menu at the end of the row")
    showColumnConfigurator: Optional[bool] = Field(
        None, description="Show a button to configure the table's columns if possible"
    )
    showDateRange: Optional[bool] = Field(None, description="Show date range selector")
    showElapsedTime: Optional[bool] = Field(None, description="Show the time it takes to run a query")
    showEventFilter: Optional[bool] = Field(
        None, description="Include an event filter above the table (EventsNode only)"
    )
    showExport: Optional[bool] = Field(None, description="Show the export button")
    showHogQLEditor: Optional[bool] = Field(None, description="Include a HogQL query editor above HogQL tables")
    showOpenEditorButton: Optional[bool] = Field(
        None, description="Show a button to open the current query as a new insight. (default: true)"
    )
    showPropertyFilter: Optional[bool] = Field(None, description="Include a property filter above the table")
    showReload: Optional[bool] = Field(None, description="Show a reload button")
    showSavedQueries: Optional[bool] = Field(None, description="Shows a list of saved queries")
    showSearch: Optional[bool] = Field(None, description="Include a free text search field (PersonsNode only)")
    source: Union[
        EventsNode, EventsQuery, PersonsNode, RecentPerformancePageViewNode, HogQLQuery, TimeToSeeDataSessionsQuery
    ] = Field(..., description="Source of the events")


class PropertyGroupFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    type: FilterLogicalOperator
    values: List[PropertyGroupFilterValue]


class RetentionQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    aggregation_group_type_index: Optional[float] = Field(None, description="Groups aggregation")
    dateRange: Optional[DateRange] = Field(None, description="Date range for the query")
    filterTestAccounts: Optional[bool] = Field(
        None, description="Exclude internal and test users by applying the respective filters"
    )
    kind: str = Field("RetentionQuery", const=True)
    properties: Optional[
        Union[
            List[
                Union[
                    EventPropertyFilter,
                    PersonPropertyFilter,
                    ElementPropertyFilter,
                    SessionPropertyFilter,
                    CohortPropertyFilter,
                    RecordingDurationFilter,
                    GroupPropertyFilter,
                    FeaturePropertyFilter,
                    HogQLPropertyFilter,
                    EmptyPropertyFilter,
                ]
            ],
            PropertyGroupFilter,
        ]
    ] = Field(None, description="Property filters for all series")
    retentionFilter: Optional[RetentionFilter] = Field(None, description="Properties specific to the retention insight")
    samplingFactor: Optional[float] = Field(None, description="Sampling rate")


class StickinessQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    aggregation_group_type_index: Optional[float] = Field(None, description="Groups aggregation")
    dateRange: Optional[DateRange] = Field(None, description="Date range for the query")
    filterTestAccounts: Optional[bool] = Field(
        None, description="Exclude internal and test users by applying the respective filters"
    )
    interval: Optional[IntervalType] = Field(
        None, description="Granularity of the response. Can be one of `hour`, `day`, `week` or `month`"
    )
    kind: str = Field("StickinessQuery", const=True)
    properties: Optional[
        Union[
            List[
                Union[
                    EventPropertyFilter,
                    PersonPropertyFilter,
                    ElementPropertyFilter,
                    SessionPropertyFilter,
                    CohortPropertyFilter,
                    RecordingDurationFilter,
                    GroupPropertyFilter,
                    FeaturePropertyFilter,
                    HogQLPropertyFilter,
                    EmptyPropertyFilter,
                ]
            ],
            PropertyGroupFilter,
        ]
    ] = Field(None, description="Property filters for all series")
    samplingFactor: Optional[float] = Field(None, description="Sampling rate")
    series: List[Union[EventsNode, ActionsNode]] = Field(..., description="Events and actions to include")
    stickinessFilter: Optional[StickinessFilter] = Field(
        None, description="Properties specific to the stickiness insight"
    )


class TrendsQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    aggregation_group_type_index: Optional[float] = Field(None, description="Groups aggregation")
    breakdown: Optional[BreakdownFilter] = Field(None, description="Breakdown of the events and actions")
    dateRange: Optional[DateRange] = Field(None, description="Date range for the query")
    filterTestAccounts: Optional[bool] = Field(
        None, description="Exclude internal and test users by applying the respective filters"
    )
    interval: Optional[IntervalType] = Field(
        None, description="Granularity of the response. Can be one of `hour`, `day`, `week` or `month`"
    )
    kind: str = Field("TrendsQuery", const=True)
    properties: Optional[
        Union[
            List[
                Union[
                    EventPropertyFilter,
                    PersonPropertyFilter,
                    ElementPropertyFilter,
                    SessionPropertyFilter,
                    CohortPropertyFilter,
                    RecordingDurationFilter,
                    GroupPropertyFilter,
                    FeaturePropertyFilter,
                    HogQLPropertyFilter,
                    EmptyPropertyFilter,
                ]
            ],
            PropertyGroupFilter,
        ]
    ] = Field(None, description="Property filters for all series")
    samplingFactor: Optional[float] = Field(None, description="Sampling rate")
    series: List[Union[EventsNode, ActionsNode]] = Field(..., description="Events and actions to include")
    trendsFilter: Optional[TrendsFilter] = Field(None, description="Properties specific to the trends insight")


class FunnelsQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    aggregation_group_type_index: Optional[float] = Field(None, description="Groups aggregation")
    breakdown: Optional[BreakdownFilter] = Field(None, description="Breakdown of the events and actions")
    dateRange: Optional[DateRange] = Field(None, description="Date range for the query")
    filterTestAccounts: Optional[bool] = Field(
        None, description="Exclude internal and test users by applying the respective filters"
    )
    funnelsFilter: Optional[FunnelsFilter] = Field(None, description="Properties specific to the funnels insight")
    interval: Optional[IntervalType] = Field(
        None, description="Granularity of the response. Can be one of `hour`, `day`, `week` or `month`"
    )
    kind: str = Field("FunnelsQuery", const=True)
    properties: Optional[
        Union[
            List[
                Union[
                    EventPropertyFilter,
                    PersonPropertyFilter,
                    ElementPropertyFilter,
                    SessionPropertyFilter,
                    CohortPropertyFilter,
                    RecordingDurationFilter,
                    GroupPropertyFilter,
                    FeaturePropertyFilter,
                    HogQLPropertyFilter,
                    EmptyPropertyFilter,
                ]
            ],
            PropertyGroupFilter,
        ]
    ] = Field(None, description="Property filters for all series")
    samplingFactor: Optional[float] = Field(None, description="Sampling rate")
    series: List[Union[EventsNode, ActionsNode]] = Field(..., description="Events and actions to include")


class LifecycleQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    aggregation_group_type_index: Optional[float] = Field(None, description="Groups aggregation")
    dateRange: Optional[DateRange] = Field(None, description="Date range for the query")
    filterTestAccounts: Optional[bool] = Field(
        None, description="Exclude internal and test users by applying the respective filters"
    )
    interval: Optional[IntervalType] = Field(
        None, description="Granularity of the response. Can be one of `hour`, `day`, `week` or `month`"
    )
    kind: str = Field("LifecycleQuery", const=True)
    lifecycleFilter: Optional[LifecycleFilter] = Field(None, description="Properties specific to the lifecycle insight")
    properties: Optional[
        Union[
            List[
                Union[
                    EventPropertyFilter,
                    PersonPropertyFilter,
                    ElementPropertyFilter,
                    SessionPropertyFilter,
                    CohortPropertyFilter,
                    RecordingDurationFilter,
                    GroupPropertyFilter,
                    FeaturePropertyFilter,
                    HogQLPropertyFilter,
                    EmptyPropertyFilter,
                ]
            ],
            PropertyGroupFilter,
        ]
    ] = Field(None, description="Property filters for all series")
    samplingFactor: Optional[float] = Field(None, description="Sampling rate")
    series: List[Union[EventsNode, ActionsNode]] = Field(..., description="Events and actions to include")


class PathsQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    aggregation_group_type_index: Optional[float] = Field(None, description="Groups aggregation")
    dateRange: Optional[DateRange] = Field(None, description="Date range for the query")
    filterTestAccounts: Optional[bool] = Field(
        None, description="Exclude internal and test users by applying the respective filters"
    )
    kind: str = Field("PathsQuery", const=True)
    pathsFilter: Optional[PathsFilter] = Field(None, description="Properties specific to the paths insight")
    properties: Optional[
        Union[
            List[
                Union[
                    EventPropertyFilter,
                    PersonPropertyFilter,
                    ElementPropertyFilter,
                    SessionPropertyFilter,
                    CohortPropertyFilter,
                    RecordingDurationFilter,
                    GroupPropertyFilter,
                    FeaturePropertyFilter,
                    HogQLPropertyFilter,
                    EmptyPropertyFilter,
                ]
            ],
            PropertyGroupFilter,
        ]
    ] = Field(None, description="Property filters for all series")
    samplingFactor: Optional[float] = Field(None, description="Sampling rate")


class InsightVizNode(BaseModel):
    class Config:
        extra = Extra.forbid

    full: Optional[bool] = Field(None, description="Show with most visual options enabled. Used in insight scene.")
    kind: str = Field("InsightVizNode", const=True)
    showCorrelationTable: Optional[bool] = None
    showHeader: Optional[bool] = None
    showLastComputation: Optional[bool] = None
    showLegendButton: Optional[bool] = None
    showTable: Optional[bool] = None
    source: Union[TrendsQuery, FunnelsQuery, RetentionQuery, PathsQuery, StickinessQuery, LifecycleQuery]


class Model(BaseModel):
    __root__: Union[
        DataTableNode,
        SavedInsightNode,
        InsightVizNode,
        TrendsQuery,
        FunnelsQuery,
        RetentionQuery,
        PathsQuery,
        StickinessQuery,
        LifecycleQuery,
        RecentPerformancePageViewNode,
        TimeToSeeDataSessionsQuery,
        DatabaseSchemaQuery,
        Union[EventsNode, EventsQuery, ActionsNode, PersonsNode, HogQLQuery, HogQLMetadata, TimeToSeeDataSessionsQuery],
    ]


PropertyGroupFilterValue.update_forward_refs()
