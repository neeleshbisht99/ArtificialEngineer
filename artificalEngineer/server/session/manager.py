import atexit
import json
import os
from typing import Dict, Callable

from fastapi import WebSocket

from opendevin.logger import opendevin_logger as logger
from .msg_stack import message_stack
from .session import Session

CACHE_DIR = os.getenv('CACHE_DIR', 'cache')
SESSION_CACHE_FILE = os.path.join(CACHE_DIR, 'sessions.json')


class SessionManager:
    _sessions: Dict[str, Session] = {}

    def __init__(self):
        self._load_sessions()
        atexit.register(self.close)

    
    def close(self):
        logger.info('Saving sessions...')
        self._save_sessions()
    
    
    def _save_sessions(self):
        data = {}
        for sid, conn in self._sessions.items():
            data[sid] = {
                'sid': conn.sid,
                'last_active_ts': conn.last_active_ts,
                'is_alive': conn.is_alive
            }
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        with open(SESSION_CACHE_FILE, 'w+') as file:
            json.dump(data, file)
    

    def _load_sessions(self):
        try:
            with open(SESSION_CACHE_FILE, 'r') as file:
                data = json.load(file)
                for sid, sdata in data.items():
                    conn = Session(sid, None)
                    ok = conn.load_from_data(sdata)
                    if ok:
                        self._sessions[sid] = conn
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
