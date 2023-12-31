import sys
import os
import logging
from epdlib import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

from render import image_test

logging.basicConfig(level=logging.DEBUG)

cal_year = int(sys.argv[1])
cal_month = int(sys.argv[2])

image_test.make_calendar(cal_year, cal_month).save("test_cal.png")
try:
    logging.info("epd7in5_V2 calendar test")
    epd = epd7in5_V2.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    logging.info("read testcal file")
    Himage = Image.open("test_cal.png")
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