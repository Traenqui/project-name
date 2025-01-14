"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Project Name."""


if __name__ == "__main__":
    main(prog_name="project-name")  # pragma: no cover
