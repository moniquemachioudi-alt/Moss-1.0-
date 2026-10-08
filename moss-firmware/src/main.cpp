// ------------------------------ CAPACITIVE SOIL MOISTURE ------------------------------

/*  GOAL: output clean cvs file

0. To find the ESP32's serial port name 
    run (in terminal): ls /dev/cu.usb* 
    /dev/cu.usbserial-0001
1. to redirect the incoming data stream to the cvs 
    run : cat /dev/cu.usbserial-0001 > ~/Documents/mySideQuests/Moss/data
2. Run the program
3. Look at the sensor_data.csv files 





*/




#include <Arduino.h>

// connected on GPIO34 
const int MOISTURE_PIN = 34;


// established endpoints 
const int AIR_VALUE = 2640;
const int WATER_VALUE = 982;


void setup() {
  Serial.begin(115200);
  delay(1000);

  analogReadResolution(12);
  analogSetPinAttenuation(MOISTURE_PIN, ADC_11db);

  Serial.println("timestamp_ms,raw_adc,voltage_v,moisture_pct");
}




void loop() {
  long sum = 0;
  for (int i = 0; i < 10; i++) {
    sum += analogRead(MOISTURE_PIN);
    delay(10);
  }
  int rawADC = sum / 10;

  float voltage = (rawADC / 4095.0) * 3.3;

  int moisturePercent = map(rawADC, AIR_VALUE, WATER_VALUE, 0, 100);
  moisturePercent = constrain(moisturePercent, 0, 100);

  Serial.print(millis());
  Serial.print(",");
  Serial.print(rawADC);
  Serial.print(",");
  Serial.print(voltage, 2);
  Serial.print(",");
  Serial.println(moisturePercent);

  delay(1000);



  // This loop takes 10 sequential samples spaced 10 milliseconds apart, 
  // sums them together, and computes the mathematical average. 
  // This smooths out voltage spikes into a stable signal.


}








// Test code : blinking LED's
// #include <Arduino.h>

// // Define the GPIO pin connected to the LED
// const int ledPin = 2; 

// void setup() {
//   // Initialize the digital pin as an output
//   pinMode(ledPin, OUTPUT);
// }

// void loop() {
//   digitalWrite(ledPin, HIGH);   // Turn the LED on (HIGH voltage level)
//   delay(1000);                  // Wait for 1 second (1000 milliseconds)
//   digitalWrite(ledPin, LOW);    // Turn the LED off by making the voltage LOW
//   delay(1000);                  // Wait for 1 second
// }