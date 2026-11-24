import argparse
import sys
import ollama


def main():
    parser = argparse.ArgumentParser(description="Genera text amb Ollama.")
    parser.add_argument("prompt", type=str, help="El prompt a generar.")
    parser.add_argument(
        "--vegades",
        type=int,
        default=5,
        help="Nombre de vegades a generar el prompt (per defecte: 5).",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="Temperatura per la generació (per defecte: 1.0).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Llavor per reproduir resultats (per defecte: None).",
    )
    parser.add_argument(
        "--top_k",
        type=int,
        default=None,
        help="Nombre màxim de tokens candidats (per defecte: None).",
    )
    parser.add_argument(
        "--top_p",
        type=float,
        default=None,
        help="Probabilitat acumulada màxima dels tokens candidats (per defecte: None).",
    )
    parser.add_argument(
        "--num_predict",
        type=int,
        default=None,
        help="Nombre màxim de tokens a generar (per defecte: None).",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    print(f"Prompt: {args.prompt}")
    print(f"vegades: {args.vegades}")
    print(f"temperature: {args.temperature}")
    if args.seed is not None:
        print(f"seed: {args.seed}")
    if args.top_k is not None:
        print(f"top_k: {args.top_k}")
    if args.top_p is not None:
        print(f"top_p: {args.top_p}")
    if args.num_predict is not None:
        print(f"num_predict: {args.num_predict}")
    print()

    for i in range(1, args.vegades + 1):
        options = {"temperature": args.temperature}
        if args.seed is not None:
            options["seed"] = args.seed
        if args.top_k is not None:
            options["top_k"] = args.top_k
        if args.top_p is not None:
            options["top_p"] = args.top_p
        if args.num_predict is not None:
            options["num_predict"] = args.num_predict

        response = ollama.generate(
            model="gemma3:4b",
            prompt=args.prompt,
            options=options,
        )
        tokens = response.get("eval_count")
        print(f"{i}. {response['response'].strip()}")
        print(f"   tokens generats (eval_count): {tokens}")


if __name__ == "__main__":
    main()