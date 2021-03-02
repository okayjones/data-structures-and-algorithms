def insertion_sort(arr: list) -> list:

  for i in range(1, len(arr)):
    last_index = i - 1
    curr_value = arr[i]

    while last_index >= 0 and curr_value < arr[last_index]:
      arr[last_index + 1] = arr[last_index]
      last_index -= 1
    
    arr[last_index + 1] = curr_value
    
  return arr
