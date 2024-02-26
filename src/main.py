import os
import sys
import asyncio

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.orm import SyncOrm
from queries.core import SyncCore
from models import ResumeOrm, Workload

SyncOrm.create_tables()
# SyncCore.create_tables()

# SyncCore.insert_data()
SyncOrm.insert_data([
    ResumeOrm(title='Python Junior Developer', compensation=50000, workload=Workload.fulltime, worker_id=1),
    ResumeOrm(title='Python Разработчик', compensation=150000, workload=Workload.fulltime, worker_id=1),
    ResumeOrm(title='Python Data Engineer', compensation=250000, workload=Workload.parttime, worker_id=2),
    ResumeOrm(title='Data Scientist', compensation=300000, workload=Workload.fulltime, worker_id=2),
])

# SyncCore.select_workers()
SyncOrm.select_workers()

# SyncCore.update_worker()
SyncOrm.update_worker()

SyncOrm.select_resumes_avg_compensation()
