import json
import sys
from pathlib import Path

RUNTIME = Path(__file__).resolve().parent
PROJECT_ROOT = RUNTIME.parent


def main():
    if len(sys.argv) != 2:
        print(
            "Usage: python -m runtime.cli <project-input.json>",
            file=sys.stderr,
        )
        sys.exit(2)

    input_file = Path(sys.argv[1]).resolve()

    if not input_file.exists():
        print(f"Input file not found: {input_file}", file=sys.stderr)
        sys.exit(2)

    sys.path.insert(0, str(RUNTIME))

    from orchestrator.workflow import run_file

    result = run_file(input_file)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
