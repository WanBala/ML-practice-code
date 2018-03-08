#include <stdio.h>
#include <stdlib.h>
FILE *rptr,*wptr;

char buffer[100];

int main(){
	rptr=fopen("save.dat","r");
	wptr=fopen("copy.dat","w");
	for(int i=0;i<100;i++){
		if(!feof(rptr)){
			fscanf(rptr,"%c",&buffer[i]);
			
		}
	}
	for(int i=0;i<100;i++){
	
		fprintf(wptr,"%c",buffer[i]);
	}
	printf("µ²§ô");
	system("pause");
	
}
