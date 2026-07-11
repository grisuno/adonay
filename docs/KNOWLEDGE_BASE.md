# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 1 | **Total Symbols Extracted:** 5 | **Total Imports:** 0

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
    app_py["app.py (py)"]
    class app_py mod;
    app_py_calcular_gematr_a["calcular_gematría"]
    class app_py_calcular_gematr_a fn;
    app_py --> app_py_calcular_gematr_a
    app_py_obtener_gematr_a_palabra["obtener_gematría_palabra"]
    class app_py_obtener_gematr_a_palabra fn;
    app_py --> app_py_obtener_gematr_a_palabra
    app_py_obtener_significados["obtener_significados"]
    class app_py_obtener_significados fn;
    app_py --> app_py_obtener_significados
    app_py_obtener_palabra["obtener_palabra"]
    class app_py_obtener_palabra fn;
    app_py --> app_py_obtener_palabra
    app_py_significado_gematr_a["significado_gematría"]
    class app_py_significado_gematr_a fn;
    app_py --> app_py_significado_gematr_a
```

---

## Architecture Reference

### PY (1 files)

#### `app.py`
**Path:** `app.py`

**Functions:**
- `calcular_gematría` (line 1)
- `obtener_gematría_palabra` (line 14)
- `obtener_significados` (line 19)
- `obtener_palabra` (line 58)
- `significado_gematría` (line 97)
