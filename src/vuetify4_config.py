"""Demo to show how to update a Vuetify 4 config file."""

from __future__ import annotations

from pathlib import Path
from typing import Final, cast

from trame.app import get_server
from trame.ui.vuetify4 import SinglePageLayout
from trame.widgets import vuetify4 as v4
from trame_server import Server

resources_folder = Path(__file__).parent / "assets"

VUETIFY3_OVERRIDES = {
    "defaults": {
        # This makes the VBtns capitalized again: https://vuetifyjs.com/en/getting-started/upgrade-guide/#themes
        "VBtn": {
            "class": "text-uppercase",
        },
    },
    # This restores the breakpoints: https://vuetifyjs.com/en/getting-started/upgrade-guide/#breakpoints
    "display": {
        "thresholds": {
            "md": 960,
            "lg": 1280,
            "xl": 1920,
            "xxl": 2560,
        },
    },
    # Restore light theme as the default, not system: https://vuetifyjs.com/en/getting-started/upgrade-guide/#themes
    "theme": {
        "defaultTheme": "light",
    },
}

USE_VUETIFY3_STYLES: Final[bool] = False


class Vuetify4ConfigExample:
    def __init__(self) -> None:
        self.server = cast("Server", get_server(None))

        if USE_VUETIFY3_STYLES:
            self.server.state.trame__vuetify3_config = VUETIFY3_OVERRIDES
            serve_vuetify3_css_layer(self.server)

        self.build_ui()

    def build_ui(self) -> None:
        with SinglePageLayout(self.server) as layout, layout.content:
            v4.VBtn(children="click me")


def serve_vuetify3_css_layer(server: Server | None) -> None:
    """Serve custom JavaScript content, and static files.

    Parameters
    ----------
    server: Server | None
        The server object from SmartScan.
    """
    if server is not None:
        server.enable_module(
            {
                "serve": {
                    "example": str(resources_folder),
                },
                # "scripts": ["example/index.js"],
                "styles": ["example/vuetify3-reversion-layer.css"],
            },
        )


if __name__ == "__main__":
    app = Vuetify4ConfigExample()
    app.server.start()
