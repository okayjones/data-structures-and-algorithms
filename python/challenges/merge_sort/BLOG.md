# Merge Sort

Merege Sort is a sorting algorithm (made of two sub-algorithms) that operates by "dividing" the array in half recursively, then "merging" elements into a new list and swapping values as needed to sort.

## Pseudocode

```java
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace

Sample Array: [8, 4, 23, 42, 16, 15]

## Efficency

* Time: O(n*(log(n))
  * Time complexity is based on the length of the original table, which dictates how many times we'll need to "split" the array.
* Space: O(n)
  * Space complexity is based on the number of items in the original array.
