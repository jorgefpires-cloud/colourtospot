# Reverse engineering notes

## Scope

The goal is behavioral reconstruction of the legacy Separate → Selective operation, not redistribution of the original software.

## Recovered class

`Bx_TSelective` in `bx_operations.dll`.

Important methods recovered:

- `ComputeFromRgb`
- `ComputeFromCmyk`
- `DensitoValuesOfRgb`
- `DensitoValuesOfCmyk`
- `SplitRgb`
- `SplitCmyk`
- `NrRegions`
- `GetRegionName`
- parameter getters/setters

`NrRegions()` returns 18. The parameter array is at object offset `+0x170` and contains 18 32-bit values.

## Validation policy

Every formula should be tagged as one of:

1. **Recovered** — directly supported by instruction-level analysis.
2. **Inferred** — supported by multiple binary observations but still requiring runtime comparison.
3. **Hypothesis** — useful for UI/research but not yet established.

Do not label a result pixel-perfect until it has been compared against the original runtime on captured input/parameter vectors.

## IP hygiene

Do not commit the original Barco installer, DLLs, proprietary artwork, or extracted proprietary assets to the public repository. Keep those privately for validation only.
