import re

from pypaperless import Paperless

pattern = re.compile(r"[^_]+_\d{4}-\d{2}-\d{2}_(.+)")


def main(endpoint: str, token: str, dry_run=True, verbose=True):
    client = Paperless(endpoint=endpoint, token=token)

    documents = client.get_documents()

    filtered = list(filter(lambda doc: pattern.match(doc.title), documents))

    for doc in filtered:
        match = pattern.findall(doc.title)[0]
        if verbose:
            print(f"{doc.title:<80} {match}")
        if not dry_run:
            doc.title = match
            client.save(doc)


if __name__ == "__main__":
    from argparse import ArgumentParser, BooleanOptionalAction

    parser = ArgumentParser()
    parser.add_argument("endpoint")
    parser.add_argument("token")
    parser.add_argument("--dry-run", "-n", dest="dry_run", action=BooleanOptionalAction)
    args = parser.parse_args()

    main(endpoint=args.endpoint, token=args.token, dry_run=args.dry_run)
