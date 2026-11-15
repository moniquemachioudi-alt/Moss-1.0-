#include <Arduino.h>
#include <WiFi.h>
#include <time.h>

#include <OneWire.h>            // for DS18B20 Soil Temperature Sensor
#include <DallasTemperature.h>  // for DS18B20 Soil Temperature Sensor
#include <BH1750.h>             // for BH1750 Light Sensor 
#include <Adafruit_AHTX0.h>     // for AHT20 Air Humid. and Temp Sensor


// =================== HOW IT SENDS DATA TO THE FAST API ===================

/*  GOAL: output clean cvs file

0. To find the ESP32's serial port name 
    run (in terminal): ls /dev/cu.usb* 
    /dev/cu.usbserial-0001
1. to redirect the incoming data stream to the cvs 
    run : cat /dev/cu.usbserial-0001 > ~/Documents/mySideQuests/Moss/data
2. Run the program
3. Look at the sensor_data.csv files 
*/

// PIN 2     : Blue LED => blinks when it records data 
// PIN 34    : Capacitive Soil Moisture
// PIN 18    : DS18B20 Soil Temperature Sensor
// PIN 21/22 : BH1750 Light Sensor 
//           : AHT20 Air Humidity + Temp
//           : OLED screen

// set up the WIFI 
const char* WIFI_SSID = "TP-Link_A5E4";
const char* WIFI_PASS = "16067332";

const int bluePin = 2;  
const int SOIL_MOIS_PIN = 34;
const int SOIL_TEMP_PIN = 18;

const int NUM_SAMPLES = 10;

// measured calibrated endpoints
// const int AIR_VALUE = 2640;
// const int WATER_VALUE = 982;


// ================ BINARY FORMAT DATE & TIME ================
time_t get_time_binary() {
  time_t now;
  time(&now);  // Writes current real-world Unix timestamp into 'now'
  return now;
}



BH1750 lightMeter; // Light Sensor
Adafruit_AHTX0 air_temp_rh; // Air Temp/Humid Sensor
OneWire soilsTemp_wire(SOIL_TEMP_PIN);                // DS18B20 Soil Temperature
DallasTemperature soilTemp_sensor(&soilsTemp_wire);   


// Find the Median of NUM_SAMPLES ADC reads
// Why? One bad reading can't skew it (so use this instead of an average).
int readMoistureMedian() {
  int samples[NUM_SAMPLES];
  for (int i=0; i < NUM_SAMPLES; i++) {
    samples[i] = analogRead(SOIL_MOIS_PIN);
    delay(5);
  }

  // sort the array in ascending order
  for (int i=0; i < NUM_SAMPLES; i++) {
    int key = samples[i];
    int j = i-1;
    while (j>=0 && samples[j] > key) {
      samples [j+1] = samples[j];
      j--;
    }
    samples[j+1] = key;
  }
  return samples [NUM_SAMPLES/2];
}




void setup() {
  Serial.begin(115200);
  delay(1000);

  // 1. Configure ADC for Moisture Probe
  analogReadResolution(12);                           // make it 12 bit range aka, 0-4095
  analogSetPinAttenuation(SOIL_MOIS_PIN, ADC_11db);   // scale down the incoming voltage so it can safely read higher analog signals.

  // 2. Configure DS18B20 Soil Temperature
  soilTemp_sensor.begin();

  // 3. Initialize the BH1750 Light Sensor 
  Wire.begin(21, 22);
  lightMeter.begin();
  air_temp_rh.begin();



  // Make the LED blink when recording data 
  pinMode(bluePin, OUTPUT);   // pushing electricity OUT to power things
  digitalWrite(bluePin, LOW); // start with low



  // 1. Connect to WIFI
  Serial.print("CONNECTING TO WIFI");
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi Connected! IP: " + WiFi.localIP().toString());

  // 2. Sync Unix timestamp via NTP
  configTime(0, 0, "pool.ntp.org", "time.nist.gov");


  // what you see in the Serial Monitor
  Serial.println("recorded_at, ELAPSED_TIME_s, raw_adc, soil_temp_c, light_lux, air_temp_c, air_rh_pct");

}





void loop() {

  // configure the LED pin, s.t. it blinks blue whenever data is collecting
  digitalWrite(bluePin, HIGH);

  // // 0. Get the date and time (NO WIFI)
  // time_t time_binary = get_time_binary();

  // 0. Get the date and time (WITH WIFI)
  time_t now;
  time(&now);

  // 1. Read Soil Moisture
  int rawADC = readMoistureMedian();
  // float voltage = (rawADC / 4095.0) * 3.3;

  // 2. Read Soil Temperature (°C)
  soilTemp_sensor.requestTemperatures();
  float soilTempC = soilTemp_sensor.getTempCByIndex(0);

  // 3. Ambient Light (Lux)
  float lux = lightMeter.readLightLevel();

  // 4. Air Temp (°C) and Humidity (%) 
  sensors_event_t humidity, temp;
  air_temp_rh.getEvent(&humidity, &temp);
  float airTempC = temp.temperature;
  float airRH = humidity.relative_humidity;


  // Print the exact JSON payload you will soon POST to FastAPI
  String payload = "{";
  payload += "\"recorded_at\":" + String((long)now) + ",";
  payload += "\"ELAPSED_TIME_s\":" + String(millis()) + ",";
  payload += "\"raw_adc\":" + String(rawADC) + ",";
  payload += "\"soil_temp_c\":" + String(soilTempC, 2) + ",";
  payload += "\"light_lux\":" + String(lux, 1) + ",";
  payload += "\"air_temp_c\":" + String(airTempC, 2) + ",";
  payload += "\"air_rh_pct\":" + String(airRH, 2);
  payload += "}";

  Serial.println(payload);


  // WHEN USING CSV
  // Serial.print(time_binary);
  // Serial.print(",");
  // Serial.print(millis());
  // Serial.print(",");
  // Serial.print(rawADC);
  // // Serial.print(",");
  // // Serial.print(voltage, 2);
  // // Serial.print(",");
  // // Serial.print(moisturePercent);
  // Serial.print(",");
  // Serial.print(soilTempC, 2);
  // Serial.print(",");
  // Serial.print(lux, 1);
  // Serial.print(",");
  // Serial.print(airTempC, 2);
  // Serial.print(",");
  // Serial.println(airRH, 2);


  // turn off the LED after one cycle
  digitalWrite(bluePin, LOW);
  delay(2000);
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