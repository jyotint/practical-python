import logging
import csv
from .follow import follow


log = logging.getLogger(__name__)

def update_portfolio(rows):
    pass

def filter_data(rows):
    pass

def parse_stock_data(lines):
    pass

def process_real_time_data(portfolio):
    log.info(f'Starting real time data processing...')
    lines = follow('../Data/stocklog.csv')
    rows = parse_stock_data(lines)
    rows = filter_data(rows)
    update_portfolio(rows)
