import logging

from ._version import get_versions
from .record import RecordPackage, EPICSRecord
from . import pragmas
from . import parser
from . import epics

logger = logging.getLogger(__name__)
__version__ = get_versions()['version']
del get_versions


__all__ = [
    'EPICSRecord',
    'RecordPackage',
    'epics',
    'logger',
    'parser',
    'pragmas',
]
