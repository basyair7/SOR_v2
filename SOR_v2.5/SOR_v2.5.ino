/* NAME PROJECT : SWITCH ON ALL REMOTE PC
 * Creator      : Basyair7
 * powered by arduino
 */

char koneksi_app = 0;
int saklar_1 = 4;
int saklar_2 = 2;
int saklar_3 = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(saklar_1, OUTPUT);
  pinMode(saklar_2, OUTPUT);
  pinMode(saklar_3, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  koneksi_app = int(Serial.read());

  //process in saklar 1
  // on
  if(koneksi_app == '0'){
    digitalWrite(saklar_1, HIGH);
  }

  // off
  else if(koneksi_app == '1'){
    digitalWrite(saklar_1, LOW);
  }

  //process in saklar 2
  // on
  else if(koneksi_app == '2'){
    digitalWrite(saklar_2, HIGH);
  }

  // off 
  else if(koneksi_app == '3'){
    digitalWrite(saklar_2, LOW);
  }

  //process in saklar 3
  // on
  else if(koneksi_app == '4'){
    digitalWrite(saklar_3, HIGH);
  }

  // off
  else if(koneksi_app == '5'){
    digitalWrite(saklar_3, LOW);
  }

  // on all saklar
  else if(koneksi_app == '6'){
    digitalWrite(saklar_1, HIGH);
    digitalWrite(saklar_2, HIGH);
    digitalWrite(saklar_3, HIGH);
  }

  // off all saklar
  else if(koneksi_app == '7'){
    digitalWrite(saklar_1, LOW);
    digitalWrite(saklar_2, LOW);
    digitalWrite(saklar_3, LOW);
  }

}
