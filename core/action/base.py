from dataclasses import dataclass, asdict
from typing import TYPE_CHECKING
from artificialEngineer.schema import ActionType

if TYPE_CHECKING:
    from artificialEngineer.controller import AgentController
    from artificialEngineer.observation import Observation

@dataclass
class Action:
    async def run(self, controller: 'AgentController') -> 'Observation':
        raise NotImplementedError
    
    def to_memory(self):
        d = asdict(self)
        try:
            v = d.pop('action')
        except KeyError:
            raise NotImplementedError(f'{self=} does not have action attribute set')
        return {'action':v, 'args':d}
    
    def to_dict(self):
        d = self.to_memory()
        d['message'] = self.message
        return d
    
    @property
    def executable(self) -> bool:
        raise NotImplementedError
    
    @property
    def message(self) -> str:
        raise NotImplementedError
    

@dataclass
class ExecutableAction(Action):
    @property
    def executable(self) -> bool:
        return True
    
@dataclass
class NotExecutableAction(Action):
    @property
    def executable(self) -> bool:
        return False
    
@dataclass
class NullAction(NotExecutableAction):
    """
    An action that does nothing.
    This is used when the agent need to recevie user followup messages from the frontend.
    """

    action: str = ActionType.NULL

    @property
    def message(self) -> str:
        return 'No Action'