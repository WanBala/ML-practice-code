#include <stdio.h>
#include <stdlib.h>

int arr[]={0,1,2,3,4,5,6};
void power(int x[]);
int num=15;
void fun(int number);

int main(void){
	power(arr);
	for(int y=0;y<7;y++){
		printf("%d\n",arr[y]);
	}
	system("pause");
	
	printf("%d",num);
	fun(num);
	printf("%d",num);
	system("pause");
	return 0;
} 




void power(int x[]){
	for(int y=0;y<7;y++){
		x[y]*=2;
	}
}
void fun(int number){
	num=num+1;
}
