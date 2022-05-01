import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Gerência de Bebum Application")

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("🍺 Uhooo! Beer added to database 🍺")


#    else:
#       print("😔 Oh nooooo! The beer was not added to database 😔")


@main.command("list")
def list_(style: Optional[str] = None):
    """Lists the beers from database"""
    beers = get_beers_from_database()
    table = Table(title=":beer_mug: Beerlog :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%d-%M-%Y")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    table.add_row("", "", "", "", "(Date in BRT)")
    console.print(table)
