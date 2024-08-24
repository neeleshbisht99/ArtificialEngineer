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

from opendevin import config
from opendevin.logger import opendevin_logger as logger
from opendevin.sandbox.sandbox import Sandbox
from opendevin.sandbox.process import Process
from opendevin.sandbox.docker.process import DockerProcess
from opendevin.sandbox.plugins.jupyter import JupyterRequirement
from opendevin.schema import ConfigType
from opendevin.utils import find_available_tcp_port
from opendevin.exceptions import SandboxInvalidBackgroundCommandError


