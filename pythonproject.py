import random
import string
import sys

def generate_palette(n=5):
    """Return a list of `n` random hex colours."""
    palette = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        palette.append(f"#{r:02x}{g:02x}{b:02x}")
    return palette

def generate_password(length=16):
    """Build a random password and return it with a simple strength label."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd = "".join(random.choice(chars) for _ in range(length))
    strength = "💪 Strong" if length >= 12 else "⚠️ Weak"
    return pwd, strength

def analyze_numbers(numbers):
    """Return statistics for a list of numbers."""
    if not numbers:
        return {}
    total = sum(numbers)
    mean = total / len(numbers)
    sorted_n = sorted(numbers)
    mid = len(sorted_n) // 2
    median = sorted_n[mid]
    return {
        "Mean": round(mean, 2),
        "Median": median,
        "Max": max(numbers),
        "Min": min(numbers),
        "Sum": total,
    }

def roll_dice(sides=6, count=2):
    """Roll `count` dice with `sides` sides and return the rolls, total and a message."""
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls)
    if total == count * sides:
        msg = "🎉 JACKPOT!"
    elif total >= count * sides * 0.7:
        msg = "😄 Great Roll!"
    else:
        msg = "🎲 Try Again!"
    return rolls, total, msg

def main():
    menu = (
        "\n"
        "Select a project:\n"
        "1. 🎨 Color Palette Generator\n"
        "2. 🔐 Password Generator\n"
        "3. 📊 Number Stats\n"
        "4. 🎲 Dice Roll Game\n"
        "0. Exit\n"
        "Choice: "
    )

    while True:
        try:
            choice = input(menu).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if choice == "0":
            print("Goodbye!")
            break
        if choice == "1":
            n = input("How many colours? [5] ").strip()
            n = int(n) if n.isdigit() and int(n) > 0 else 5
            print("Your Palette:", generate_palette(n))
        elif choice == "2":
            l = input("Password length? [16] ").strip()
            length = int(l) if l.isdigit() and int(l) > 0 else 16
            pwd, strength = generate_password(length)
            print(f"Password: {pwd}")
            print(f"Strength: {strength}")
        elif choice == "3":
            line = input("Enter numbers separated by spaces: ")
            try:
                nums = [float(x) for x in line.strip().split()]
            except ValueError:
                print("Invalid input, please enter only numbers.")
                continue
            stats = analyze_numbers(nums)
            for k, v in stats.items():
                print(f"{k}: {v}")
        elif choice == "4":
            s = input("Sides per die? [6] ").strip()
            c = input("Number of dice? [2] ").strip()
            sides = int(s) if s.isdigit() and int(s) > 0 else 6
            count = int(c) if c.isdigit() and int(c) > 0 else 2
            rolls, total, msg = roll_dice(sides, count)
            print(f"Rolled: {rolls}")
            print(f"Total: {total}")
            print(f"Result: {msg}")
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()