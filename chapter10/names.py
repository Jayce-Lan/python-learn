import logging
import logging.config
import os

from name_function import get_formatted_name

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

log.info('Enter \'q\' at any time to quit')
while True:
    first = input('please enter your first name: ')
    if first.lower() == 'q':
        break
    last = input('please enter your last name: ')
    if last.lower() == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    log.info(f'Formatted name: {formatted_name}')
