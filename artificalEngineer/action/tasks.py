from dataclasses import dataclass, field

from .base import ExecutableAction, NotExecutableAction
from artificialEngineer.schema import ActionType
from artificialEngineer.observation import NullObservation

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from artificialEngineer.controller import AgentController


@dataclass
class AddTaskAction(ExecutableAction):
    parent: str
    goal: str
    subtasks: list = field(default_factory=list)
    action: str = ActionType.ADD_TASK

    async def run(self, controller: 'AgentController') -> NullObservation:
        if controller.state is not None:
            controller.state.plan.add_subtask(self.parent, self.goal, self.subtasks)
        return NullObservation('')
    
    @property
    def message(self) -> str:
        return f'Added task: {self.goal}'
    

@dataclass
class ModifyTaskAction(ExecutableAction):
    id: str
    state: str
    action: str = ActionType.MODIFY_TASK

    async def run(self, controller: 'AgentController') -> NullObservation:
        if controller.state is not None:
            controller.state.plan.set_subtask_state(self.id, self.state)
        return NullObservation('')
    
    @property
    def message(self) -> str:
        return f'Set task {self.id} to  {self.state}'
    

@dataclass
class TaskStateChangedAction(NotExecutableAction):
    task_state: str 
    action: str = ActionType.CHANGE_TASK_STATE

    @property 
    def message(self) -> str:
        return f'Task State changed to {self.task_state}'
    
