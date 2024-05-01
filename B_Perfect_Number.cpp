#include <bits/stdc++.h>

using namespace std;

template <typename A, typename B>
ostream &operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template <typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type>
ostream &operator<<(ostream &os, const T_container &v)
{
    os << '{';
    string sep;
    for (const T &x : v)
        os << sep << x, sep = ", ";
    return os << '}';
}
void dbg_out() { cerr << endl; }
template <typename Head, typename... Tail>
void dbg_out(Head H, Tail... T)
{
    cerr << ' ' << H;
    dbg_out(T...);
}
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()
#define ll long long
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vll vector<long long>
#define mii map<int, int>
#define si set<int>
#define sc set<char>

/* FUNCTIONS */
#define f(i, s, e) for (long long int i = s; i < e; i++)
#define cf(i, s, e) for (long long int i = s; i <= e; i++)
#define rf(i, e, s) for (long long int i = e - 1; i >= s; i--)
#define pb push_back
#define eb emplace_back
const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

template <typename T = int>
struct Edge
{
    int from, to;
    T weight;
};

template <typename T = int>
struct Graph
{
    vector<vector<Edge<T>>> adj;

    Graph(int n)
    {
        adj.resize(n);
    }

    void addEdge(int from, int to, T weight = 1)
    {
        adj[from].push_back({from, to, weight});
        adj[to].push_back({to, from, weight});
    }

    void readWeightedGraph()
    {
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < m; i++)
        {
            int from, to, weight;
            cin >> from >> to >> weight;
            addEdge(from, to, weight);
        }
    }

    void readUnweightedGraph()
    {
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < m; i++)
        {
            int from, to;
            cin >> from >> to;
            addEdge(from, to);
        }
    }
};
template <typename T>
void read(T &x)
{
    cin >> x;
}

template <typename T, typename... Args>
void read(T &first, Args &...rest)
{
    read(first);
    read(rest...);
}

void solve()
{
    int k;
    cin >> k;
    int cnt = 0;
    for (int i = 1; i <= 1e9; i++)
    {
        int sum = 0;
        int x = i;
        while (x)
        {
            sum += x % 10;
            x /= 10;
        }
        if (sum == 10)
            cnt++;
        if (cnt == k)
        {
            cout << i << endl;
            return;
        }
    }
    return;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++)
    {
        // cout << "Case #" << t << ": ";
        solve();
    }
}