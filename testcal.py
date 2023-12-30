import sys
import os
import logging
from epdlib import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

from render import image_test

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5_V2 calendar test")
    epd = epd7in5_V2.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    logging.info("read testcal file")
    img = image_test.make_calendar(2023, 12)
    Himage = Image.open(img)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit(cleanup=True)
    exit()