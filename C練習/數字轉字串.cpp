#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int fre2,fre0;
int arr[20];
int main(void){
	sprintf(arr,"%d",82253123);
	printf("最高位數字為",arr[0]);
	for(int num=0;num<8;num++){
		if(arr[num]==2){
			++fre2;
		}
		if(arr[num]==0){
			++fre0;
		}
	}
	printf("出現0的次數為%d",fre0);
	printf("出現2的次數為%d",fre2);
	system("pause");
} 
