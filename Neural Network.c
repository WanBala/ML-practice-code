#include <stdio.h>
#include <stdlib.h>
#include<assert.h>
#include <math.h>
#include <time.h>

#define input_n 1				//輸入的特徵數
#define input_examples 10  			//輸入的樣本數
#define hidden_n 10				//隱藏層個數
#define output_n 1				//輸出的個數
#define iterations 200				//總迭代次數
#define learning_rate 0.1			//訓練速率
//注意，樣本在矩陣中一律放直的!


//創立一個矩陣，維度為D1、D2，若Mode 為0，以initial的值初始化，若Mode為非零為隨機初始化
float *Mat_Create(int D1,int D2, float Mod,int initial){
	float *Array=malloc(D1*D2*sizeof(float));
	float *Copy=Array;
	if(Mod==0){		
		for (int i = 0; i <(D1*D2); i++)
		{
			*Copy=initial;
			Copy=Copy+1;		
		}
	}
	else{

		for (int i = 0; i <(D1*D2); i++)
		{
			*Copy=(double) (2*(rand() / (RAND_MAX + 1.0))-1);
			Copy=Copy+1;		
		}
	}
	return Array;   
}        

//給定矩陣的維度還有指定的位置，將回傳其記憶體位置
float *Mat_Idx(float *Array,int D1,int D2,int idx1, int idx2){
	assert(idx1<(D1+1) && idx2<(D2+1));
	float *position=Array+(idx1-1)*D2+idx2-1;
	return position;   
}

//給定矩陣A，矩陣B以及其分別的維度，將返回矩陣內積的記憶體位置
float *Mat_Dot(float *Array1,float* Array2, int D11,int D12,int D21, int D22){
	assert(D12==D21);
	float *result=malloc(D11*D22*sizeof(float));
	float *address=result;
	float total=0;
	for (int k = 1; k < (D11+1); k++)
	{
		for (int i = 1; i < (D22+1); i++)
		{
			for (int j = 1; j < (D21+1); j++)
			{
				total=total+(*Mat_Idx(Array1,D11,D12,k,j))*(*Mat_Idx(Array2,D21,D22,j,i));
			}
			*result=total;
			total=0;
			result++;
		}
	}
	return address;
}//創新變數

//給定矩陣A及其維度，返回矩陣轉置的記憶體位置
float *Mat_Tran(float *Array1,int D1, int D2){
	float *Inv_ptr=malloc(D1*D2*sizeof(float));
	float *ptr=Inv_ptr;
	for (int i = 1; i < (D2+1); i++)
	{
		for (int j = 1; j < (D1+1); j++)
		{
			*ptr=*Mat_Idx(Array1,D1,D2,j,i);
			ptr++;
		}
	}
	return Inv_ptr;
}//創新變數

//給定矩陣A及維度，印出內容
void Mat_Show(float *Array,int D1, int D2){
	for (int i = 1; i < (D1+1); i++)
	{
		for (int j = 1; j < (D2+1); j++)
		{
			printf("%f  ",*Array);
			Array++;
		}
		printf("\n");
	}
}

//給定矩陣A和B及其分別的維度，值會加到A，返回A的記憶體位置
float *Mat_Plus(float *Array1,float *Array2, int D11,int D12,int D21,int D22){
	float *pointer=Array1;
	if(D11==D21 && D12==D22){
		for (int i = 0; i < (D11*D22); i++)
		{
			*Array1=*Array1+*Array2;
			Array1++;
			Array2++;
		}
	}
	else if(D11 ==D21 && D22==1){
		for (int i = 1; i < (D21+1); i++)
		{
			for (int j = 1; j < (D12+1); j++)
			{
				*Mat_Idx(Array1,D11,D12,i,j)=*Mat_Idx(Array1,D11,D12,i,j)+*Mat_Idx(Array2,D21,D22,i,1);
			}
		}
	}
	else if(D21==1 && D12==D22){
		for (int i = 1; i < (D22+1); i++)
		{
			for (int j = 1; j < (D11+1); j++)
			{
				*Mat_Idx(Array1,D11,D12,j,i)=*Mat_Idx(Array1,D11,D12,j,i)+*Mat_Idx(Array2,D21,D22,1,i);
			}
		}
	}
	else if(D21==1 && D22==1){
		for (int i = 0; i < (D11*D12); i++)
		{
			*Array1=*Array1+*Array2;
			Array1++;	
		}
	}
	else{
		printf("These two matrix can't be operated.");
	}
	return pointer;
} //不創新變數

//給定矩陣A和B及其分別的維度，A矩陣-B矩陣，返回A的記憶體位置
float *Mat_Minus(float *Array1,float *Array2, int D11,int D12,int D21,int D22,float rate){
	float *pointer=Array1;
	if(D11==D21 && D12==D22){
		for (int i = 0; i < (D11*D22); i++)
		{
			*Array1=*Array1-rate**Array2;
			Array1++;
			Array2++;
		}
	}
	else if(D11 ==D21 && D22==1){
		for (int i = 1; i < (D21+1); i++)
		{
			for (int j = 1; j < (D12+1); j++)
			{
				*Mat_Idx(Array1,D11,D12,i,j)=*Mat_Idx(Array1,D11,D12,i,j)-rate**Mat_Idx(Array2,D21,D22,i,1);
			}
		}
	}
	else if(D21==1 && D12==D22){
		for (int i = 1; i < (D22+1); i++)
		{
			for (int j = 1; j < (D11+1); j++)
			{
				*Mat_Idx(Array1,D11,D12,j,i)=*Mat_Idx(Array1,D11,D12,j,i)-rate**Mat_Idx(Array2,D21,D22,1,i);
			}
		}
	}
	else if((D21==1 && D22==1)||(D11==1&&D12==1) ){
		for (int i = 0; i < (D11*D12); i++)
		{
			*Array1=*Array1-rate**Array2;
			Array1++;	
		}
	}
	else{
		printf("These two matrix can't be operated.\n");
	}
	return pointer;
}  //不創新變數

//給定矩陣A及其維度，返回1-矩陣A的值
float *One_Minus(float *Array1,int D11, int D12){
	float *space=malloc(D11*D12*sizeof(float));
	float *ptr=space;
	for (int i = 0; i < D11*D12; i++)
	{
		*space=1.0-*Array1;
		Array1++;
		space++;
	}
	return ptr;
} //創新變數



//給定矩陣A、B及其分別的維度 回傳矩陣點乘積的記憶體位置
float *Mat_Mul(float *Array1,float *Array2, int D11,int D12,int D21,int D22){
	float *pointer=Array1;
	if(D11==D21 && D12==D22){
		for (int i = 0; i < (D11*D22); i++)
		{
			*Array1=*Array1**Array2;
			Array1++;
			Array2++;
		}
	}
	else if(D21==1 && D22==1){
		for (int i = 0; i < (D11*D12); i++)
		{
			*Array1=*Array1**Array2;
			Array1++;

		}
	}



	else if(D11 ==D21 && D22==1){
		for (int i = 1; i < (D21+1); i++)
		{
			for (int j = 1; j < (D12+1); j++)
			{
				*Mat_Idx(Array1,D11,D12,i,j)=*Mat_Idx(Array1,D11,D12,i,j)**Mat_Idx(Array2,D21,D22,i,1);
			}
		}
	}
	else if(D21==1 && D12==D22){
		for (int i = 1; i < (D22+1); i++)
		{
			for (int j = 1; j < (D11+1); j++)
			{
				*Mat_Idx(Array1,D11,D12,j,i)=*Mat_Idx(Array1,D11,D12,j,i)**Mat_Idx(Array2,D21,D22,1,i);
			}
		}
	}

	else{
		printf("These two matrix can't be operated.\n");
	}
	return pointer;
}//創新變數

//給定矩陣A及其維度 返回取Relu後的記憶體位置
float *Relu(float *Array,int D1,int D2){
	float *space=malloc(D1*D2*sizeof(float));
	float *ptr=space;
	for (int i = 0; i < (D1*D2); i++)
	{	
		if(*Array<0){
			*space=0;
		}
		else{
			*space=*Array;
		}
		space++;
		Array++;
	}
	return ptr;
} //創新變數

//給定矩陣A及其維度，返回取dRelu後的記憶體位置
float *dRelu(float *Array,int D1, int D2){
	float *ptr=malloc(D1*D2*sizeof(float));
	float *address=ptr;
	for (int i = 0; i < (D1*D2); i++)
	{
		if(*Array<0){
			*ptr=0;
		}
		else{
			*ptr=1;
		}
		ptr++;
		Array++;
	}
	return address;
}//創新變數

//給定矩陣A及其維度，返回取Sigmoid後的記憶體位置
float *Sigmoid(float *Array,int D1, int D2){
	float *ptr=malloc(D1*D2*sizeof(float));
	float *address=ptr;
	for (int i = 0; i < (D1*D2); i++)
	{
		*ptr=1.0/(1.0+exp(-*Array));
		ptr++;
		Array++;
	}
	return address;
}//創新變數

//給定矩陣A及其維度，返回取dSigmoid後的記憶體位置
float *dSigmoid(float *Array,int D1, int D2){
	float *Sig=Sigmoid(Array, D1, D2);    //+
	float  *Minus=One_Minus(Sig,D1,D2);
	float *dSig=Mat_Mul(Sig,Minus,D1,D2,D1,D2);
//	free(Minus);
//	free(Sig);
	return dSig;
}//創新變數

//給定矩陣A及標準答案B，返回Cross-Entropy後的Cost
float Cross_Entropy(float *Array,float *True_label,int D1, int D2){
	float total=0;
	for (int i = 0; i < (D1*D2); i++)
	{
		total=total+(*True_label*log(*Array)+(1-*True_label)*log(1-*Array));
		Array++;
		True_label++;
	}
	total=total/(D2);
	return total;
}

//給定矩陣A及標準答案B，返回差平方的Cost
float Square_Err(float *Array,float *True_label,int D1, int D2){
	float total=0;
	for (int i = 0; i < (D1*D2); i++)
	{
		total=total+pow(*Array-*True_label,2);
		Array++;
		True_label++;
	}
	total/=(D1*D2);
	return total;
}

//給定矩陣A及標準答案B，返回差平方之微分
float *dSquare_Err(float *Array, float* True_label,int D1, int D2){
	float *dSq=malloc(D1*D2*sizeof(float));
	float *ptr=dSq;
	for (int i = 0; i < D1*D2; i++)
	{
		*ptr=*Array*(*Array-*True_label);
		ptr++;
		True_label++;
	}
	return dSq;
}
//給定矩陣A及其維度，返回其行和
float *b_Total(float *Array, int D1, int D2){
	float *space=malloc(D1*sizeof(float));
	float *ptr=space;
	float total=0;
	for (int i = 1; i < (D1+1); i++)
	{
		total=0;
		for (int j = 1; j< (D2+1); j++)
		{
			total=total+*Mat_Idx(Array,D1,D2,i,j);
		}
		total=total/D2;
		*ptr=total;
		ptr++;
	}
	return space;
}//創新變數

給定矩陣和其維度，會將scale縮小
void Mat_Scale(float *Array,int D1, int D2){
	for (int i = 0; i<D1*D2; i++)
	{
		*Array=*Array/(float)input_examples;
	Array++;
	}
	
}

int main(){
	srand(time(NULL));
//定義Input以及全連結函數W	
	float *Input1x10=Mat_Create(input_n,input_examples,1,0);
	float *W1_10x1=Mat_Create(hidden_n,input_n,1,1);      //注意第三個位數是模式位、0為以第四參數為初始值、1為隨機初始化
	float *b1_10x1=Mat_Create(hidden_n,1,0,0);
	float *W2_1x10=Mat_Create(output_n,hidden_n,1,1);
	float *b2_1x1=Mat_Create(output_n,1,0,0);
	float *Ouput1x10=Mat_Create(output_n,input_examples,1,0);
//定義向前傳遞
	
	for (int i = 0; i <iterations; ++i)
	{	
	
	float *Z1_10x10=Mat_Plus(Mat_Dot(W1_10x1,Input1x10,hidden_n,input_n,input_n,input_examples),b1_10x1,hidden_n,input_examples,hidden_n,1);
	float *A1_10x10=Relu(Z1_10x10,hidden_n,input_examples);
	float *Z2_1x10=Mat_Plus(Mat_Dot(W2_1x10,A1_10x10,output_n,hidden_n,hidden_n,input_examples),b2_1x1,output_n,input_examples,output_n,1);
	float *A2_1x10=Sigmoid(Z2_1x10,output_n,input_examples);
	

//定義向後傳遞

		/* code */
	
	float difference=Square_Err(A2_1x10,Ouput1x10,output_n,input_examples);
	printf("Square_Error is %f\n",difference);

	float *dCost=dSquare_Err(A2_1x10,Ouput1x10,output_n,input_examples);    //直接將Cost微分視為dA

	float *Sig=dSigmoid(A2_1x10,output_n,input_examples);			//對Sigmoid微分

	float  *dZ2_1x10=Mat_Mul(dCost,Sig,output_n,input_examples,output_n,input_examples);  //求dZ2


	float *TA1_10x10=Mat_Tran(A1_10x10,hidden_n,input_examples);     //取得A1的Transpose




	float *dW2_1x10=Mat_Dot(dZ2_1x10,TA1_10x10,output_n,input_examples,input_examples,hidden_n);   //計算出dW1
	Mat_Scale(dW2_1x10,output_n,hidden_n);				//將dW縮放，因為在計算dW時沒有除以總樣本數，因此在這邊除


	printf("-------------------\n");
	float *db2_1x1=b_Total(dZ2_1x10,output_n,1);               //計算db2


	float *W2_tran_10x1=Mat_Tran(W2_1x10,output_n,hidden_n);	       //算W2轉置
	float *dA1=Mat_Dot(W2_tran_10x1,dZ2_1x10,hidden_n,output_n,output_n,input_examples);	//算dA1
	float *rel=dRelu(A1_10x10,hidden_n,input_examples);			//算Relu微分

	float *dZ1_10x10=Mat_Mul(dA1,rel,hidden_n,input_examples,hidden_n,input_examples);		//算dZ1
	float *Tinput_10x1=Mat_Tran(Input1x10,input_n,input_examples);		//得Input的Transpose



	float *dW1_10x1=Mat_Dot(dZ1_10x10,Tinput_10x1,hidden_n,input_examples,input_examples,input_n);  //計算dW2
	Mat_Scale(dW1_10x1,hidden_n,input_n);					//將dW 縮放 因為計算dW時沒有除樣本數
	float *db1_10x1=b_Total(dZ1_10x10,hidden_n,input_examples);			//求db1

//以下為更新參數和刪除一些暫存的空間
	Mat_Minus(W2_1x10,dW2_1x10, output_n,hidden_n,output_n,hidden_n,learning_rate);		
	Mat_Minus(b2_1x1,db2_1x1, output_n,1,output_n,1,learning_rate);
	Mat_Minus(W1_10x1,dW1_10x1,hidden_n,input_n,hidden_n,input_n,learning_rate);
	Mat_Minus(b1_10x1,db1_10x1,hidden_n,1,hidden_n,1,learning_rate);
	free(dCost);free(Sig);free(dZ2_1x10);free(dZ1_10x10);free(TA1_10x10);free(dW1_10x1);free(dW2_1x10);
	free(rel);free(db1_10x1);free(db2_1x1);free(W2_tran_10x1);free(Tinput_10x1);
	}

}

