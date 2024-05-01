

from opendevin.agent import Agent
from opendevin.schema.task import TaskState


class AgentController:
    id: str
    agent: Agent

    _task_state: TaskState = TaskState.INIT


    async def start(self, task:str):
        """
        Starts the agent controller with a task.
        If task already run before, it will continue from last step.
        """

        self._task_state = TaskState.RUNNING
        await self.notify_task_state_changed()

        self.state = State(Plan(task))

        await self._run()