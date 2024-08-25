from dataclasses import dataclass
from typing import List

from artificialEngineer.observation.base import Observation
from artificialEngineer.schema.observation import ObservationType


@dataclass
class CmdOutputObservation(Observation):
    """
    This data class represents output of a command.
    """

    command_id: int
    command: str
    exit_code: int = 0
    observation: str = ObservationType.RUN
    
    @property
    def error(self) -> bool:
        return self.exit_code != 0

    @property
    def message(self) -> str:
        return f'Command `{self.command}` executed with exit code {self.exit_code}.'


