# ColourToSpot

Clean-room research and reimplementation of the legacy Barco ArabesqueMC V3 Selective/Separate colour-separation behavior.

## Status

The repository currently contains the research scaffold for reconstructing the Selective colour-separation engine. The implementation is based on static analysis of the legacy binary behavior and is deliberately separated from the original proprietary installer/DLLs.

## Layout

- `docs/` — reverse-engineering notes and mathematical reconstruction
- `reference/` — Python reference implementation of recovered Selective behavior
- `engine/` — future production implementation
- `tests/` — regression tests
- `ui/` — future modern interface

## Important

Do not add the original Barco installer, proprietary DLLs, or other copyrighted binaries to this repository. Use the repository for the clean-room implementation, documentation, and independently created tests/assets.

## Research status

Recovered so far:

- 18 Selective regions
- RGB/CMYK sector geometry
- `ComputeFromRgb` weighted computation structure
- `ComputeFromCmyk` weighted computation structure
- integer scaling/division and clamping behavior
- RGB final inversion behavior

The remaining work includes exact parameter limits/defaults, serialization, and runtime validation against reference outputs.
