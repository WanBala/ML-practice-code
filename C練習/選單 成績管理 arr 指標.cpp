#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

char name[10][11];
int score[11];
int time=-1,total=0,ave,time2=0,end=0;
int main(void){
	printf("��  �w��Ө즨�Z����t��:\n");
	printf("�p�n�i���J���Z �Ы�1�A�d�ݤw��J�����Z�Ы�2\n");
	printf("�d���`���Z�������ȽЫ�3�A�h�X�t�νЫ�4\n");
	for(;end<2;){
	switch(getch()){
		case '1':
			time=time+1;
			printf("��J�H�W�o\n");
			scanf("%s",&name[time][0]);
			printf("��J�L�����Z:\n");
			scanf("%d",&score[time]); 
			printf("�p�n�i���J���Z �Ы�1�A�d�ݤw��J�����Z�Ы�2\n");
	        printf("�d���`���Z�������ȽЫ�3�A�h�X�t�νЫ�4\n");
			break;
		case '2':
			for(time2=0;time2<=time;time2++){
				printf("%s\n",&name[time2][0]);
				printf("%d\n",score[time2]);
				
			}
			printf("�p�n�i���J���Z �Ы�1�A�d�ݤw��J�����Z�Ы�2\n");
	        printf("�d���`���Z�������ȽЫ�3�A�h�X�t�νЫ�4\n");
			break;
		case '3':
			
			for(time2=0;time2<=time+1;time2++){
				total=total+score[time2];
			}
			ave=total/(time+1);
			printf("������%d\n",ave);
			total=0;
			printf("�p�n�i���J���Z �Ы�1�A�d�ݤw��J�����Z�Ы�2\n");
	        printf("�d���`���Z�������ȽЫ�3�A�h�X�t�νЫ�4\n");
			break;
		case '4':
			end=end+1;
			break;
		default:
			end=end;
			break;

			
	}
}
    return(0);
    system("pause");
}
