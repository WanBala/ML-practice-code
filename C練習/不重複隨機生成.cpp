#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
int range=-1,number=-1;
void norerand(int);
int main(void){
	srand(time(NULL));
	printf("輸入要不重複重新產生值的範圍:(1~x) 輸入x=?\n");
	scanf("%d",&range);
	printf("輸入要排除值的數量\n");
	scanf("%d",&number);
	norerand(range);
	system("pause");
} 
void norerand(int x){
	int buffer1[number]={-1};
	int buffer[x]={-1};
	int y=rand()%x+1;
	printf("依次請輸入要排除的值\n");
	for(int i=0;i<number;i++){
	    scanf("%d",&buffer[i]);
	}
	printf("輸入完畢，輸出結果\n");
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

