from lcd2usb import LCD

try:
  lcd = LCD.find_or_die()
  lcd.info()
except NameError:
  print("LCD not found")