# config.py
import os

# ---- Base directories ----
# Override with environment variables, otherwise default to local './data' and './outputs'
DATA_ROOT = os.environ.get("SKIN_DATA_ROOT", os.path.join(os.path.dirname(__file__), "data"))
OUTPUT_ROOT = os.environ.get("SKIN_OUTPUT_ROOT", os.path.join(os.path.dirname(__file__), "outputs"))

# ---- Subdirectories (relative to DATA_ROOT) ----
CSV_DIR = os.path.join(DATA_ROOT, "CSVs")
IMAGE_DIR = os.path.join(DATA_ROOT, "ISIC_2019_Training_Input")

# ---- Working directories (inside OUTPUT_ROOT) ----
LABELED_DIR = os.path.join(OUTPUT_ROOT, "labeled_real")
CHECKPOINT_DIR = os.path.join(OUTPUT_ROOT, "checkpoints")
RESULTS_DIR = os.path.join(OUTPUT_ROOT, "results")

# ---- Automatic override for Kaggle (detected by environment) ----
if "KAGGLE_KERNEL_RUN_TYPE" in os.environ:
    # These paths are specific to your Kaggle dataset – adjust if needed
    CSV_DIR = "/kaggle/input/datasets/ittisamurtunib/dataset/CSVs-20260711T054424Z-2-001/CSVs"
    IMAGE_DIR = "/kaggle/input/datasets/ittisamurtunib/dataset/ISIC_2019_Training_Input/ISIC_2019_Training_Input"
    OUTPUT_ROOT = "/kaggle/working/Thesis_Outputs"
    LABELED_DIR = "/kaggle/working/data/labeled_real"
    CHECKPOINT_DIR = OUTPUT_ROOT
    RESULTS_DIR = OUTPUT_ROOT

# ---- Automatic override for Google Colab (optional) ----
# if "COLAB_GPU" in os.environ:
#     # You could set paths to your mounted Drive here, or rely on environment variables.
#     pass

# Ensure directories exist
os.makedirs(LABELED_DIR, exist_ok=True)
os.makedirs(CHECKPOINT_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# Print paths when run as script for debugging
if __name__ == "__main__":
    print(f"DATA_ROOT: {DATA_ROOT}")
    print(f"CSV_DIR: {CSV_DIR}")
    print(f"IMAGE_DIR: {IMAGE_DIR}")
    print(f"OUTPUT_ROOT: {OUTPUT_ROOT}")
    print(f"LABELED_DIR: {LABELED_DIR}")
    print(f"CHECKPOINT_DIR: {CHECKPOINT_DIR}")
    print(f"RESULTS_DIR: {RESULTS_DIR}")