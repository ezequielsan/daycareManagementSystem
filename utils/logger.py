import logging
import os

# Create logs directory if it doesn't exist
LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Create a logger instance
logger = logging.getLogger('DaycareManagementSystem')
