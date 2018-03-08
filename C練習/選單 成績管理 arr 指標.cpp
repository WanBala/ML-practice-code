#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

char name[10][11];
int score[11];
int time=-1,total=0,ave,time2=0,end=0;
int main(void){
	printf("恩  歡迎來到成績估算系統:\n");
	printf("如要進行輸入成績 請按1，查看已輸入的成績請按2\n");
	printf("查看總成績的平均值請按3，退出系統請按4\n");
	for(;end<2;){
	switch(getch()){
		case '1':
			time=time+1;
			printf("輸入人名囉\n");
			scanf("%s",&name[time][0]);
			printf("輸入他的成績:\n");
			scanf("%d",&score[time]); 
			printf("如要進行輸入成績 請按1，查看已輸入的成績請按2\n");
	        printf("查看總成績的平均值請按3，退出系統請按4\n");
			break;
		case '2':
			for(time2=0;time2<=time;time2++){
				printf("%s\n",&name[time2][0]);
				printf("%d\n",score[time2]);
				
			}
			printf("如要進行輸入成績 請按1，查看已輸入的成績請按2\n");
	        printf("查看總成績的平均值請按3，退出系統請按4\n");
			break;
		case '3':
			
			for(time2=0;time2<=time+1;time2++){
				total=total+score[time2];
			}
			ave=total/(time+1);
			printf("平均為%d\n",ave);
			total=0;
			printf("如要進行輸入成績 請按1，查看已輸入的成績請按2\n");
	        printf("查看總成績的平均值請按3，退出系統請按4\n");
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
