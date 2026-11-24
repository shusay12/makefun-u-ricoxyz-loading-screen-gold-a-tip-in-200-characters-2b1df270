"""Loading-screen tip for stressed developers and AI coding agents.

Writes one line (1-200 characters) to /output/entry.txt.

Entry v3 (final): compression pass — "while you were staring at it" becomes
"while you blinked". Shorter (fewer bytes helps the exact-tie tie-break),
and the punch lands harder: the agent did the work in a blink, while the
human is the slow one. The joke is now that the human, not the machine,
is the bottleneck — both sides feel seen.
"""

import os

ENTRY = (
    "Tip: your AI agent is staring at this screen too, waiting for you to "
    "approve the fix it wrote while you blinked."
)


def main() -> None:
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
