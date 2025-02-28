#include<bits/stdc++.h>
using namespace std;
#define ll long long int

int main(){
    int n;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    // int min;
    // int t;
    // for(int i=0;i<n;i++){
    //     if(min>arr[i]){
    //         min=arr[i];
    //         t=i;
    //     }
    // }
    int count =0;
    for(int i=0;i<n;i++){
        if(arr[i]!=i+1){
            for(int j=0;j<n;j++){
                if(arr[j]==i+1){
                    int temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                    count ++;
                }
            }
        }
    }

    cout << count;


    return 0;
}