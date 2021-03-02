# Insertion Sort

Insertion Sort is a sorting algorithm that traverses the array, and compares each value to each previous value to determine where it should be inserted.

## Pseudocode

```java
  InsertionSort(int[] arr)
    
    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp
```

## Trace

Sample Array: [8, 4, 23, 42, 16, 15]

### Pass 1

```bash
i = 1
j (previous index) = 0
temp (value at i) = 4

Index              0  1   2   3   4   5
Starting Array    [8, 4, 23, 42, 16, 15]
                      ^

Index              0  1   2   3   4   5
Current Array     [4, 8, 23, 42, 16, 15]
                      ^
```

In the first pass through the insertion sort (i = 1), we store the previous index (j = 0) and the value at the current index (temp = 4). Then, we evaluate if the value at the current index (4) is less than the value at the prior index (8). Since 4 < 8, index i is set to the value at the previous index, 8. Then, the previous index is set to our temporary varaible, 4. Essentially, we've swapped the current and previous values.

### Pass 2

```bash
i = 2
j (previous index) = 1
temp (value at i) = 23

Index              0  1   2   3   4   5
Starting Array    [4, 8, 23, 42, 16, 15]
                          ^

Index              0  1   2   3   4   5
Current Array     [4, 8, 23, 42, 16, 15]
                          ^
```

In the next pass through the insertion sort (i = 2), we store the previous index (j = 1) and the value at the current index (temp = 23). Then, we evaluate if the value at the current index (23) is less than the value at the prior index (8). Since 23 !< 8, we move to the next iteration.

### Pass 3

```bash
i = 3
j (previous index) = 2
temp (value at i) = 42

Index              0  1   2   3   4   5
Starting Array    [4, 8, 23, 42, 16, 15]
                              ^

Index              0  1   2   3   4   5
Current Array     [4, 8, 23, 42, 16, 15]
                              ^
```

In the 3rd pass (i = 3), we store the previous index (j = 2) and the value at the current index (temp = 42). Then, we evaluate if the value at the current index (42) is less than the value at the prior index (23). Since 42 !< 23, we move to the next iteration.

### Pass 4

```bash
i = 4
j (previous index) = 3
temp (value at i) = 16

Index              0  1   2   3   4   5
Starting Array    [4, 8, 23, 42, 16, 15]
                                  ^

Index              0  1   2   3   4   5
Current Array     [4, 8, 16, 23, 42, 15]
                                  ^
```

In the 4th pass (i = 4), we store the previous index (j = 3) and the value at the current index (temp = 16). Then, we evaluate if the value at the current index (16) is less than the value at the prior index (42). Since 16 < 42, the current index is set to 42. Then, we continue to compare 16 to each prior index. Since 16 is also < 23, index 3 is updated to 23. Since 16 !< 8 (index 1) we'll stop and update index 2 to 16.

### Pass 5

```bash
i = 5
j (previous index) = 4
temp (value at i) = 15

Index              0  1   2   3   4   5
Starting Array    [4, 8, 16, 23, 42, 15]
                                      ^

Index              0  1   2   3   4   5
Current Array     [4, 8, 15, 16, 23, 42]
                                      ^
```

In the 5th and final pass (i = 5), we store the previous index (j = 4) and the value at the current index (temp = 15). Then, we evaluate if the value at the current index (15) is less than the value at the prior index (42). Since 15 < 42, the current index is set to 42. Then, we continue to compare 15 to each prior index. Since 15 is also < 23, index 4 is updated to 23. Next, since 15 < 16, index 3 is updated to 16. Finally, since 15 !< 8 (index 1) we'll stop and update index 2 to 15.

Now, the array is sorted!

## Efficency

* Time: O(n^2)
  * The number of iterations in the code is dependent on the length of the array. Additionally, each iteration may need to sub-iterate through previous values.
* Space: O(1)
  * No additional space is being created, since the array is being sorted in place
