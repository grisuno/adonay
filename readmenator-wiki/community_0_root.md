# root

*Community 0 | 1 files | cohesion 1.00*

## Definition

This community groups 1 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `calcular_gematría`, `obtener_gematría_palabra`, `obtener_palabra`, `obtener_significados`, `significado_gematría`. Core file: `app.py` (5 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 5 | no |

## Key Symbols

- `calcular_gematría` (function, `app.py:1`) `def calcular_gematría(letra)`
- `obtener_gematría_palabra` (function, `app.py:14`) `def obtener_gematría_palabra(palabra)`
- `obtener_significados` (function, `app.py:19`) `def obtener_significados(letras)`
- `obtener_palabra` (function, `app.py:58`) `def obtener_palabra(letras)`
- `significado_gematría` (function, `app.py:97`) `def significado_gematría(suma)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `app.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
