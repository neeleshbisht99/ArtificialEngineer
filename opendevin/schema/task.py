from enum import Enum

class TaskState(str, Enum):
    INIT = 'init'
    """Initial stte of the task.
    """

    RUNNING = 'running'
    """The task is running.
    """

    PAUSED = 'paused'
    """The task is paused.
    """

    STOPPED = 'stopped'
    """The task is stopped.
    """

    FINISHED = 'finished'
    """The task is finished.
    """

    ERROR = 'error'
    """An error occured during the task.
    """

class TaskStateAction(str, Enum):
    START = 'start'
    """Starts the task.
    """

    PAUSE = 'pause'
    """Pauses the task.
    """

    RESUME = 'resume'
    """ Resumes the task.
    """

    STOP = 'stop'
    """Stops the task.
    """