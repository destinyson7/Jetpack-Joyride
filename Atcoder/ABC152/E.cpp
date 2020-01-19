#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
 
using namespace __gnu_pbds;
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;
typedef pair <ll, ll> pll;
typedef pair <int, int> pii;

typedef tree <ll, null_type, less <ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
// order_of_key(val): returns the number of values less than val
// find_by_order(k): returns an iterator to the kth largest element (0-based)

#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(a) a.begin(), a.end()
#define sz(a) (ll)(a.size())
#define endl "\n"

template <class Ch, class Tr, class Container>
basic_ostream <Ch, Tr> & operator << (basic_ostream <Ch, Tr> & os, Container const& x) 
{
    os << "{ ";
    for(auto& y : x) 
    {
        os << y << " ";
    }
    return os << "}";
}

template <class X, class Y>
ostream & operator << (ostream & os, pair <X, Y> const& p) 
{
    return os << "[" << p.ff << ", " << p.ss << "]";
}

ll gcd(ll a, ll b)
{
    if(b==0)
    {
        return a;
    }

    return gcd(b, a%b);
}

ll modexp(ll a, ll b, ll c)
{   
    a%=c;

    ll ans = 1;

    while(b)
    {
        if(b&1)
        {
            ans = (ans*a)%c;
        }

        a = (a*a)%c;
        b >>= 1;
    }

    return ans;
}

const ll L = 1e6+5;
const ll mod = 1e9+7;

vector <ll> least_prime_factor(L, 0);

void sieve()
{
    least_prime_factor[0] = 1;
    least_prime_factor[1] = 1;

    for(ll i=2; i<L; i++)
    {
        if(least_prime_factor[i] == 0)
        {
            for(ll j=i; j<L; j+=i)
            {
                least_prime_factor[j] = i;
            }
        }
    }
}

map <ll, ll> m;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    sieve();
    
    ll N;
    cin >> N;

    vector <ll> a;

    for(ll i=0; i<N; i++)
    {
        ll t;
        cin >> t;

        a.pb(t);

        map <ll, ll> temp;

        while(t > 1)
        {
            ll f = least_prime_factor[t];
            temp[f]++;
            t /= f;
        }   

        for(auto j: temp)
        {
            m[j.ff] = max(m[j.ff], j.ss);
        }
    }

    ll l = 1;

    for(auto i: m)
    {
        l *= modexp(i.ff, i.ss, mod);
        l %= mod;
    }

    ll ans = 0;

    for(ll i=0; i<N; i++)
    {
        // ans += (l/a[i]);
        ans += ((l * modexp(a[i], mod-2, mod))%mod);
        // ans %= mod;
    }

    cout << ans%mod << endl;

    return 0;
}