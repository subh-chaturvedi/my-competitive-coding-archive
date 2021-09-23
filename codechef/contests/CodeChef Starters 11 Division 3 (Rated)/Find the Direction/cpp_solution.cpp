#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n{};
	int turns{};
	
	cin>>n;
	for(int i;i<n;i++){
	    cin>>turns;
	    if(turns%4==0){
	        cout<<"North"<<"\n";
	    }
	    else if(turns%4==1){
	        cout<<"East"<<"\n";
	    }
	    else if(turns%4==2){
	        cout<<"South"<<"\n";
	    }
	    else{
	        cout<<"West"<<"\n";
	    }
	}
	
	return 0;
}
