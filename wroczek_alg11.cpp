/*
 * wroczek_alg11.cpp
 * 
 */

#include <iostream>
 
using namespace std;
 
void sprawdz_liczbe(int a)
{
    int i = 2;
    while(a!=i)
    {
        if(i==100)
        {
            cout<<"nieparzyste";
            break;
        }
        i+=2;
    }
    if(a==i) // wedlug rysunku tego ifa nie powinno byc, ale bez niego nie dziala xd
    {
        cout<<"parzyste";
    }
}
 
int main(int argc, char **argv)
{
    int a = 0;
    do
    {
        cout<<"Podaj liczbe:";
        cin>>a;
    }while(a<=0 || a>=100);
   
   
    sprawdz_liczbe(a);
   
 
   
    return 0;
}
