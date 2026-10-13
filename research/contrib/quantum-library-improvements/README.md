# Quantum-code library improvements — reference package

This branch publishes the English package discussed with Vincent Russo on 2026-10-13.

## Package

`QUANTUM_CODE_LIBRARY_IMPROVEMENTS_20261012_EN.zip`

The archive contains three small reference components plus tests:

- `symplectic_doubling.py` — shared CSS/non-CSS symplectic-doubling backend with Pauli-weight rescore.
- `proof_gate.py` — prevents heuristic/PARTIAL distance evidence from being presented as exact/headline distance.
- `resweep_queue.py` — builds a priority queue for fresh-seed re-checks of non-EXACT records.

It also includes an architecture note connecting discovery -> verification -> syndrome circuits -> decoder -> logical ISA -> hardware scheduler.

## Test status

The package was repackaged with English documentation and the regression tests were rerun: **7/7 PASS**.

## Scope

This is a reference/prototype package for discussion. It does not claim a new quantum-code parameter record, and it is not presented as an upstream-ready patch. The useful question is which pieces, if any, should be adapted to the repository's existing proof/replay and distance-evidence workflow.
