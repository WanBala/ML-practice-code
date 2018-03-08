#include <stdio.h>
#include <stdlib.h>
typedef struct poly
{
	int coef;			//�Y�� 
	int expo;			//����
	struct poly *next;	//�U�@�Ӹ`�I������ 
}poly;

void	printpoly	(poly*);					//�C�L�X��Ӧh���� 
int		length		(poly*);					//�Ǧ^�Ӧh���������� 
poly*	add			(poly*);					//�b�����ݷs�W�`�I 
poly*	del			(poly*,int);				//�R�����w��m���`�I,�_�l��1 
poly*	write		(poly*,int,int,int);		//�b���w�s�����`�I�g�J���,�_�l��1 
poly*	insert		(poly*,poly*,int);			//�b���w�s�����`�I�ᴡ�J���
poly*	combine		(poly*);					//��Ӧh�����i��P�����X��
poly*	inverse		(poly*);					//��Ӧh�������Y�ƥ��t���ۤ�

int main(void)
{	
	/***����Ω�h�����إߪ�poly*���������VNULL��0�_�hadd()�إߦh�����|�X��***/ 
	
	int coef,expo,count;
	poly *QA=0,*QB=0;
	
	while(1)
	{
		printf("�Ш̧ǿ�J�h����Q(A)���Y�ƤΦ���,��J0,0�h�X\n");
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
		printf("�Ш̧ǿ�J�h����Q(B)���Y�ƤΦ���,��J0,0�h�X\n");		
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
	printf("�аݭn����ۥ[�ά۴�?�п�J+��-\n");
		
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
			printf("�A��J%d ���~:�Э��s��J\n",c[0]);
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
		printf("�p�⥢��:�A�ǤJ�F�@�ӪŪ�����");
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
	//�إ߲Ĥ@��
	if(sptr==0)
	{
	//printf("�s�W�Ĥ@��");
	sptr=(poly*)malloc(sizeof(poly));
	sptr->next = NULL;
	return sptr;
	}
	//�إ߲�n�� 
	else
	{
	//	printf("�s�W��n��");
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
	//�p�G�W�X�`�I�d�� �h�L�R���ʧ@
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
		printf("�R������-�W�X���޽d��\n");
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
	//�p�G�W�X�`�I�d�� �h�L�g�J�ʧ@ 
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
		printf("�g�J����-�W�X���޽d��\n");
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
		printf("���J����:�W�X���޽d��\n");
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
