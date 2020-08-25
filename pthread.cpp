#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int i=0;
int main(){
    ifstream ip("input.csv");
    if(!ip.is_open()) cout<< "error in opening file"<<"\n";
    string id;
    string interval;
    string preceed;
    int lines;
    string line;
    for(lines = 0; getline(ip,line); lines++);
    cout<<lines<<endl;


    while(ip.good()){
        char smallArr[3];
        getline(ip,id,',');
        getline(ip,interval,',');
        getline(ip,preceed,'\n');

    cout<<"id="<<id<<"intrval="<<interval<<"preceed="<<preceed<<endl;
    // user_input[i][0]=stoi(id);
    // user_input[i][1]=stoi(interval);
    // user_input[i][2]=stoi(preceed);
    }
    ip.close();
    // cout<<user_input[0][0]<<user_input[0][1]<<endl;
    return 0;
}