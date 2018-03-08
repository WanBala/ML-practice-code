#include <stdio.h>
#include <stdlib.h>

typedef struct Group Group;
struct Group{
	int AP;
	Group *next;
} ;
int count=0;

void Surfing_List(int number,Group *head){
	Group *current=malloc(sizeof(Group));
	current=head;
	while(1){
		count++;
		if((current)!=NULL){
			printf("This is the %d   level  number :%d \n",count,current->AP);
			current=current->next;
		}
		else{
			break;
		}
	}
}

Group* Create(int number,Group *head){
	Group *new=malloc(sizeof(Group));
	head->next=new;
	new->AP=number;
	return new;
}


int main(){
	printf("Input a number that would be the first number\n");
	int number=0;

	Group *head=malloc(sizeof(Group));
	scanf("%d",&number);
	head->AP=number;
	head->next=NULL;
	Group *current=head;

/*	for (int i = 0; i <10; i++)
	{
		printf("Input a number\n");
		scanf("%d",&number);
		current->next=malloc(sizeof(Group));
		current=current->next;
		current->AP=number;
		current->next=NULL;
	}*/
	current=Create(8,current);
//	Surfing_List(8,head);
	printf("%d\n",current->AP);

	printf("End\n");
	system("pause");
	return 0;
}

