import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


# Documentação pública que deve permanecer consistente
DOCUMENTS = [
    ROOT / "README.md",
    ROOT / "CHAPTERS.md",
]

DOCUMENTS.extend(
    sorted((ROOT / "docs").rglob("*.md"))
)

DOCUMENTS.extend(
    sorted((ROOT / "chapters").rglob("*.md"))
)


patterns = [
    r"(?<![\w.-])(data/[A-Za-z0-9_./*=-]+)",
    r"(?<![\w.-])(src/[A-Za-z0-9_./-]+)",
    r"(?<![\w.-])(scripts/[A-Za-z0-9_./-]+)",
    r"(?<![\w.-])(tests/[A-Za-z0-9_./-]+)",
    r"(?<![\w.-])(chapters/[A-Za-z0-9_./-]+)",
    r"(?<![\w.-])(docs/[A-Za-z0-9_./-]+)",
    r"(?<![\w.-])(config/[A-Za-z0-9_./-]+)",
    r"(?<![\w.-])(notebooks/[A-Za-z0-9_./-]+)",
]


# Caminhos que são gerados durante a execução dos laboratórios
# e não precisam existir em um checkout limpo.
generated = (
    "data/bronze",
    "data/silver",
    "data/gold",
    "data/quarantine",
    "data/checkpoints",
    "data/delta/smoke_test",
)


# Referências textuais que podem parecer caminhos,
# mas não representam arquivos ou diretórios reais.
ignored_refs = {
    "data/hora",
}


def is_generated_path(ref: str) -> bool:
    return any(
        ref == prefix
        or ref.startswith(prefix + "/")
        for prefix in generated
    )


refs: set[str] = set()


for document in DOCUMENTS:

    if not document.exists():
        continue

    text = document.read_text(
        encoding="utf-8"
    )

    for pattern in patterns:

        for ref in re.findall(
            pattern,
            text,
        ):
            refs.add(
                ref.rstrip(
                    ".,);`\\\"'"
                )
            )


failures = []


for ref in sorted(refs):

    # Ignora expressões textuais que não são caminhos reais.
    if ref in ignored_refs:
        continue

    # Ignora caminhos produzidos pelos pipelines.
    if is_generated_path(ref):
        continue

    # Valida referências que utilizam wildcard.
    if "*" in ref:

        if not list(
            ROOT.glob(ref)
        ):
            failures.append(
                (
                    ref,
                    "glob sem arquivos",
                )
            )

        continue

    path = ROOT / ref

    if path.exists():
        continue

    failures.append(
        (
            ref,
            "ausente",
        )
    )


if failures:

    for ref, reason in failures:
        print(
            f"FAIL {ref}: {reason}"
        )

    raise SystemExit(1)


print(
    "PATH_AUDIT_OK "
    f"references={len(refs)} "
    "missing=0"
)