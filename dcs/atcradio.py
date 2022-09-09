from dataclasses import dataclass


@dataclass(frozen=True)
class AtcRadio:
    hf_hz: int
    vhf_low_hz: int
    vhf_high_hz: int
    uhf_hz: int
