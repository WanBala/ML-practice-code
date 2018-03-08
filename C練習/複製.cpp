#include <stdio.h>
#include <stdlib.h>
FILE *rptr,*wptr;

char ch;

int main(){
	rptr=fopen("save.dat","r");
	wptr=fopen("copy.dat","w"); 
	while(!feof(rptr)){
		fscanf(rptr,"%c",&ch);
		fprintf(wptr,"%c",ch);
	}
	
	printf("完成任務!");
	
	system("pause");
} 
