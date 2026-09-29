"""Live pitch demo: memory-less vs. memory-backed reflection on the M&A integration bank."""

from hindsight_setup import get_client

EMPTY_BANK_ID = "empty-demo-bank"
SEEDED_BANK_ID = "manda-demo"

SEPARATOR = "=" * 70


def print_header(title: str) -> None:
    print()
    print(SEPARATOR)
    print(title)
    print(SEPARATOR)


def ask(client, bank_id: str, query: str) -> None:
    print(f"Q: {query}\n")
    response = client.reflect(bank_id=bank_id, query=query)
    print(response.text)


def main() -> None:
    client = get_client()

    print_header("BEFORE MEMORY")
    ask(
        client,
        EMPTY_BANK_ID,
        "What's our cloud infrastructure decision for the integration?",
    )

    print_header("AFTER MEMORY: 19 MEETING NOTES LOADED")
    ask(
        client,
        SEEDED_BANK_ID,
        "What's our cloud infrastructure decision for the integration?",
    )

    print_header("THE CATCH")
    ask(
        client,
        SEEDED_BANK_ID,
        "A team lead just proposed keeping their AWS pipeline for Q1 since it's "
        "already working. Does this conflict with any prior decision?",
    )

    print_header("OPEN CONFLICTS")
    ask(
        client,
        SEEDED_BANK_ID,
        "What integration decisions are still unresolved or contested?",
    )

    print()
    print(SEPARATOR)


if __name__ == "__main__":
    main()
