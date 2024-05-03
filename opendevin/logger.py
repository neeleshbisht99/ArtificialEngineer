import logging
import os
import sys
import traceback
from datetime import datetime
from opendevin import config
from typing import Literal, Mapping
from termcolor import colored

DISABLE_COLOR_PRINTING = (
    config.get('DISABLE_COLOR').lower() == 'true'
)



ColorType = Literal[
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'light_grey',
    'dark_grey',
    'light_red',
    'light_green',
    'light_yellow',
    'light_blue',
    'light_magenta',
    'light_cyan',
    'white',
]

LOG_COLORS: Mapping[str, ColorType] = {
    'BACKGROUND_LOG': 'blue',
    'ACTION': 'green',
    'OBSERVATION': 'yellow',
    'INFO': 'cyan',
    'ERROR': 'red',
    'PLAN': 'light_magenta',
}



class ColoredFormatter(logging.Formatter):
    def format(self, record):
        msg_type = record.__dict__.get('msg_type', None)
        if msg_type in LOG_COLORS and not DISABLE_COLOR_PRINTING:
            msg_type_color = colored(msg_type, LOG_COLORS[msg_type])
            msg = colored(record.msg, LOG_COLORS[msg_type])
            time_str = colored(self.formatTime(record, self.datefmt), LOG_COLORS[msg_type])
            name_str = colored(record.name, 'cyan')
            level_str = colored(record.levelName, 'yellow')
            if msg_type in ['ERROR', 'INFO']:
                return f'{time_str} - {name_str}:{level_str}: {record.filename}:{record.lineno}\n{msg_type_color}\n{msg}'
            return f'{time_str} - {msg_type_color}\n{msg}'
        elif msg_type == 'STEP':
            msg = '\n\n===============\n' + record.msg + '\n'
            return f'{msg}'
        return super.format(record)

console_formatter = ColoredFormatter(
    '\033[92m%(asctime)s - %(name)s:%(levelname)s\033[0m: %(filename)s:%(lineno)s - %(message)s',
    datefmt='%H:%M:%S',
)

file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s:%(levelname)s: %(filename)s:%(lineno)s - %(message)s',
    datefmt='%H:%M:%S',
)

llm_formatter = logging.Formatter(
    '%(message)s'
)

