void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  byte incomingbyte;

  if (Serial.available() > 0) {
    incomingbyte = Serial.read();

    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    digitalWrite(7, LOW);

    switch (incomingbyte) {
      case '0': break;
      case '1': digitalWrite(2, HIGH); break;
      case '2': digitalWrite(3, HIGH); break;
      case '3': digitalWrite(4, HIGH); break;
      case '4': digitalWrite(5, HIGH); break;
      case '5': digitalWrite(6, HIGH); break;
      case '6': digitalWrite(7, HIGH); break;
      default:
        digitalWrite(2, HIGH);
        digitalWrite(3, HIGH);
        digitalWrite(4, HIGH);
        digitalWrite(5, HIGH);
        digitalWrite(6, HIGH);
        digitalWrite(7, HIGH);
        break;
    }
  }
}
