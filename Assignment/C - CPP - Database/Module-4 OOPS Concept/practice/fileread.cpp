#include<iostream>
#include<fstream>
using namespace std;
int main(){
string str;  
    ifstream fin;
    fin.open("D:\\paras\\Assignment\\Module-4 OOPS Concept\\practice\\file.txt");
   while(!fin.eof()){
    getline(fin,str);
     cout<<str<<endl;
   }

      fin.close();
}