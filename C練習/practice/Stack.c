#include <stdlib.h>
#include <stdio.h>
#define MAX 10

int top=-1;
int stack[MAX];
int pop(void);
void push(int);


void push(int number){
	if (top<(MAX-1))
	{
		top++;
		stack[top]=number;
	}
	else{
		printf("容器超過容量上限\n");
	}
}

int pop(void){
	int value=0;
	if(top>-1){
		value=stack[top];
		top--;
	}
	else{
		printf("已經沒內容物了 低能\n");
	}

	return value;
}

int  main(){
	int  number=0;
	for (int i = 0; i < MAX; i++)
	{
		printf("Input 個 Number\n");
		scanf("%d",&number);
		push(number);
	}
	for (int i = 0; i < MAX; i++)
	{
		printf("This number is %d\n",pop());
	}
	system("pause");
	return 0;
}