import logging
import requests
import os.path

logger = logging.getLogger(__name__)


def ensure_pdf_source_exists(url, local_name):
    here = os.path.abspath(os.path.dirname(__file__))
    local_path = os.path.join(here, 'local', local_name)
    if os.path.isfile(local_path):
        logger.info('file {} already exists'.format(local_path))
    else:
        logger.info('file {} does not exist, fetching it'.format(local_path))
        response = requests.get(url)
        with open(local_path, 'wb') as f:
            f.write(response.content)
