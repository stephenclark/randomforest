/*
SELECT table1.ID, table1.VAR1,  table1.VAR2, table1.VAR3, table2.VAR4, table2.VAR5, table2.VAR6, table2.VAR7, table2.VAR8, table2.VAR9, table2.VAR10, table1.OUTCOME
FROM table1 JOIN table2 ON table1.ID = table2.ID;

+--------+------+------+------+------+------+------+------+------+------+-------+---------+
| ID     | VAR1 | VAR2 | VAR3 | VAR4 | VAR5 | VAR6 | VAR7 | VAR8 | VAR9 | VAR10 | OUTCOME |
+--------+------+------+------+------+------+------+------+------+------+-------+---------+
|  25033 |   32 |    1 |    0 | N    | N    | N    | L    | N    | N    | N     |       1 |
|  25037 |   33 |    1 |    0 | N    | N    | N    | N    | N    | N    | N     |       0 |
|  25039 |   73 |    1 |    0 | L    | L    | L    | H    | N    | L    | H     |       0 |
|  25044 |   56 |    1 |  441 | N    | N    | N    | H    | N    | N    | N     |       1 |
|  25086 |   82 |    0 |    0 | L    | N    | L    | H    | N    | L    | N     |       0 |
|  25109 |   27 |    0 |    7 | N    | H    | N    | N    | N    | N    | N     |       1 |
|  25121 |   75 |    0 |  261 | N    | L    | N    | N    | N    | L    | N     |       1 |
|  25130 |   39 |    0 |    1 | N    | N    | N    | L    | N    | N    | N     |       0 |
|  25136 |   36 |    0 |    0 | N    | N    | N    | L    | N    | N    | N     |       1 |
|  25157 |   25 |    0 |    0 | N    | N    | N    | N    | N    | N    | N     |       1 |
|  25161 |   61 |    0 |    0 | N    | N    | N    | N    | N    | N    | N     |       1 |
|  25168 |   62 |    2 |    0 | N    | H    | N    | H    | N    | N    | N     |       1 |
|  25177 |   63 |    1 |    0 | L    | N    | L    | N    | N    | L    | N     |       0 |
|  25230 |   72 |    1 |  107 | N    | N    | N    | N    | N    | L    | N     |       0 |
|  25231 |   21 |    0 |    0 | N    | N    | N    | N    | N    | N    | N     |       0 |


SELECT table1.VAR1,  table1.VAR2, table1.VAR3, table2.VAR4, table2.VAR5, table2.VAR6, table2.VAR7, table2.VAR8, table2.VAR9, table2.VAR10, table1.OUTCOME
FROM table1 JOIN table2 ON table1.ID = table2.ID;


*/