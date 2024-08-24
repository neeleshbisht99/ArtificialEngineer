from pathlib import Path
from typing import Any, Dict, List

class WorkspaceFile:
    name: str
    childern: List['WorkspaceFile']


    def __init__(self, name:str, children: List['WorkspaceFile']):
        self.name = name
        self.childern = children

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the File object to a dictionary.

        Returns: 
            The dictionary representation of the File Object.
        """

        return {
            'name': self.name,
            'children': [child.to_dict() for child in self.children]
        }

def get_folder_structure(workdir: Path) -> WorkspaceFile:
    """
    Gets the folder structure of a directory.

    Args: 
        workdir: The directory path.

    Returns:
        The folder structure.       
    """

    root = WorkspaceFile(name=workdir.name, children=[])
    for item in workdir.iterdir():
        if item.is_dir():
            dir = get_folder_structure(item)
            if dir.childern:
                root.childern.append(dir)
        else:
            root.childern.append(WorkspaceFile(name=item.name, children=[]))
    return root

