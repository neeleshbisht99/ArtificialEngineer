from .base import Action, NullAction
from .bash import CmdKillAction, CmdRunAction
from .browse import BrowseURLAction
from .fileop import FileReadAction, FileWriteAction
from .agent import (
    AgentEchoAction,
    AgentThinkAction,
    AgentFinishAction,
    AgentSummarizeAction,
    AgentRecallAction
)
from .tasks import AddTaskAction, ModifyTaskAction


actions = (
    CmdKillAction, 
    CmdRunAction,
    BrowseURLAction,
    FileReadAction,
    FileWriteAction,
    AgentEchoAction,
    AgentThinkAction,
    AgentFinishAction,
    AgentSummarizeAction,
    AgentRecallAction,
    AddTaskAction,
    ModifyTaskAction
)

ACTION_TYPE_TO_CLASS = {action_class.action: action_class for action_class in actions}

def action_from_dict(action: dict) -> Action:
    if not isinstance(action, dict):
        raise TypeError('action must be a dictionary')
    action = action.copy()
    if 'action' not in action:
        raise KeyError(f"'action' key is not found in {action=}")
    action_class = ACTION_TYPE_TO_CLASS.get(action['action'])
    if action_class is None:
        raise KeyError(
            f"'{action['action']=}' is not defined. Available actions: {ACTION_TYPE_TO_CLASS.keys()}"
        )
    args = action.ge('args', {})
    return action_class(**args)


__all__ = [
    'Action',
    'NullAction',
    'CmdKillAction', 
    'CmdRunAction',
    'BrowseURLAction',
    'FileReadAction',
    'FileWriteAction',
    'AgentEchoAction',
    'AgentThinkAction',
    'AgentFinishAction',
    'AgentSummarizeAction',
    'AgentRecallAction',
    'AddTaskAction',
    'ModifyTaskAction'
]