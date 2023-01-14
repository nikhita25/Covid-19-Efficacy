from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP,DARKLY
from src.components.layout import create_layout
import dash_bootstrap_components as dbc


def main() -> None:
    app = Dash(external_stylesheets = [DARKLY])
    app.title = 'Vaccine Efficacy Dashboard'
    app.layout = create_layout(app)
    app.run()


if __name__ == '__main__':
    main()
