
const byte IR = A0;
const byte CMD_READ_IR = 1;

long prev_t = 0;
int ir_val = 100;
byte cmd_id = 0;

String result="";

void setup() {
  // put your setup code here, to run once:
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
      result = result + ir_val;
      Serial.println(result);
      result = "";
      break;
    break;
  }
}
