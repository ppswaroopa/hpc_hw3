#include<iostream>
#include<climits>
using namespace std;

int sumInContiguosSubArray(int arr[], int size)
{
    int max = INT_MIN, max_end = 0;

    for (int i = 0; i < size; i++)
    {
        max_end = max_end + arr[i];
        if (max < max_end)
            max = max_end;

        if (max_end < 0)
            max_end = 0;
    }
    return max;
}

int main()
{
    int a[] = {-2,1, -3, 4, -1, 2, 1, -5, 4};
    int n = sizeof(a)/sizeof(a[0]);
    int maxSum = sumInContiguosSubArray(a, n);
    cout << "Maximum contiguous sum is " << maxSum;
    return 0;
}