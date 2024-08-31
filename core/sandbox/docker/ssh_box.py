import atexit
import os
import platform
import sys
import time
import uuid
import tarfile
from glob import glob
from collections import namedtuple
from typing import Dict, List, Tuple, Union

import docker
from pexpect import pxssh

from artificialEngineer import config
from artificialEngineer.logger import artificialEngineer_logger as logger
from artificialEngineer.sandbox.sandbox import Sandbox
from artificialEngineer.sandbox.process import Process
from artificialEngineer.sandbox.docker.process import DockerProcess
from artificialEngineer.sandbox.plugins.jupyter import JupyterRequirement
from artificialEngineer.schema import ConfigType
from artificialEngineer.utils import find_available_tcp_port
from artificialEngineer.exceptions import SandboxInvalidBackgroundCommandError


