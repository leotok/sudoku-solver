# Sudoku Solver

## Representation
```
tabuleiro = [
    [0,0,0,7,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,4,3,0,2,0,0],
    [0,0,0,0,0,0,0,0,6],
    [0,0,0,5,0,9,0,0,0],
    [0,0,0,0,0,0,4,1,8],
    [0,0,0,0,8,1,0,0,0],
    [0,0,2,0,0,0,0,5,0],
    [0,4,0,0,0,0,3,0,0],
]
```

## Results

1. Backtracking normal
    - Turnos: 24.396.706
    - Tempo: 349.2255051136017
2. Backtracking usando set para validação de jogada
    - Turnos 24.396.706
    - Tempo: 221.23285508155823
2. Backtracking usando set para validação de jogada e somatorio para fim de jogo
    - Turnos 24.396.706
    - Tempo: 191.17112708091736

```
Turno 24396706 | Nivel 64 | Max Nivel 64
|_2_|_6_|_4_|_7_|_1_|_5_|_8_|_3_|_9_|
|_1_|_3_|_7_|_8_|_9_|_2_|_6_|_4_|_5_|
|_5_|_9_|_8_|_4_|_3_|_6_|_2_|_7_|_1_|
|_4_|_2_|_3_|_1_|_7_|_8_|_5_|_9_|_6_|
|_8_|_1_|_6_|_5_|_4_|_9_|_7_|_2_|_3_|
|_7_|_5_|_9_|_6_|_2_|_3_|_4_|_1_|_8_|
|_3_|_7_|_5_|_2_|_8_|_1_|_9_|_6_|_4_|
|_9_|_8_|_2_|_3_|_6_|_4_|_1_|_5_|_7_|
|_6_|_4_|_1_|_9_|_5_|_7_|_3_|_8_|_2_|
```