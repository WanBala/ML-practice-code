#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
int range=-1,number=-1;
void norerand(int);
int main(void){
	srand(time(NULL));
	printf("��J�n�����ƭ��s���ͭȪ��d��:(1~x) ��Jx=?\n");
	scanf("%d",&range);
	printf("��J�n�ư��Ȫ��ƶq\n");
	scanf("%d",&number);
	norerand(range);
	system("pause");
} 
void norerand(int x){
	int buffer1[number]={-1};
	int buffer[x]={-1};
	int y=rand()%x+1;
	printf("�̦��п�J�n�ư�����\n");
	for(int i=0;i<number;i++){
	    scanf("%d",&buffer[i]);
	}
	printf("��J�����A��X���G\n");
	for(int i=number;i<x;i++){
		for(int j=0;j<x;j++){
			
			if(buffer[j]==y){
				y=rand()%x+1;
				j=-1;
			}
		}
		buffer[i]=y;
		printf("%d\n",y);
	}
}

