###USES I2C CHAR DISPLAY FOR RASPBERRY PI https://github.com/dcityorg/i2c-char-display-library-raspberrypi

from lcdpi import lcdpi
import time

if __name__ == "__main__":


    LCDADDRESS =    0x27                    # i2c address for the lcd display
    
    lcd = lcdpi("LCD", LCDADDRESS, 2)
    
    
    while 1:
        lcd.clear()
        lcd.cursorMove(1, 3)
        lcd.writeString("Preparing to")
        time.sleep(3)
        lcd.cursorMove(2,1)
        lcd.writeString("tell you a story")
        time.sleep(3)
        lcd.clear()
        lcd.cursorMove(1,3)
        lcd.writeString("About a man")
        time.sleep(3)
        lcd.cursorMove(2,5)
        lcd.writeString("who was")
        time.sleep(3)
        lcd.clear()
        lcd.cursorMove(1,1)
        lcd.writeString("excited to")
        time.sleep(3)
        lcd.cursorMove(2,5)
        lcd.writeString("work but")
        time.sleep(3)
        lcd.clear()
        lcd.cursorMove(1, 3)
        lcd.writeString("stayed up way")
        time.sleep(3)
        lcd.cursorMove(2,3)
        lcd.writeString("too late")
        time.sleep(3)
        lcd.clear()
        lcd.cursorMove(1, 3)
        lcd.writeString("and overslept")
        time.sleep(3)
        lcd.cursorMove(2,3)
        lcd.writeString("and hit snooze")
        time.sleep(3)
        lcd.clear()
        lcd.cursorMove(1, 3)
        lcd.writeString("too often")
        time.sleep(3)
        lcd.cursorMove(2,3)
        lcd.writeString("in a rush")
        time.sleep(3)
        lcd.clear()
        lcd.cursorMove(1, 2)
        lcd.writeString("he made it to")
        time.sleep(3)
        lcd.cursorMove(2,1)
        lcd.writeString("work on time")
        time.sleep(1)
        lcd.writeString("!")
        time.sleep(1)
        lcd.writeString("!")
        time.sleep(1)
        lcd.writeString("!")
        time.sleep(3)
