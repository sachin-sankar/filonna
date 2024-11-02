from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Markdown, TabPane, TabbedContent


class FilonnaApp(App):
    TITLE = "Filonna"
    BINDINGS = [
        ("ctrl+d", "toggle_dark", "Toggle dark mode"),
        ("ctrl+q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:

        yield Header(show_clock=True, icon="🎥")
        with TabbedContent():
            with TabPane("Info", id="info"):
                yield Markdown("Info")
            with TabPane("Subtitles", id="subs"):
                yield Markdown("Hello")

        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


if __name__ == "__main__":
    app = FilonnaApp()
    app.run()
