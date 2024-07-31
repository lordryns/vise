from textual.app import App, ComposeResult 
from textual.widgets import Header, Footer 


class ViseApp(App):
    BINDINGS = [('t', 'toggle_dark', 'Toggle dark mode'), ('q', 'exit_app', "Exit App")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark 

    
    def action_exit_app(self) -> None:
        quit(0)


    
if __name__ == '__main__':
    app = ViseApp()
    app.run()