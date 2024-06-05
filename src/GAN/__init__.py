import logging
from rich.logging import RichHandler
import os 
logging_str = '[%(asctime)s:%(levelname)s:%(module)s: %(message)s]'

logs = 'logs'
log_filepath = os.path.join(logs,'running_logs.log')
os.makedirs(logs, exist_ok=True)

logging.basicConfig(
    level=logging.NOTSET,
    format=logging_str,
   handlers=[
       RichHandler()
   ]
)
log = logging.getLogger(__name__)
