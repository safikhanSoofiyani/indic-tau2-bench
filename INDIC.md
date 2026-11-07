# Indic tau2-bench: changes in this copy

This repository is a copy of [sierra-research/tau2-bench](https://github.com/sierra-research/tau2-bench)
at v1.0.1 (commit `2174a60`), with the one change needed to score the
[Indic tau2-bench](https://huggingface.co/datasets/ai4bharat/indic-tau2-bench) translations
(14 Indian languages). Everything else is upstream, unchanged.

## What changed

| file | change |
|---|---|
| `src/tau2/evaluator/evaluator_communicate.py` | The COMMUNICATE check (does the agent tell the customer a required value, such as `1628`) also accepts that number written in native digits (१६२८, ১৬২৮, ۱۶۲۸ ...). ASCII-only text behaves exactly as before, so English results do not change. |
| `tests/test_communicate_digits.py` | Tests for the above. |
| `.gitignore` | Ignores locally generated `data_??/` directories. |
