from dataclasses import dataclass, field
from typing import List, Tuple

from artificialEngineer.plan import Plan

from artificialEngineer.action import (
    Action,
)
from artificialEngineer.observation import (
    Observation,
    CmdOutputObservation,
)

@dataclass 
class State:
    plan: Plan
    iteration: int = 0
    # number of character we have sent to and recevied from LLM so far for current task
    num_of_chars: int = 0
    background_command_obs: List[CmdOutputObservation] = field(
        default_factory=list
    )
    history: List[Tuple[Action, Observation]] = field(
        default_factory=list
    )
    updated_info: List[Tuple[Action, Observation]] = field(
        default_factory=list
    )