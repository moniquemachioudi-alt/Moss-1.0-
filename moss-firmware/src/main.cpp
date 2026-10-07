#include <Arduino.h>

// Moss Soil Moisture Sensor on ADC1 (GPIO 34)
const int MOISTURE_PIN = 34;

void setup() {
  Serial.begin(115200);
  delay(1000);

  // 12-bit ADC: 0 to 4095
  analogReadResolution(12);
  analogSetPinAttenuation(MOISTURE_PIN, ADC_11db);

  Serial.println("======================================");
  Serial.println("ESP32 Capacitive Moisture Sensor Test");
  Serial.println("======================================");
}

void loop() {
  int rawADC = analogRead(MOISTURE_PIN);
  float voltage = (rawADC / 4095.0) * 3.3;

  Serial.print("Raw ADC Value: ");
  Serial.print(rawADC);
  Serial.print("  |  Signal Voltage: ");
  Serial.print(voltage, 2);
  Serial.println(" V");

  delay(1000);
}