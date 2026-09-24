"""Example to verify Vuetify v3 functions normally with the v4 update.

This isn't meant to show off anything, just verifies that existing Trame
projects using v3 lab aren't impacted by the v4 update.
"""

from __future__ import annotations

from typing import cast

from trame.app import get_server
from trame.decorators import TrameApp
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import html
from trame.widgets import vuetify3 as v3
from trame_server import Server

v3.enable_lab()


@TrameApp()
class DemoApp:
    def __init__(self) -> None:
        self.server = cast("Server", get_server(None))
        self.state = self.server.state

        self.my_component = TodoList(app=self)
        self.build_ui()

    def build_ui(self) -> None:
        with SinglePageLayout(self.server) as layout, layout.content:
            self.my_component.build_ui()


class TodoList:
    def __init__(self, app: DemoApp) -> None:
        self.app = DemoApp
        self.state = app.state

        self.state.items = [
            {
                "title": "Find File",
                "subtitle": "Open general search",
                "prependIcon": "mdi-file-find",
                "value": "find-file",
            },
            {
                "title": "Open Project",
                "subtitle": "Open an existing project",
                "prependIcon": "mdi-folder-open",
                "value": "open-project",
            },
            {"type": "divider"},
            {"type": "subheader", "title": "Settings"},
            {
                "title": "Help",
                "subtitle": "View documentation",
                "prependIcon": "mdi-help-circle-outline",
                "value": "help",
            },
        ]
        self.state.search = ""

        self.state.todo_list = []
        self.state.selected_todo_indexes = []
        self.state.current_todo_text = ""

    def build_ui(self) -> None:
        with html.Div(classes="h-75 w-100 justify-items-center"):  # noqa: SIM117
            with html.Div(classes="h-100 w-33 pt-4 d-flex flex-column"):
                with html.Div(classes="d-flex ga-3 align-center"):
                    v3.VTextField(
                        label="Create a new todo:",
                        v_model=("current_todo_text",),
                        hide_details=True,
                    )
                    v3.VBtn(
                        children="Add Todo",
                        click=self.add_new_todo,
                        disabled=("current_todo_text.length === 0",),
                    )
                    with (
                        v3.VCommandPalette(
                            v_model_search=("search",),
                            items=("items",),
                            placeholder="Search commands...",
                            hotkey="ctrl+shift+k",
                            click_item=(self.on_item_click, "[]", "{item: $event}"),
                        ),
                        v3.Template(
                            v_slot_activator=("{ props: activatorProps }"),
                        ),
                    ):
                        v3.VBtn(
                            v_bind=("activatorProps",),
                            children="Open Command Palette",
                        )

                with v3.VList(classes="overflow-y-auto flex-grow-1"):  # noqa: SIM117
                    with v3.VListItem(
                        v_for=("(todo_item, index) in todo_list",),
                    ):
                        v3.VCheckbox(
                            label=("todo_item",),
                            model_value=("selected_todo_indexes.includes(index)",),
                            change=(
                                self.on_todo_select,
                                "[]",
                                "{todo_index: index, is_now_checked: $event.target.checked}",
                            ),
                            hide_details=True,
                        )

                with html.Div(classes="d-flex flex-column"):
                    v3.VBtn(
                        children="{{ selected_todo_indexes.length === todo_list.length ? 'Remove All Todos' : 'Remove Selected Todos' }}",
                        click=self.remove_selected_todos,
                        disabled=("selected_todo_indexes.length === 0",),
                        append_icon=(
                            "selected_todo_indexes.length === todo_list.length ? 'mdi-check-all' : 'mdi-check'",
                        ),
                    )
                    html.P(
                        classes="text-body-medium",
                        children="Selected todos: {{ selected_todo_indexes }}",
                    )

    def on_todo_select(self, todo_index: int, is_now_checked: bool) -> None:
        if is_now_checked:
            self.state.selected_todo_indexes.append(todo_index)
        else:
            self.state.selected_todo_indexes.remove(todo_index)

        # Without this, the indexes don't update!
        self.state.dirty("selected_todo_indexes")

    def add_new_todo(self) -> None:
        self.state.todo_list.append(self.state.current_todo_text)
        print(f"Added new todo: {self.state.current_todo_text}")
        self.state.current_todo_text = ""

        self.state.dirty("todo_list")

    def remove_selected_todos(self) -> None:
        new_todos = [
            todo
            for index, todo in enumerate(self.state.todo_list)
            if index not in self.state.selected_todo_indexes
        ]

        self.state.todo_list = new_todos
        self.state.selected_todo_indexes = []

    def on_item_click(self, item: dict[str, str]) -> None:
        print(item)


if __name__ == "__main__":
    app = DemoApp()
    app.server.start()
