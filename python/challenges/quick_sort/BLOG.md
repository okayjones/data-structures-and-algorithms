# Quick Sort

Quick sort is a divide and conquer algorithm. It sorts by selecting a "pivot" and uses it to parition the array.

## Pseudocode

```java
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

## Trace

Sample Array: [8, 4, 23, 42, 16, 15]

### Step 1

```bash
Starting array

index      0  1   2   3   4   5
values    [8, 4, 23, 42, 16, 15]
```

We begin by calling quick sort, passing in array along with the left most index (0) and the right most index (5). First we check that the left is smaller than the right. Since 0 < 5 we continue and call partition.

```bash
Ending array

index      0  1   2   3   4   5
values    [8, 4, 15, 42, 16, 23]
swapped           ^           ^
```

Partition will assign the right most value as the 'pivot', 15. Next, we'll iterate through the array to find the index where 15 can be assigned so all values to the left are smaller, and all values to the right are larger. Once this position is found (index 2) the values will be swapped so 15 is in index 2, and the original value (23) in now in index 5. The partition function will then return index 2, which is assigned to position in the calling function.

### Step 2

```bash
Starting array

index      0  1   2   3   4   5
values    [8, 4, 15, 42, 16, 23]
position          ^
```

Now, quick sort is called again. This time we'll pass in the array, but set left and right as the left side of the position (array, 0, 1)

```bash
Ending array

index      0  1   2   3   4   5
values    [4, 8, 15, 42, 16, 23]
swapped    ^  ^ 
```

When partition is called now, it's only dealing with the left portion of the array [8, 4] and the pivot is assigned to 4. We'll iterate through the array again, looking for the position where 4 is higher than all the numbers to the left. This is only true if 4 is in index 0, so values 8 and 4 are swapped. Then we return index 0 back to the caller to be assigned the position.

### Step 3

```bash
Starting array

index      0  1   2   3   4   5
values    [4, 8, 15, 42, 16, 23]
position   ^  
```

Quick sort will be called again with side of the array left of the position (0, -1). However, since 0 !< -1, we'll exit out without doing anything. Next, we call quick sort with the right side (1, 1). Again, since 1 !< 1 we'll exit the function again.

```bash
Ending array

index      0  1   2   3   4   5
values    [4, 8, 15, 42, 16, 23]
position          ^  
```

At this point, everything to the left of our initial position (index 2) is sorted! We've circled back to this point in the call chain with our position back at index 2.

### Step 4

```bash
Starting array

index      0  1   2   3   4   5
values    [4, 8, 15, 42, 16, 23]
position          ^  
```

Now that the left of our current position is sorted, we'll call quick sort on the right [42, 16, 23]. The first step will be assigning the position, and again we'll call parition to do that.

```bash
Ending array

index      0  1   2   3   4   5
values    [4, 8, 15, 16, 23, 42]
swapped               ^   ^
swapped                   ^   ^
```

Partition is called with the left and right indexes (3, 5) of the sub-array [42, 16, 23]. We'll iterate through the array, determining where out right index (value 23) belongs. This time, we find out of order values [42, 16] so we swap them first. Then, we can swap [42, 23] so 23 is in the right position. We'll return the lowest index where 23 is now (4) back to our caller.

### Step 5

```bash
Starting array

index      0  1   2   3   4   5
values    [4, 8, 15, 16, 23, 42]
position                  ^
```

Now that we have our new positon, we'll call quick sort on the portion of the sub-array [16, 23, 5] that is left of the position (3, 3). Similiar to step #3, we'll exit quickly since 3 !< 3. Now we'll do the right side of the position (5, 5). Again, we'll exit quickly.

```bash
Starting array

index      0  1   2   3   4   5
values    [4, 8, 15, 16, 23, 42]
```

At this point both original sides of the array have been sorted and we'll exit the function!

## Efficency

* Time: O(n^2)
* Space: O(log(n))
