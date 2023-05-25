#include <bits/stdc++.h>
#define INF 987654321
#define MAXN 100
#define itr 100
using namespace std;
struct dat{
    int red,blue,green;
    int operator-(const dat &q)const{
        return -(red-q.red)*(red-q.red)-(blue-q.blue)*(blue-q.blue)-(green-q.green)*(green-q.green);
    }
}color[MAXN];

int n,a[MAXN][MAXN],s[MAXN][MAXN],r[MAXN][MAXN],exampler[MAXN],nx[MAXN];

void cluster(){
    for(int i=1; i<=n; i++){
        for(int k=1; k<=n; k++){
            int maxi=-INF;
            for(int k1=1; k1<=n; k1++)if(k1!=k)maxi=max(maxi,a[i][k1]+s[i][k1]);
            r[i][k]/=2;
            r[i][k]+=(s[i][k]-maxi)/2;
        }
    }
    for(int i=1; i<=n; i++){
        for(int k=1; k<=n; k++){
            if(i==k)continue;
            int temp=r[k][k];
            for(int i1=1; i1<=n; i1++)if(i1!=i && i1!=k)temp+=max(0,r[i1][k]);
            a[i][k]/=2;
            a[i][k]+=min(0,temp)/2;
        }
    }
    for(int i=1; i<=n; i++){
        int temp=0;
        for(int i1=1; i1<=n; i1++)if(i1!=i)temp+=max(0,r[i1][i]);
        a[i][i]/=2;
        a[i][i]+=temp/2;
    }
}

signed main(){
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    cin >> n;
    for(int i=1; i<=n; i++)cin >> color[i].red >>color[i].blue >> color[i].green;
    vector<int>v;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i==j)continue;
            s[i][j]=color[i]-color[j];
            v.push_back(s[i][j]);
        }
    }
    sort(v.begin(),v.end());
    for(int i=1; i<=n; i++)s[i][i]=v[n*(n-1)/2];
    int rep=0;
    while(rep<10){
        cluster();
        for(int i=1; i<=n; i++){
            int maxi=-INF;
            for(int k=1; k<=n; k++){
                if(maxi<a[i][k]+r[i][k]){
                    maxi=a[i][k]+r[i][k];
                    nx[i]=k;
                }
            }
        }
        bool flag=true;
        for(int i=1; i<=n; i++){
            if(nx[i]!=exampler[i]){
                flag=false;
                break;
            }
        }
        for(int i=1; i<=n; i++)exampler[i]=nx[i];
        if(flag)rep++;
        else rep=0;
    }
    vector<int>groups[MAXN];
    for(int i=1; i<=n; i++)groups[exampler[i]].push_back(i);
    for(int i=1; i<=n; i++){
        if(groups[i].size()!=0){
            cout << i <<" : ";
            for(auto e : groups[i])cout << e << " ";
            cout << "\n";
        }
    }
    return 0;
}
