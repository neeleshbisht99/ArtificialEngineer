import copy
from dataclasses import dataclass
from artificialEngineer.schema import ObservationType


@dataclass
class Observation:
    """
    This data class represents an observation of the environment.
    """

    content: str

    def __str__(self) -> str:
        return self.content
    
    def to_memory(self) -> dict:
        """Converts the observation to a dictionary"""
        extras = copy.deepcopy(self.__dict__)
        content = extras.pop('content', '')
        observation = extras.pop('observation', '')

        return {
            'extras': extras,
            'content': content,
            'observation': observation
        }


    def to_dict(self) -> dict:
        """Converts the observation to a dictionary and adds user message."""
        memory_dict = self.to_memory()
        memory_dict['message'] = self.message
        return memory_dict


    @property
    def message(self) -> str:
        """Return a message describing the observation."""
        return ''
    

@dataclass
class NullObservation(Observation):
    """
    This data class represents a null observation.
    This is used when the produced action is NOT executable.
    """

    observation: str = ObservationType.NULL

    @property
    def message(self) -> str:
        return ''