// CPP program to demonstrate multithreading
// using three different callables.
#include <iostream>
#include <thread>
#include <algorithm>
#include <vector>
#include <unistd.h>
#include <fstream>
#include <string>




using namespace std;


int user_input[16][3] = {1,5,8,
2,1,15,
3,1,8,
4,2,2,
5,3,6,
6,1,0,
7,2,15,
8,1,6,
9,2,3,
10,2,5,
11,6,14,
12,3,0,
13,2,1,
14,2,8,
15,3,9,
16,1,1,
};
// int user_input[6][3] = {1, 2 ,0 ,
// 2 ,4 , 1 ,
// 4,3,2,
// 3 , 5 , 0,
// 5,10,3,
// 7,16,2};

int length=sizeof(user_input)/sizeof(user_input[0]);
vector<thread> workers;
vector <thread> subtask;
int counter = 0;
int totalOut=0;


// A dummy function
void foo(int input_user[],int previousTime)
{

int totalTime=previousTime;
counter++;
cout << "id" << input_user[0] << endl;
totalTime = totalTime + input_user[1];
if(totalOut<totalTime)totalOut=totalTime;
// cout << "total Time" << totalTime<<endl;
for (int i = 0; i < length; i++) {
	if (user_input[i][0] != input_user[0] && user_input[i][2]==input_user[0]) {
	// subtask.push_back(thread(foo, user_input[i],totalTime));
		thread t1(foo, user_input[i], totalTime);
		t1.detach();
		sleep(input_user[1]);
	}
}

}

// A callable object
// class thread_obj {
// public:
// void operator()(int x)
// {
// for (int i = 0; i < x; i++)
// cout << "Thread using function"
// " object as callable\n";
// }

// };

void readFile(){
	
ifstream ip("input.csv");
    if(!ip.is_open()) cout<< "error in opening file"<<"\n";
    string id;
    string interval;
    string preceed;

    while(ip.good()){
        getline(ip,id,',');
        getline(ip,interval,',');
        getline(ip,preceed,'\n');

    cout<<"id="<<id<<"intrval="<<interval<<"preceed="<<preceed<<endl;
    }
    ip.close();
}

int main()
{

// readFile();
for(size_t i = 0; i < length; i++)
{
if(user_input[i][2]==0){
workers.push_back(std::thread([i]()
{
cout << "thread function\n" << user_input[i][0];
foo(user_input[i],0);
}));
}
}


// thread th2(foo,4);

// This thread is launched by using
// function object as callable
// thread th2(thread_obj(), 3);

for_each(workers.begin(), workers.end(), [](thread &t)
{

if (t.joinable())
{
t.join();
}
});


sleep(2);
cout << "final output" << totalOut<<endl;
return 0;
}