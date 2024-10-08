from dataclasses import dataclass
from typing import TYPE_CHECKING

from .base import ExecutableAction
from artificialEngineer.schema import ActionType

if TYPE_CHECKING:
    from artificialEngineer.controller import AgentController
    from artificialEngineer.observation import CmdOutputObservation


@dataclass
class CmdRunAction(ExecutableAction):
    command: str
    background: bool = False
    action: str = ActionType.RUN

    async def run(self, controller: 'AgentController') -> 'CmdOutputObservation':
        return controller.action_manager.run_command(self.command, self.background)
    
    @property
    def message(self) -> str:
        return f'Running command: {self.command}'
    

@dataclass
class CmdKillAction(ExecutableAction):
    id: int
    action: str = ActionType.KILL

    async def run(self, controller: 'AgentController') -> 'CmdOutputObservation':
        return controller.action_manager.kill_command(self.id)
    

    @property
    def mesage(self) -> str:
        return f'Killing command: {self.id}'
    
