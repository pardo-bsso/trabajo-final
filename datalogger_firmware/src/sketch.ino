#include "High_Temp.h"

volatile char sample = 0;

HighTemp ht(A1, A0);

void setup()
{
    Serial.begin(115200);

    analogReference(EXTERNAL);
    ht.setAnalogReference(3.3);
    ht.begin();

    pinMode(13, OUTPUT);
    pinMode(2, OUTPUT);
    pinMode(12, INPUT);
    digitalWrite(12, HIGH);
    digitalWrite(13, LOW);

    digitalWrite(2, HIGH);
    delay(500);
    Serial.print("Offset: ");
    Serial.println( ht.getOffset() );
    digitalWrite(2, LOW);
    delay(500);

    cli();

    TCCR1A = 0;
    TCCR1B = 0;
    TCCR1B |= (1 << WGM12);
    TCCR1B |= (1 << CS12);
    // XXX fudge factor para tener 20 samples/seg. en nuestra placa.
    OCR1A = 3124 + 90;
    TIMSK1 |= (1 << OCIE1A);

    sei();
}

ISR (TIMER1_COMPA_vect)
{
    sample = 1;
}

void loop()
{
    while (1) {
      while (!sample) {
      }
      sample = 0;

      digitalWrite(13, HIGH);
      ht.getRoomTmp();
      Serial.print(ht.getThmc());
      Serial.print(' ');
      Serial.println(1 - digitalRead(12));
      digitalWrite(13, LOW);
    }
}

