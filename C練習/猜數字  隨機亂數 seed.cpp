#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int times,number,min=0,max=100,user;

int main(void){
	srand(time(NULL));
	number=1+(rand()%100);
	for(times=1;;times++){
	printf("輸入一個數字，現在區間為%d~%d\n",min,max);
	scanf("%d",&user);
	if(user==number){break;}
	if(user>number){max=user;}
	if(user<number){min=user;}
    }
    printf("恭喜猜中 猜的次數為%d",times);
    system("pause");
    return 0;
}

