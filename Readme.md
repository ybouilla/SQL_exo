# SQL exercises

Exercises from https://www.w3resource.com/sql-exercises/sql-retrieve-from-table.php


## Principles related to databases

### ACID databases
- A: atomicity, each statement in transaction is considered as a single unit: either the entire statement is executed or
- C: consistency, constraints on table column
- I: Isolation, concurent transactions leave database in same state
- D: Durability: transaction commited,remain commited even if there is a system failure

### BASE databases

- BA: basically available: ensure availability
- Soft state: due to lack of immediate consistency, data values may change over time
- Eventualy consistant


### CAP thoerem

- Consistency: guarentees same data is everywhere the most recent
- AVailability: all request will result in a response, even if nodes are down. not always the most recent data
- Partition tolerence: system continues to operate despite network failure
