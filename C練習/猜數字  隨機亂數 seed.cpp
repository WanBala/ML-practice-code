#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int times,number,min=0,max=100,user;

int main(void){
	srand(time(NULL));
	number=1+(rand()%100);
	for(times=1;;times++){
	printf("��J�@�ӼƦr�A�{�b�϶���%d~%d\n",min,max);
	scanf("%d",&user);
	if(user==number){break;}
	if(user>number){max=user;}
	if(user<number){min=user;}
    }
    printf("���߲q�� �q�����Ƭ�%d",times);
    system("pause");
    return 0;
}

