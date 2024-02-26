import os
import sys
import asyncio

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.core import SyncCore
from queries.orm import SyncOrm

SyncOrm.create_tables()
# SyncCore.create_tables()

# SyncCore.insert_data()
SyncOrm.insert_data()

# SyncCore.select_workers()
SyncOrm.select_workers()

# SyncCore.update_worker()
SyncOrm.update_worker()
