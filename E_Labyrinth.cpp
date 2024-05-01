#include <bits/stdc++.h>
using namespace std;


// Macros
#define fast_io            \
  ios::sync_with_stdio(0); \
  cin.tie(0);              \
  cout.tie(0);

template <typename T>
void inputList(vector<T> &arr, int n)
{
  arr.resize(n);
  for (auto &a : arr)
    cin >> a;
}

bool inBound(int i, int j, int n, int m)
{
  if (i >= 0 && i < n && j >= 0 && j < m)
    return true;
  return false;
}

// Main function for solving the problem
void solve()
{
  // Start here
  int n, m;
  cin >> n >> m;
  int i, j;
  cin >> i >> j;
  int maxLeft, maxRight;
  cin >> maxLeft >> maxRight;
  vector<string> grid(n);
  inputList(grid, n);
  queue<tuple<int, int, int, int>> q;
  q.emplace(i - 1, j - 1, maxLeft, maxRight);
  int count = 1;
  int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  vector<vector<pair<int, int>>> visited(n, vector<pair<int, int>>(m, {-1, -1}));
  visited[i-1][j-1] = make_pair(maxLeft, maxRight);

  while (!q.empty())
  {
    auto [x, y, ml, mr] = q.front();
    q.pop();
    for (auto &dir : dirs)
    {
      int nx = x + dir[0], ny = y + dir[1];
      if (!inBound(nx, ny, n, m) || grid[nx][ny] == '*')
        continue;
      int nml = ml, nmr = mr;
      if (dir[1] == 1)
        nmr--;
      if (dir[1] == -1)
        nml--;

      if (nml >= 0 && nmr >= 0)
      {
        if (visited[nx][ny] == make_pair(-1, -1))
          count++;
        if (visited[nx][ny] < make_pair(nml, nmr)){
          q.emplace(nx, ny, nml, nmr);
          visited[nx][ny] = {nml, nmr};
        }
      }
    }
  }
  cout << count << "\n";
}

int main()
{
  fast_io;
  int t = 1;
  // cin >> t;
  while (t--)
    solve();

  return 0;
}