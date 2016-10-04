# To run this code on CodeBug, visit:
#
#     http://www.codebug.org.uk/learn/activity/66/tethering-codebug-with-python/#step585
#
import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT,
                            IO_PWM_OUTPUT,
                            IO_ANALOG_INPUT)
from codebug_tether.sprites import Sprite
import time

codebug = codebug_tether.CodeBug()
codebug.set_leg_io(0, IO_DIGITAL_INPUT);
codebug.set_leg_io(1, IO_DIGITAL_INPUT);
codebug.set_leg_io(2, IO_DIGITAL_INPUT);
codebug.set_leg_io(3, IO_DIGITAL_INPUT);
codebug.set_leg_io(4, IO_DIGITAL_INPUT);
codebug.set_leg_io(5, IO_DIGITAL_INPUT);
codebug.set_leg_io(6, IO_DIGITAL_INPUT);
codebug.set_leg_io(7, IO_DIGITAL_INPUT);

def build_sprite(rows):
  s = Sprite(5, 5)
  for i in range(5):
    s.set_row(i, rows[i])
  return s


while True:
  if codebug.get_input('A') == 1:
    for count in range(5):
      codebug.scroll_sprite(build_sprite([0b10001,0b10001,0b10101,0b11011,0b10001]), 75/1000, 'L')
      codebug.scroll_sprite(build_sprite([0b01010,0b01010,0b01110,0b01010,0b00100]), 75/1000, 'L')
      codebug.scroll_sprite(build_sprite([0b00100,0b00100,0b00100,0b00100,0b11111]), 75/1000, 'L')
      codebug.scroll_sprite(build_sprite([0b00100,0b00100,0b00100,0b00100,0b11111]), 75/1000, 'L')
      time.sleep(1000/1000);
  elif codebug.get_input('B') == 1:
    codebug.draw_sprite(0, 0, build_sprite([0b01110,0b10001,0b00000,0b01010,0b01010]));
    time.sleep(7000/1000);
  else:
    # interrupts -- and therefore sleep -- not supported in Python
