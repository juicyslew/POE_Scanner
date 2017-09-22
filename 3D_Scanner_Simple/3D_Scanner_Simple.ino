#include <Servo.h>

const byte IR = A0;
const byte CMD_READ_IR = 1;
const byte h_maxpos = 120;
const byte h_minpos = 60;
const byte v_maxpos = 120;
const byte v_minpos = 60;
const byte stoptime = 100;
const byte h_step = 1;
const byte v_step = 5;

long prev_t = 0;
int ir_val = 100;
byte cmd_id = 0;
bool h_forward = 1;
bool v_forward = 1;
byte h_pos = h_minpos;
byte v_pos = v_minpos;

String result="";

Servo h_servo;  // create servo object to control a servo
Servo v_servo;
// twelve servo objects can be created on most boards

void setup() {
  h_servo.attach(3);  // attaches the servo on pin 3 to the servo object
  v_servo.attach(5);
  Serial.begin(9600);
}

void loop() {
    // put your main code here, to run repeatedly:
  ir_val = analogRead(IR);

  if(Serial.available() > 0) {
    cmd_id = Serial.read();
  } else {
    cmd_id = 0;
  }

  switch(cmd_id){
    case CMD_READ_IR:
      result = result + ir_val + "|" + h_pos + "|" + v_pos;
      Serial.println(result);
      result = "";
      break;
    break;
  }
  
  if(millis()-prev_t > stoptime){
    // in steps of 1 degree
    h_servo.write(h_pos);              // tell servo to go to position in variable 'pos'
    if (h_forward){
      h_pos += h_step;
    }else{
      h_pos -= h_step;
    }
    if (h_pos == h_forward * (h_maxpos-h_minpos) + h_minpos){
      v_servo.write(v_pos);
      if (v_forward){
        v_pos += v_step;
      }else{
        v_pos -= v_step;
      }
      delay(50);
      if (v_pos == v_forward * (v_maxpos-v_minpos) + v_minpos){
        v_forward = !v_forward;
      }
      h_forward = !h_forward;
    }
    prev_t = millis();
  }
}
