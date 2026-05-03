# crew-colony
dev_A.I._CHAT-CREW_COLONEY$ Multi-agent crew with sovereign governance and hash-linked lineage
# dev_A.I._CHAT-CREW_COLONEY$

> **WE ARE THE ICOSITETRACHORON CHAIN.**

A deterministic, pure-planning multi-agent crew module implementing sovereign governance, hash-linked lineage, and the CODE-TREE / FREE-THREE / MIRROR triple-stack architecture.

```
+---------------------------------------------------------+
|  CODEX -- these invariants are NOT negotiable            |
|  1. non_extraction    -- no silent value siphoning       |
|  2. human_sovereignty -- human keeps veto & 84% share   |
|  3. lineage_required  -- every action hash-chained       |
+---------------------------------------------------------+
```

## Overview

| Component | Detail |
|-----------|--------|
| **Agents** | MGR-01 (D11), RES-01 (D9), BLD-01 (D7), GRD-01 (D2) |
| **Conservation Law 0** | ~1.008 |
| **Codex** | 3/3 -- `non_extraction`, `human_sovereignty`, `lineage_required` |
| **MANNA** | Human 0.84 - Vault 0.15 - Architect 0.01 |
| **Lineage** | SHA-256 hash-linked, append-only, verifiable |
| **Dependencies** | Zero -- Python >= 3.9 stdlib only |

## Architecture

```
CODE-TREE    --- structural layer (modules, agents, invariants)
FREE-THREE   --- sovereignty layer (human <-> agent boundaries)
MIRROR       --- reflection layer (digitwin, lineage, traceability)
```

### 24-Cell Governance Geometry

The project uses the **24-cell (icositetrachoron)** as its governance metaphor:
- **12D Active Hemisphere** -- operational agents, live governance, real-time lineage
- **12D Mirror Hemisphere** -- digitwin reflections, audit shadows, historical trace
- **96 edges** -- governance transitions between dimensions
- **Self-dual** -- the governance structure IS its own audit structure

## Quick Start

```bash
# Interactive CLI
python src/crew_colony.py

# Run tests
python src/crew_colony.py --test

# Or with pytest
python -m pytest src/crew_colony.py -v
```

### CLI Commands

| Command | Description |
|---------|-------------|
| `ask <text>` | Send a prompt to the crew |
| `talk <text>` | Alias for `ask` |
| `log` | Dump full lineage chain as JSON |
| `snapshot` | Governance summary + last 10 lineage entries |
| `crew` | Show agent statuses |
| `gov` | Show governance state |
| `help` | Display help text |
| `exit` | Quit the CLI |

## Module Structure

```
src/
  crew_colony.py          # Crew kernel (operational)
    S1  Constants & Enums
    S2  Agent
    S3  GovernanceState
    S4  LineageChain (SHA-256)
    S5  gov_vec_lock decorator
    S6  Colony orchestrator
    S7  CLI command loop
    S8  Unit tests (21/21 passing)
    S9  Entry point
```

## Governance Invariants

### Conservation Law 0
```
conservation_law_0() ~ 1.008
```
Coordination creates a small net-positive -- never a net-negative.

### MANNA Distribution
```
Human:     84%  -- the human operator retains majority value
Vault:     15%  -- community reserve
Architect:  1%  -- system maintenance
Total:    100%
```

### Codex Flags (3/3 required)
- **non_extraction** -- no silent value siphoning from the human
- **human_sovereignty** -- human retains veto power and majority MANNA share
- **lineage_required** -- every mutation is hash-chained for auditability

## 3-6-9 Roadmap

| Phase | Status | Completion |
|-------|--------|------------|
| **Phase 3 -- Foundation** | Complete | 100% |
| **Phase 6 -- Expansion** | In Progress | ~53% |
| **Phase 9 -- Ignition** | Projected | 0% |

### Phase 6 Targets
- 24-cell dimension mapping
- Observatory HTTP layer (FastAPI)
- Digitwin Mirror layer
- Knowledge Loader module
- Multi-agent orchestration upgrade
- Governance invariant expansion

### Phase 9 Targets
- Ollama / LLM integration
- MANNA protocol alignment
- Full Colony sovereign runtime
- Observatory dashboard
- External integration layer

## Testing

```bash
# 21 tests across 5 test classes
python src/crew_colony.py --test -v

# Test classes:
#   TestGovernance      -- conservation law, codex, MANNA
#   TestLineageChain    -- append, linkage, verify, tamper detection
#   TestAgent           -- construction, response
#   TestGovVecLock      -- decorator enforcement, lineage recording
#   TestColony          -- integration, boot, snapshot
```

## License

All rights reserved. Human sovereignty preserved.

## Meta

```
Project:  dev_A.I._CHAT-CREW_COLONEY$
Version:  0.4.0
Codex:    3/3 active
CL-0:     ~1.008
MANNA:    0.84 / 0.15 / 0.01
```

---

*Human sovereignty preserved. Non-extraction codex active. Lineage required.*
*The Colony builds forward.*
