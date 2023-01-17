from aoc22_types import Move
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.pretty import Pretty
from rich.spinner import Spinner
from rich.text import Text

# Use rich library: https://rich.readthedocs.io


def color(c: str) -> str:
    return {
        ">": "[bold red]:arrow_right:[/]",
        "v": "[bold red]:arrow_down:[/]",
        "<": "[bold red]:arrow_left:[/]",
        "^": "[bold red]:arrow_up:[/]",
        ".": "[dim green].[/]",
        "#": "[bold green]#[/]",
        " ": " ",
    }[c]


class Show:
    def __init__(self, pointer: "Pointer", moves: list[Move]):
        self.pointer = pointer

        self.map = pointer.map
        self.moves = moves

    def show_start(self):
        self.console = Console()
        self.body = Layout(name="body", size=24)
        self.info = Text("Hi!")
        self.spinner = Spinner("squareCorners")

        self.layout = Layout()
        self.layout.split_row(Layout(name="left", size=45))
        self.layout["left"].split(
            Layout(Pretty(self.pointer, justify="center"), size=1),
            self.body,
            Layout(self.info, name="moves", size=2),
            Layout(self.spinner, size=2),
        )

        self.live = Live(
            self.layout,
            console=self.console,
            refresh_per_second=10,
        )
        self.live.start()

    def show_stop(self):
        self.live.stop()

    def show(self, n: int | None = None, *, stop=False):

        row, col = self.pointer.pos

        if n is not None:
            move = self.moves[n]

            info = Text.assemble(
                (
                    " ".join(str(x) for x in self.moves[(n - 5) : n]),
                    "grey13",
                ),
                (f" [ {move} ] ", "bold cyan"),
                (
                    " ".join(str(x) for x in self.moves[(n + 1) : n + 5]),
                    "grey13",
                ),
                end="",
            )
            self.layout["moves"].update(info)
            if isinstance(move, int):
                self.spinner.update(text=f"Move {n} of {move}")

        body = "\n".join(
            "".join(
                color(
                    ">v<^"[self.pointer.face]
                    if (i, j) == self.pointer.pos
                    else self.map.get((i, j), " ")
                )
                for j in range(col - 20, col + 21)
            )
            for i in range(row - 10, row + 11)
        )

        self.body.update(Panel(body, border_style="cyan"))
