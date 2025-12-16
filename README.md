# ReversingSudoku
This Repository contains our Explainable Machine Learning Project. We aim to create a ILP Model using Popper that extracts the rules of sudoku.



Structure: 



sudoku-popper/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── sudoku.csv              # Kaggle-Datensatz (unverändert)
│   │
│   ├── processed/
│   │   ├── puzzles.json            # Sudokus als Python-freundliches Format
│   │   ├── solutions.json
│   │   └── popper_examples.pl      # pos/neg Beispiele für Popper
│   │
│   └── samples/
│       ├── valid_sudoku.txt
│       └── invalid_sudoku.txt
│
├── src/
│   ├── __init__.py
│   │
│   ├── sudoku/
│   │   ├── __init__.py
│   │   ├── representation.py       # Grid, Konvertierungen
│   │   ├── validator.py             # Python-Sudoku-Validierung
│   │   ├── solver.py                # (optional) Backtracking-Solver
│   │   └── printer.py               # CLI/pretty print
│   │
│   ├── popper/
│   │   ├── bk.pl                    # Background Knowledge
│   │   ├── bias.pl                  # Popper Bias
│   │   ├── run_popper.py            # Python-Wrapper für Popper
│   │   └── results/
│   │       └── learned_rules.pl
│   │
│   └── preprocessing/
│       ├── __init__.py
│       ├── kaggle_loader.py         # CSV → Grid
│       ├── to_prolog.py             # Grid → Prolog
│       └── make_examples.py         # pos/neg Erzeugung
│
├── experiments/
│   ├── learn_validity.py            # Popper-Lernexperiment
│   ├── evaluate.py                  # Vergleich Python vs Popper
│   └── benchmark.py
│
├── tests/
│   ├── test_validator.py
│   ├── test_conversion.py
│   └── test_solver.py
│
└── scripts/
    ├── build_dataset.py             # komplette Pipeline
    ├── train_popper.sh
    └── check_sudoku.py

