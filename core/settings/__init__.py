from .base import *
from .ckeeditor_config import *

try :
    from .local import *
except:
    pass

from .production import *