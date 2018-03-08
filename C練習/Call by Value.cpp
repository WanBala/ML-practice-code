#include <stdlib.h>
#include <stdio.h>
int a=8;

int main(void){
	printf("%d\n",a);
	printf("%p\n",&a);
	int *g=&a;
	printf("%d",*g);
}
