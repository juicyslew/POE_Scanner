#include <Servo.h>

Servo h_servo;
Servo v_servo;
void setup() {
  // put your setup code here, to run once:
  h_servo.attach(3);
  v_servo.attach(5);
}

void loop() {
  // put your main code here, to run repeatedly:
  h_servo.write(90);
  v_servo.write(90);
  delay(20);
}
