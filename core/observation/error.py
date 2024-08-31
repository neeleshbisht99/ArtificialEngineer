from dataclasses import dataclass

from artificialEngineer.observation.base import Observation
from artificialEngineer.schema.observation import ObservationType


@dataclass 
class AgentErrorObservation(Observation):
    """
    This observation class represents an error encountered by the agent.
    """

    observation: str= ObservationType.ERROR

    @property
    def message(self) -> str:
        return 'Oops. Something went wrong ' + self.content 
    

    