/*
 * cwiczenie3_wroczek.cxx
 */

#include <iostream>

using namespace std;

void znajdzMinMax(int tab[],int i,int &maximum,int &minimum, int len )
{
if(i<len){
if (tab[i]<minimum)minimum=tab[i];
if (tab[i]>maximum)maximum=tab[i];
znajdzMinMax(tab,i+1,maximum,minimum,len);
}
	return 0;
}

