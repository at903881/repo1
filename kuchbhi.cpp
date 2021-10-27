//PERMUTATION OF SPACES
/////////////////LIBRARIES///////////////////
#include<bits/stdc++.h>
using namespace std;
/////////////////////CLASSES//////////////////

//////////////U D FUNCTIONS//////////////////////////////
void all_subset(string ip,string op);
////////////////MAIN///////////////////////////////////
int main()
{
    string ip="ABC";
    string op="";
    char first=ip[0];
    ip.erase(ip.begin()+0);
    all_subset(ip,op+first);
}

/////////////////////////OUTPUT///////////////////////////////
//A_B_C
//A_BC
//AB_C
//ABC
/////////////////////////FUNCTIONS//////////////////////////////
void all_subset(string ip,string op)
{
    if(ip.size()==0)
    {
        cout<<op<<"\n";
        return;
    }
    else
    {
        char first=ip[0];
        ip.erase(ip.begin()+0);
        all_subset(ip,op+"_"+first);
        all_subset(ip,op+first);
    }

}
