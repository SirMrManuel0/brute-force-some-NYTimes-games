import argparse
from scripts import letterboxed
from scripts import wordle


def handle_command(args):
    if args.game == "letterboxed":
        letterboxed.index()
    elif args.game == "wordle":
        wordle.index()
    else:
        print(f"Unknown command: {args.command}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("game", choices=["letterboxed", "wordle"], help="letterboxed or wordle")

    args = parser.parse_args()

    handle_command(args)
   
   
   
