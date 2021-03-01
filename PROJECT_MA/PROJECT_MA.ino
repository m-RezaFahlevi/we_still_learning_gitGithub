#include <LiquidCrystal.h>
#include <Servo.h>
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
Servo motor;

int noCol = 0;
void setup() {
  // put your setup code here, to run once:
  lcd.begin(16, 2);
  pinMode(7, INPUT);
  motor.attach(9);
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);

  digitalWrite(7, HIGH);
  digitalWrite(A3, HIGH);
  digitalWrite(A4, HIGH);
  digitalWrite(A5, HIGH);
  motor.write(0);

}

void loop() {
  // put your main code here, to run repeatedly:
  motor.write(0);
  int inputButton = digitalRead(7);
  int rightLeaveButton = digitalRead(A3);
  int middleLeaveButton = digitalRead(A4);
  int leftLeaveButton = digitalRead(A5);
  lcd.clear();
  lcd.print("No. table");
  if (inputButton == LOW) {
    noCol++;
    switch (noCol) {
      case 1: 
        motor.write(90);
        digitalWrite(A0, HIGH);
        break;
      case 2: 
        motor.write(90);
        digitalWrite(A1, HIGH);
        break;
      case 3: 
        motor.write(90);
        digitalWrite(A2, HIGH);
        break;
      default:
        digitalWrite(A0, LOW);
        digitalWrite(A1, LOW);
        digitalWrite(A2, LOW);
        noCol = 0;
    }
  }
  lcd.setCursor(0, 1);
  lcd.print("Colums ");
  lcd.print(noCol);
  //motor.write(0);
  delay(1000);
  if (leftLeaveButton == LOW) {
    noCol--;
    digitalWrite(A0, LOW);
  } else if (middleLeaveButton == LOW) {
    noCol--;
    digitalWrite(A1, LOW);
  } else if (rightLeaveButton == LOW) {
    noCol--;
    digitalWrite(A2, LOW);
  }
  if (noCol < 0) {
    noCol = 0;
  }
}
