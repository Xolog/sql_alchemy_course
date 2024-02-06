import os
import sys
import asyncio

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.orm import create_tables, insert_data

create_tables()
asyncio.run(insert_data())
