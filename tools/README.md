# Tools

Helper scripts for course notebooks (I/O, objectives, clarity, splitting).

## Clarity and objectives

- **`clarity_multi.py`** – Multi-course clarity pass. Run from repo root.
  - `python tools/clarity_multi.py all` – Run objectives scripts, then duplicate Story removal, then optional terse I/O expansion.
  - `python tools/clarity_multi.py objectives` – Run only objectives (objectives_multi, c03/c04/c06/c07, clarity_updates_c05).
  - `python tools/clarity_multi.py story` – Remove duplicate "The Story | القصة" cells when intro already has "The Story: X" + before/after.
  - `python tools/clarity_multi.py io` – Expand terse Inputs/Outputs where mapped (see `TERSE_IO_UPDATES`).
  - Skips `DOCS`, `PROJECTS`, `.ipynb_checkpoints`.

- **`split_large_code_cells.py`** – Split oversized code cells that contain `# PART 1:`, `# PART 2:`, … section markers.
  - `python tools/split_large_code_cells.py` – Run on all Course 01–12 notebooks.
  - `--min-lines N` / `--min-chars N` – Thresholds (default 80 lines, 3500 chars).
  - Skips `DOCS`, `PROJECTS`, `.ipynb_checkpoints`. Optional `BLOCKLIST` in script.
  - Prints a report of which notebooks and cells were split.

## Suggested workflow

1. Run objectives: `python tools/clarity_multi.py objectives`
2. Run Story + I/O: `python tools/clarity_multi.py all` (or `story` / `io` only)
3. Split large code cells: `python tools/split_large_code_cells.py`

## Other tools

- `add_inputs_outputs_multi.py`, `objectives_multi.py` – Add I/O sections and replace generic objectives (courses 01, 02, 08–12).
- Per-course: `add_inputs_outputs_c03`–`c07`, `c03`–`c07_specific_objectives`, `clarity_updates_c05`.
