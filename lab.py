import argparse
import sys
import ollama

def main():
    parser = argparse.ArgumentParser(description="Genera text amb Ollama.")
    parser.add_argument("prompt", type=str, help="El prompt a generar.")
    parser.add_argument("--vegades", type=int, default=5, help="Nombre de vegades a generar el prompt (per defecte: 5).")
    parser.add_argument("--temperature", type=float, default=1.0, help="Temperatura per la generació (per defecte: 1.0).")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    
    print(f"Prompt: {args.prompt}")
    print(f"vegades: {args.vegades}")
    print(f"temperature: {args.temperature}")
    print()
    
    for i in range(1, args.vegades + 1):
        response = ollama.generate(
            model="gemma3:4b",
            prompt=args.prompt,
            options={"temperature": args.temperature}
        )
        print(f"{i}. {response['response'].strip()}")

if __name__ == "__main__":
    main()