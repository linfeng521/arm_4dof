#include <Servo.h>

Servo myservo[6];
int pwm_port[6]={3,5,6,9,2,7};
int steady_pos[6] = {90,60,180,0,0,0};
int last_pos[6] = {90,60,180,0,0,0};
int distance,stepper;
int i = 0;
void setup() {
  Serial.begin(9600);
  //Serial.println("Servo init successful!!!!starting.......");
  //初始化舵机到稳定位置
  for ( int i = 0; i < 6; ++i ) {
      myservo[i].attach(pwm_port[i],500,2500);
      myservo[i].write(steady_pos[i]);
  }
}

//驱动id对应的舵机到指定的degree位置
void power(int servo_Id,int degree){
  
  distance = degree-last_pos[servo_Id];
  stepper = distance/10;
//  if (distance=0){
//    return 0;
//  }
  //Serial.print("distance:");Serial.print(distance);Serial.print("stepper:");Serial.print(stepper);Serial.print("Servo_id:");Serial.print(servo_Id);
  for (int i = 1;i<11;++i){
      myservo[servo_Id].write(last_pos[servo_Id]+stepper*i);
//      Serial.print("write degree:");Serial.println(last_pos[servo_Id]+stepper*i);
      delay(50);
    }

  Serial.print(servo_Id);Serial.print(":");Serial.print(degree);Serial.print(";");
}
void loop() {
 while (Serial.available() > 0)  
    {
        if(i>5) i=0;
        int degree = Serial.parseInt();
        //Serial.print("Servo id: ");Serial.print(i);Serial.print("LAST servo: ");Serial.println(degree);
        power(i,degree);
        last_pos[i]=degree;
        i++;
    }
    //下次usb数据做准备
   if (i>0){
      //Serial.println("All done");
      i = 0;
   }
}
