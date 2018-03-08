#include <stdio.h>
#include <stdlib.h>
typedef struct poly
{
	int coef;			//係數 
	int expo;			//次數
	struct poly *next;	//下一個節點的指標 
}poly;

void	printpoly	(poly*);					//列印出整個多項式 
int		length		(poly*);					//傳回該多項式的長度 
poly*	add			(poly*);					//在鍊表尾端新增節點 
poly*	del			(poly*,int);				//刪除指定位置的節點,起始為1 
poly*	write		(poly*,int,int,int);		//在指定編號的節點寫入資料,起始為1 
poly*	insert		(poly*,poly*,int);			//在指定編號的節點後插入鍊表
poly*	combine		(poly*);					//對該多項式進行同類項合併
poly*	inverse		(poly*);					//對該多項式的係數正負號相反

int main(void)
{	
	/***任何用於多項式建立的poly*必須先指向NULL或0否則add()建立多項式會出錯***/ 
	
	int coef,expo,count;
	poly *QA=0,*QB=0;
	
	while(1)
	{
		printf("請依序輸入多項式Q(A)的係數及次數,輸入0,0退出\n");
		printf("QA:");		
		printpoly(QA);
		printf("\n");		
		scanf("%d%d",&coef,&expo);
		if(coef==0&&expo==0)
		{
			break;
		}
		count++;
		QA=add(QA);
		QA=write(QA,count,coef,expo);
		system("cls");
	}
	
	count=0;
	system("cls");
	
	while(1)
	{
		printf("請依序輸入多項式Q(B)的係數及次數,輸入0,0退出\n");		
		printf("QA:");		
		printpoly(QA);
		printf("\n");
		printf("QB:");
		printpoly(QB);
		printf("\n");		
		scanf("%d%d",&coef,&expo);
		if(coef==0&&expo==0)
		{
			break;
		}
		count++;
		QB=add(QB);
		QB=write(QB,count,coef,expo);
		system("cls");
	}
	printf("請問要執行相加或相減?請輸入+或-\n");
		
	char c[3];	
	do
	{
	scanf("%s",&c);
		switch(c[0])
		{
		case '+':
			break;
		case '-':
			QB=inverse(QB);
			break;
		default:
			printf("你輸入%d 錯誤:請重新輸入\n",c[0]);
		}
	}while(c[0]!='+'&&c[0]!='-');
	
	 
	system("cls");
	printf("QA:");
	printpoly(QA);
	printf("\n");
	printf("QA:");
	printpoly(QB);
	printf("\n------------------------\n");
	QA=insert(QA,QB,length(QA));
	QA=combine(QA);
	printpoly(QA);
	
	return 0;
}
void printpoly(poly* sptr)
{
	poly *move;
	move=sptr;
	while(move!=NULL)
	{
		if(move->coef>0)
		{
			printf("+");
		}		
		printf("%dx^%d ",move->coef,move->expo);
		move = move->next;
	}
	return;
}
int length(poly* sptr)
{
	poly* move;
	move = sptr;
	if(sptr==0)
	{
		printf("計算失敗:你傳入了一個空的指標");
		return -1;
	}
	int count = 1;
	while(move->next!=NULL)
	{
		move = move->next;
		count++;
	}
	return count;
}
poly* add(poly* sptr)
{
	//建立第一個
	if(sptr==0)
	{
	//printf("新增第一個");
	sptr=(poly*)malloc(sizeof(poly));
	sptr->next = NULL;
	return sptr;
	}
	//建立第n個 
	else
	{
	//	printf("新增第n個");
		poly* move;
		move = sptr;
		while(move->next!=NULL)
		{
			move = move->next;
		}
		move->next=(poly*)malloc(sizeof(poly));
		move = move->next;
		move->next = NULL;
	return sptr;
	}
}
poly* del(poly* sptr,int number)
{
	poly *move,*pptr,*tmp;
	move = sptr;
	//如果超出節點範圍 則無刪除動作
	if(number==1)
	{
		poly *tmp;
		tmp = sptr->next;
		free(sptr);
		sptr = tmp;
		return sptr;
	}
	number--;
	while(move->next!=NULL)
	{
		if(number==0)
		break;
		else
		{
		pptr = move;
		move = move->next;
		number=number-1;
		}
	}
	if(number!=0)
	{
		printf("刪除失敗-超出索引範圍\n");
		return sptr;
	}
	tmp = move->next;
	free(move);
	pptr->next = tmp;
	
	return sptr;
}
poly* write(poly* sptr,int number,int coef,int expo)
{
	poly* move;
	move = sptr;
	number--;
	//如果超出節點範圍 則無寫入動作 
	while(move->next!=NULL)
	{
		if(number==0)
		break;
		else
		{
		move = move->next;
		number=number-1;
		}
	}
	if(number!=0)
	{
		printf("寫入失敗-超出索引範圍\n");
		return sptr;
	}
	move->coef = coef;
	move->expo = expo;
	return sptr;
}
poly* insert(poly* sptrA,poly* sptrB,int number)
{	
	poly *move,*move2,*tmp;
	move = sptrA;
	move2 = sptrB;
	number--;
	while(move->next!=NULL)
	{
		if(number==0)
		break;
		move = move->next;
		number--;
	}
	if(number!=0)
	{
		printf("插入失敗:超出索引範圍\n");
		return sptrA;
	}
	while(move2->next!=NULL)
	{
		move2 = move2->next;
	}
	tmp = move->next;
	move->next = sptrB;
	move2->next = tmp;
	
	return sptrA;
}
poly* combine(poly* sptr)
{
	poly *scan,*move;
	scan = move = sptr;
	int scount=1,mcount=1;
	while(1)
	{
		while(1)
		{
			move = move->next;
			mcount++;
			jp:
			if(move->next !=NULL)
			{
				if(scan->expo==move->expo)
				{
					scan->coef += move->coef;
					move = move->next;
					del(sptr,mcount);
					goto jp;					
				}
			}
			if(move->next == NULL)
			{
				if(scan->expo==move->expo)
				{
					scan->coef += move->coef;
					del(sptr,mcount);
				}
				break;
			}
		}//in
		if(scan->next != NULL)
		{
			scan = scan->next;
			scount++;
			move = scan;
			mcount = scount;
		}
		if(scan->next == NULL)
		{
			break;
		}
	}
	return sptr;
}
poly* inverse(poly* sptr)
{
	poly *move;
	move=sptr;
	while(move!=NULL)
	{
		move->coef = (move->coef*(-1));
		move = move->next;
	}
	return sptr;
}
