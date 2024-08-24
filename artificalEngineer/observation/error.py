from dataclasses import dataclass

from opendevin.observation.base import Observation
from opendevin.schema.observation import ObservationType


@dataclass 
class AgentErrorObservation(Observation):
    """
    This observation class represents an error encountered by the agent.
    """

    observation: str= ObservationType.ERROR

    @property
    def message(self) -> str:
        return 'Oops. Something went wrong ' + self.content 
    

    