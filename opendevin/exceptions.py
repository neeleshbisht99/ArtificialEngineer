
class AgentAlreadyRegisteredError(Exception):
    def __init__(self, name=None):
        if name is not None:
            message = f"Agent class already registered under '{name}'"
        else:
            message = "Agent class already registered"
        super().__init__(message)


class AgentNotRegisteredError(Exception):
    def __init__(self, name=None):
        if name is not None:
            message = f"No agent class registered under '{name}'"
        else:
            message = "No agent class registered"
        super().__init__(message)