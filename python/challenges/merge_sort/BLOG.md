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

### Step 1

```bash
              [8, 4, 23, 42, 16, 15]
                  /            \
            [8, 4, 23]      [42, 16, 15]
               / \
            [8]  [4, 23]
                   / \
                [4]  [23]
```

Merge sort will recusively 'divide' the arrary in half, handling the left side first and then the right. This will happen down the full height of the left side until each node is a single value.

### Step 2

```bash
              [8, 4, 23, 42, 16, 15]
                  /            \
            [8, 4, 23]      [42, 16, 15]
               / \
            [8]  [4, 23]

# Sub-array [4, 23] is now sorted

              [8, 4, 23, 42, 16, 15]
                  /            \
            [4, 8, 23]      [42, 16, 15]

# Sub-array [4, 8, 23] is now sorted                
```

Now, merge is called. This will "climb" back up the tree, evaluating values in each sub-array. Values will swap postions so they are correctly ordered. This allows the sub arrays to be reorderes as each level collapses back.

### Step 3

```bash
              [8, 4, 23, 42, 16, 15]
                  /            \
            [4, 8, 23]      [42, 16, 15]
                                /   \
                              [42]  [16, 15]
                                       / \
                                    [16] [15]
```

Next, the right side of the array will go through the same recursive process as Step #1. The right side array being split in halves until we reach single values.

### Step 4

```bash
              [8, 4, 23, 42, 16, 15]
                  /            \
            [4, 8, 23]      [42, 16, 15]
                                /   \
                              [42]  [15, 16]

# Sub-array [15, 16] is now sorted

              [8, 4, 23, 42, 16, 15]
                  /            \
            [4, 8, 23]      [15, 16, 42]

# Sub-array [15, 16, 42] is now sorted
```

The merge process will be repeated on the right side, ensuring the right half os the initial array is sorted appropriately.

### Step 5

```bash
              [2, 8, 15, 16, 23, 42]
```

Finally, the last merge method is called, completeing the sort of the original array by comparing values in order in the sub-arrays.

## Efficency

* Time: O(n*(log(n))
  * Time complexity is based on the length of the original table, which dictates how many times we'll need to "split" the array.
* Space: O(n)
  * Space complexity is based on the number of items in the original array.
