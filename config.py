import os

def load_config():
    return {
        "input_path": os.environ.get("INPUT_PATH", "input.md"),
        "output_path": os.environ.get("OUTPUT_PATH", "output.pdf")
    }
