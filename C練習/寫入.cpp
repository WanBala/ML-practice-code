#include <stdio.h>
#include <stdlib.h>
int account;
char name[30];
double total,cost;
FILE *fptr;
int main(){
	printf("�̧ǿ�J �Ʀr  char total �H��cost\n");
	fptr=fopen("client.txt","w");
	scanf("%d %s %lf %lf",&account,name,&total,&cost);
	
	
	while(!feof(stdin)){
		
		fprintf(fptr,"%d   %s   %.2lf   %.2lf\n",account,name,total,cost);
		printf("?");
		scanf("%d %s %lf %lf",&account,name,&total,&cost);
	}
	system("pause");
	return 0;
} 
