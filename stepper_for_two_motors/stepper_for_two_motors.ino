// Stepper motor run code with a4988 driver
// by Superb

const int stepPin1 = 3;
int dirPin1 = 4; 
const int stepPin2 = 6;
int dirPin2 = 7; 

int stepDelay=2000;

void setup() {
  pinMode(stepPin1,OUTPUT);
  pinMode(dirPin1,OUTPUT);
  pinMode(stepPin2,OUTPUT);
  pinMode(dirPin2,OUTPUT);


}

void loop() {

  digitalWrite(dirPin1, HIGH);

  previous = reading;

  digitalWrite(stepPin1, HIGH);
  delayMicroseconds(stepDelay);
  digitalWrite(stepPin1, LOW);
  delayMicroseconds(stepDelay);

  digitalWrite(stepPin2, HIGH);
  delayMicroseconds(stepDelay);
  digitalWrite(stepPin2, LOW);
  delayMicroseconds(stepDelay);
  
}
