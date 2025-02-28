#include<bits/stdc++.h>
using namespace std;
#define ll long long int

int main(){
    int t;
    cin >> t;
    while (t--){
        int n,x,s;
        cin >> n>>x>>s;
        int arr[n]={0};
        arr[x-1]=1;
        while(s--){
            int a,b;
            cin>> a>> b;
            int temp=arr[a-1];
            arr[a-1]=arr[b-1];
            arr[b-1]=temp;
        }
        for(int i=0;i<n;i++){
            if(arr[i]==1){
                cout<<i+1;
                break;
            }
            // cout<< arr[i];
        }
        

    }
    return 0;
}