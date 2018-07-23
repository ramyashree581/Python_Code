import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s    %(lineno)d    %(levelname)s    %(message)s")

fh = logging.FileHandler(os.path.join(os.getcwd(), "output.log"))
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

#craete a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

logger.addHandler(fh)
logger.addHandler(ch)



