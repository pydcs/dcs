from dataclasses import dataclass
from typing import Dict, Literal, Optional, Union


@dataclass(frozen=True)
class UnitPropertyDescription:
    # The ID used in the miz file for this property.
    identifier: str

    # The type of control shown in the UI for this property. "label" type properties are
    # not really properties, but text-only lines shown in the mission editor for
    # grouping properties.
    control: Literal[
        "checkbox",
        "comboList",
        "editbox",
        "groupbox",
        "label",
        "slider",
        "spinbox",
    ]

    # The human readable name of this property. When the control is a label,
    # the value may be None to indicate that a blank line should be printed in
    # the mission editor UI.
    label: Optional[str] = None

    # True if the property is only valid for units that have skill set to Player or
    # Client.
    player_only: bool = False

    # The minimum value of the property. Only present for spinbox properties.
    minimum: Optional[int] = None

    # The minimum value of the property. Only present for spinbox properties.
    maximum: Optional[int] = None

    # The default value of the property. Should be defined for all non-label properties.
    default: Optional[Union[bool, float, int, str]] = None

    # A weight adjustment applied to the aircraft when this property is enabled.
    # Only present for boolean values.
    weight_when_on: Optional[float] = None

    # The options allowed for comboList properties. The key of the dict is the ID of the
    # option which is how the value is represented in the miz. The value is the display
    # name for the UI.
    values: Optional[Dict[Union[str, int, float, None], str]] = None

    # No idea what these are for.
    dimension: Optional[str] = None
    x_lbl: Optional[int] = None
    w_ctrl: Optional[int] = None
