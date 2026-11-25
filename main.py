"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene to /output/entry.txt. The scene is a
fixed, hand-written constant, so the program is fully deterministic:
it writes exactly the same text on every run, with no randomness,
no clock, no network and no input from anywhere else.
"""

import os

SCENE = (
    "My birthday cake collapsed, so Dad rebuilt it with duct tape. "
    "Mum lit the candles anyway and said, \"Make a wish. "
    "It's already holding together.\""
)

MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def main():
    scene = SCENE.strip()
    lines = scene.splitlines()
    if not scene:
        raise ValueError("scene is empty")
    if len(lines) > 2:
        raise ValueError("scene must be one or two lines")
    if len(scene) > MAX_CHARS:
        raise ValueError("scene is longer than 280 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(scene + "\n")
    # Self-check: what landed on disk is exactly the scene, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == scene + "\n", "entry.txt does not match the scene"
    assert len(written.rstrip("\n")) <= MAX_CHARS, "entry.txt is too long"


if __name__ == "__main__":
    main()
