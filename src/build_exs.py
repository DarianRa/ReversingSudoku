# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]

import os
import kagglehub
from kagglehub import KaggleDatasetAdapter
from sudoku.sudoku import sudoku

DATA_PER_TYPE = 1
OUTPUT_PATH = "data/processed/exs.pl"

# Load the dataset
file_path = "sudoku.csv"
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "rohanrao/sudoku",
    file_path,
)

def get_data(data_per_type=DATA_PER_TYPE, output_path=OUTPUT_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    exs_lines = [":- discontiguous neg/1.\n:- discontiguous pos/1.\n\n"]

    for idx, row in df.iterrows():
        if idx >= data_per_type:
            break

        puzzle = row["puzzle"]
        solution = row["solution"]

        s = sudoku(solution)

        exs_str = s.print_exs_format()
        for type in ['row', 'col', 'block']:
            for idx in range(9):
                    exs_fake = s.print_exs_format_isolated_errors(type, idx)
                    exs_lines.append(exs_fake)
        exs_lines.append(exs_str)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(exs_lines))

    print(f"Wrote {len(exs_lines)} examples to {output_path}")

get_data()
