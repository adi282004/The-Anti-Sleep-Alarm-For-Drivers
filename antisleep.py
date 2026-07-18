// Project: Anti sleep alarm for drivers
// YouTube Channel: SKR Electronics Lab
// Channel Link: https://youtube.com/@skr_electronics_lab
// Instagram Link: https://www.instagram.com/skr_electronics_lab

// Component's required - 1. Arduinos UNO or Nano
//                        2. Eyel blink sensor
//                        3. Relay module
//                        4. BO motor with wheel
//                        5. Buzzer
//                        6. Switch -2 pieces
//                        7. 9v Battery - 2 pieces
//                        8. 9v Battery Cap - 2 pieces
//                        9. Some wires

// Connection's -

//              Eye blink sensor -
//              Connect Eye blink sensor VCC (+) - with Arduino 5v pin
//              Connect Eye blink sensor GND (-) - with Arduino GND pin
//              Connect Eye blink sensor Do (Out) - with Arduino D2 pin

//              Relay module -
//              Connect Relay module VCC (+)- with Arduino 5v pin
//              Connect Relay module GND (-)- with Arduino GND pin
//              Connect Relay module In (Input)- with Arduino D8 pin

//              Buzzer -
//              Connect Buzzer (+) - with Arduino D9 pin
//              Connect Buzzer (-) - with Arduino GND pin

//              1st Battery -
//              Connect 9v battery (+) with Arduino VIN pin through a switch
//              Connect 9v battery (-) with Arduino GND pin

//              2nd Battery and BO motor -
//              Connect 9v battery (+) with Relay module COM pin through a switch
//              Connect BO motor(+)with Relay module NO pin
//              Connect 9v battery (-) with BO motor (-)



const int sensorPin = 2;  // Pin connected to the IR sensor (or eye detection sensor)
const int motorPin = 8;   // Pin connected to the motor
const int buzzerPin = 9;  // Pin connected to the buzzer

long time; // Variable to store time

void setup() {
 pinMode(motorPin, OUTPUT); // Set motorPin as an OUTPUT
 pinMode(buzzerPin, OUTPUT); // Set buzzerPin as an OUTPUT
 pinMode(sensorPin, INPUT); // Set sensorPin as an INPUT
 digitalWrite(motorPin, HIGH); // Turn on the motor initially
}

void loop(){
// Check if the IR sensor (sensorPin) is triggered (LOW means it's triggered)
if (!digitalRead(sensorPin)){
 time = millis(); // Record the current time

 // Keep checking if the IR sensor is still triggered
 while (!digitalRead(sensorPin)) }
    // When the IR sensor is triggered, turn off the buzzer and turn on the motor and wait for 1 second
    digitalWrite(buzzerPin, LOW);
    digitalWrite(motorPin,HIGH);
    delay(1000);
  }
 }else {
// If the IR sensor is not triggered (eyes open)

// Check the time elapsed since the sensor was last triggered
  if(TimeDelay()>= 3){
   digitalWrite(buzzerPin, HIGH); // If 3 seconds have passed, turn on the buzzer
   }
   if(TimeDelay()>= 4){
    digitalWrite(motorPin, LOW); // If 4 second have passed, turn off the motor
  }
 }
}

int TimeDelay(){
 long t = millis()- time; // Calculate the time elapsed since the IR sensor was triggered
 t = t / 1000; // Convert milliseconds to seconds
return t; // Return the elapsed time in seconds
}