#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
from datetime import datetime, time
import time

def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (days, hours, minutes, seconds)

leaving_date = datetime.strptime('2020-01-17 16:20:00', '%Y-%m-%d %H:%M:%S')


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        red = graphics.Color(255, 0, 0)
        blue = graphics.Color(0, 0, 255)
      while True:
          now = datetime.now()
          counter = "%d hours, %d minutes, %d seconds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, leaving_date))
          graphics.DrawText(canvas, font, 2, 10, blue, counter)
          time.sleep(1)
          canvas.Clear()
        
        

        time.sleep(10)   # show display for 10 seconds before exit


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
