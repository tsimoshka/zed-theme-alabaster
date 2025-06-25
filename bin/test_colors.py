#!/usr/bin/env python3
"""
Terminal Color Palette Display
Shows regular, bright, and dim variations of all terminal colors
"""

# ANSI escape codes
RESET = "\033[0m"
DIM = "\033[2m"

# Color names and codes
COLORS = [
    ("Black", 0),
    ("Red", 1),
    ("Green", 2),
    ("Yellow", 3),
    ("Blue", 4),
    ("Magenta", 5),
    ("Cyan", 6),
    ("White", 7),
]


def main():
    """Display the color palette"""
    # Header
    print("\n" + "═" * 60)
    print("TERMINAL COLOR PALETTE".center(60))
    print("═" * 60)
    print()

    # Column headers
    print(f"{'Color':<12} │ {'Regular':<13} │ {'Bright':<13} │ {'Dim':<13}")
    print("─" * 12 + "─┼─" + "─" * 13 + "─┼─" + "─" * 13 + "─┼─" + "─" * 13)

    # Display each color
    for name, code in COLORS:
        # Build color displays with fixed spacing
        regular = f"\033[3{code}m████{RESET} \033[4{code}m    {RESET}"
        bright = f"\033[9{code}m████{RESET} \033[10{code}m    {RESET}"
        dim = f"\033[2;3{code}m████{RESET} \033[2;4{code}m    {RESET}"

        # Print with manual spacing (9 visible chars + 4 spaces = 13)
        print(f"{name:<12} │ {regular}     │ {bright}     │ {dim}")

    print("\n" + "═" * 60)


if __name__ == "__main__":
    main()
