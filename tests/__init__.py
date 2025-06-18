import logging
logging.basicConfig(
        format="%(asctime)s : %(name)s : %(levelname)s : %(message)s",
        level=logging.ERROR,
    )
logging.debug('Start Here')
logging.info('Test Info')
logging.warning('End Here')
logging.error('Opps')