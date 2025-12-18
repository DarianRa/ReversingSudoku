# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]

import os
import kagglehub
from kagglehub import KaggleDatasetAdapter
from sudoku.sudoku import sudoku

DATA_PER_TYPE = 10
OUTPUT_PATH = "data/processed/exes.pl"

# Load the dataset
file_path = "sudoku.csv"
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "rohanrao/sudoku",
    file_path,
)

def get_data(data_per_type=DATA_PER_TYPE, output_path=OUTPUT_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    exs_lines = []

    for idx, row in df.iterrows():
        if idx >= data_per_type:
            break

        puzzle = row["puzzle"]
        solution = row["solution"]

        s = sudoku(solution)

        exs_str = s.print_exs_format()
        exs_lines.append(exs_str)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(exs_lines))

    print(f"Wrote {len(exs_lines)} examples to {output_path}")

get_data()
