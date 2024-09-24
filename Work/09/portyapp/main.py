# Exercise 9.1: Making a simple package
# Exercise 9.2: Making an application directory
# Exercise 9.3: Top-level Scripts

import logging
from porty.report import get_portfolio as report_get_portfolio, read_prices_file as report_read_prices_file, make_report_data as report_make_report_data, print_report as report_print_report, print_table as report_print_table
from porty.ticker import process_real_time_data



logLevel = "DEBUG"
logFormat = '%(asctime)s %(levelname)-8s %(name)-20s %(message)s'
logging.basicConfig(level=logLevel, format=logFormat)


log = logging.getLogger(__name__)


def main(args):
    log.debug(f'args: {args}')
    if(len(args) != 3):
        raise SystemExit(f'Usage: {args[0]} <portfolio_filename> <prices_filename>')
    
    portfolio_filepath = args[1]
    prices_filepath = args[2]

    portfolio = report_get_portfolio(portfolio_filepath)
    report_print_table(portfolio.holdings, formatter='text', columns=['name', 'shares', 'price'])

    prices = report_read_prices_file(prices_filepath)
    report_print_table(prices, formatter='text', columns=['name', 'price'])

    reportData = report_make_report_data(portfolio, prices)
    report_print_report(reportData, 'text')

    process_real_time_data(portfolio)


if __name__ == "__main__":
    try:
        import sys
        main(sys.argv)
    except Exception as ex:
        log.error(f'  >>> EXCEPTION (Catch ALL): Type: "{type(ex)}", "{ex}"')
        SystemExit(-1)
    finally:
        SystemExit(0)
