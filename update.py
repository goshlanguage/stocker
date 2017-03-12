import argparse
import logging
import sys

import mongoengine

import stocks
from models import Stock

def get_db():
    """
    This is broken out so that it can be mocked in tests
    """
    client = mongoengine.connect()
    db = client.stock
    return db

def get_logger(logpath='/var/log/stocker.log', testing=False):
    logger = logging.getLogger()
    if testing:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
    else:
        handler = logging.FileHandler(logpath)

    logger.addHandler(handler)
    if testing:
        logger.info("Debugging Enabled\n")

    return logger

def update(logger):
    db = get_db()
    user = db.user
    stocklist = Stock.objects()

    for stock in stocklist:
        price = stocks.get_quote(stock.symbol)
        logger.info("Got latest price for {0}:{1}".format(
            stock.symbol,
            price
            )
        )
        try:
            stock.last_price = price
            stock.update(**{"set__last_price":price})
            logger.info("Updated data for {0}:{1}\n".format(
                stock['name'],
                stock['last_price']
                )
            )
        except Exception as e:
            logger.error("Error upating stock {}\n".format(stock['name']))
            logger.error(e.message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l',
        dest='log_path',
        action='store_true',
        help='log path'
    )
    parser.add_argument(
        '-d',
        dest='testing',
        action='store_true',
        help='debug'
    )
    args = parser.parse_args()
    logger = get_logger(logpath=args.log_path, testing=args.testing)
    update(logger)
