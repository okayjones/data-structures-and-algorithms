# Hashtables

A hashtable allows key/value pairs to be easy stores and access using a hash algorithm.

## Challenge

Create a hashtable implementation with methods for: add, get, contains, and hash.

## Approach & Efficiency

LinkedList was used for key/value storage in the Hashtable.

| Method | Time | Space |
|-|-|-|
| hash | O(1) | O(1) |
| add | O(1) | O(1) |
| get | O(n) | O(n) |
| contains | O(n) | O(n) |

## API

| Method | Params | Return |
|-|-|-|
| hash | key | str |
| add | key, value | n/a |
| get | key | value |
| contains | key | bool |
