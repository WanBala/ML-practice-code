#include <stdlib.h>
#include <stdio.h>
#define MAX 10

int Top=-1,Bot=-1,objects=0;
int Queue[MAX];
int Get(void);
void Add(int);

void Add(int number){

	if (objects!=MAX){
		Top++;
		Top=Top%MAX;
		Queue[Top]=number;
		objects++;
	}
	else{
		printf("No more avalible space\n");
	}
}

int Get(void){
	int value=0;
	if(objects!=0){
		Bot++;	
		Bot=Bot%MAX;	
		value=Queue[Bot];

		objects--;
	}
	else{
		printf("There is nothing in queue.\n");
	}
	return value;
}


int  main(){
	int  number=0;
	
		printf("Input a Number\n");
		scanf("%d",&number);
		Add(number);
		
	
		printf("This number is %d\n",Get());
	for (int i = 0; i < MAX; i++)
	{
		printf("Input a Number\n");
		scanf("%d",&number);
		Add(number);
	}
	for (int i = 0; i <MAX; i++)
	{
		printf("This number is %d\n",Get());
	}
	system("pause");
	return 0;
}
