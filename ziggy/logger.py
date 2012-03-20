# -*- coding: utf-8 -*-

"""
ziggy.logger
~~~~~~~~

This module provides integration with ziggy and standard python logging module.
:copyright: (c) 2012 by Rhett Garber
:license: ISC, see LICENSE for more details.

"""
import logging
import traceback

from .context import Context

class LogHandler(logging.Handler):
    """Handler to provide log events as ziggy events.

    Records standard fields such as logger name, level the message and if an
    exception was provided, the string formatted exception.

    The type name, if not specified will be something like '<my parent context>.log'
    """
    def __init__(self, name=None):
        super(LogHandler, self).__init__()

        self.name = name

    def emit(self, record):
        with Context(self.name or '.log') as c:
            c.set('name', record.name)
            c.set('level', record.levelname)
            c.set('msg', record.getMessage()) 
            if record.exc_info:
                c.set('exception', ''.join(traceback.format_exception(*record.exc_info)))
