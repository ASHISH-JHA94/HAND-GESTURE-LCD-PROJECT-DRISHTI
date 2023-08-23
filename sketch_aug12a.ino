#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    lcd.init();       // Initialize the LCD
    lcd.backlight();  // Turn on the backlight (if supported by your module)
    lcd.setCursor(0, 0);
    lcd.print("Hello, LCD!");
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0){
    char input = Serial.read();

      if(input == '1'){

        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Victory <3");
      }

      else if(input == '2'){
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Lose ( ͡° ͜ʖ ͡°)");
      }

      else if(input == '3'){
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Thumbs Up");
      }

      else if(input == '4'){
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Pain :[");
      }

      else if(input == '5'){
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Thumbs Down");
      }

      else if(input == '6'){
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Thief!");
      }

      else if(input == '7'){
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Smile :‑)");
      }

      else if(input == '8'){
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Call Me ;‑)");
      }
  }
    // lcd.clear();
    // lcd.setCursor(0, 1);
    // lcd.print("MUDRA");
    //delay(1000); // Delay before refreshing the display
}