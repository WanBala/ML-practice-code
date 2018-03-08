#include <stdio.h>
#include <stdlib.h>
char inpu[20];
int inpu2;
class group{
	public:
	
		group2(char a[],int b);
		show();
	private:
		char name[20];
		int score;
};
group::group2(char a[],int b){
	for(int i=0;i<20;i++){
		name[i]=a[i];
	}
	score=b;
}
group::show(){
	printf("%s \n   %d\n",name,score);
}

int main(void){
	group a;
	printf("輸入名稱和分數\n");
	scanf("%s",inpu);
	scanf("%d",&inpu2);
	a.group2(inpu,inpu2);
	group::show;
	system("pause");
}
 
