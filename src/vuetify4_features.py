from __future__ import annotations

from trame.app import get_server
from trame.decorators import TrameApp
from trame.ui.vuetify4 import SinglePageLayout
from trame.widgets import html
from trame.widgets import vuetify4 as v4

# Note: Some components in this example are exclusive to v4 labs, to ensure they're available:
v4.enable_lab()


@TrameApp()
class DemoApp:
    """Mini Trame app."""

    def __init__(self) -> None:
        self.server = get_server(None)
        self.state = self.server.state

        self.my_component = MyComponent(app=self)
        self.build_ui()

    def build_ui(self) -> None:
        with SinglePageLayout(self.server) as layout, layout.content:
            self.my_component.build_ui()


class MyComponent:
    def __init__(self, app: DemoApp) -> None:
        self.app = DemoApp
        self.state = app.state

        self.progress_example = ProgressExample(app=app)
        self.highlight_example = HighlightExample(app=app)
        self.date_range_picker_example = DateRangePickerExample(app=app)
        self.heatmap_example = HeatmapExample(app=app)
        self.month_picker_example = MonthPickerExample(app=app)
        self.hero = Hero(app=app)

        # Initialize it to 0
        self.state.count = 0

    def build_ui(self) -> None:
        with v4.VSheet(color="background", classes="showcase-bg min-h-screen"):  # noqa: SIM117
            with v4.VContainer(max_width="1320", classes="py-16"):
                self.hero.build_ui()
                with html.Section(classes="mt-16"):
                    with html.Div(
                        classes="d-flex flex-column flex-sm-row align-sm-end justify-space-between ga-4 mb-4"
                    ):
                        with html.Div():
                            html.Div(
                                classes="text-label-small text-primary text-uppercase font-weight-bold mb-3",
                                children="Actually new",
                            )
                            html.H2(children="Components v3.13 doesn't export")
                        v4.VChip(color="warning", variant="tonal", children="Labs APIs")
                    html.P(
                        classes="text-body-large text-medium-emphasis mb-10",
                        children="These aren't renamed v3 components. They're new component families available on the v4 side.",
                    )
                    self.date_range_picker_example.build_ui()
                    with v4.VRow():
                        with v4.VCol(cols=12, lg=5):
                            self.month_picker_example.build_ui()
                        with v4.VCol(cols=12, lg=7):
                            self.heatmap_example.build_ui()
                    with v4.VRow():
                        with v4.VCol(cols=12, lg=7):
                            self.highlight_example.build_ui()
                        with v4.VCol(cols=12, lg=5):
                            self.progress_example.build_ui()

    def increment_counter(self) -> None:
        self.state.count += 1


class ProgressExample:
    def __init__(self, app: DemoApp) -> None:
        """Progress."""
        self.state = app.state

        self.state.migration_progress = 74

    def build_ui(self) -> None:
        with v4.VCard(
            classes="overflow-hidden",
            rounded="xl",
            elevation="0",
            height="100%",
            border=True,
        ):
            with html.Div(classes="pa-8"):
                with html.Div(
                    classes="d-flex align-center ga-3 text-label-medium font-weight-bold"
                ):
                    html.Span(classes="text-primary", children="05")
                    html.Span(" &lt;VProgress /&gt;")
                html.H3(
                    classes="text-headline-medium font-weight-bold mt-6",
                    children="Progress with meaning attached.",
                )
                html.P(
                    classes="text-body-large text-medium-emphasis mt-4",
                    children="Label, value formatting, max values and accessible progress semantics in one higher-level API.",
                )

            v4.VDivider()

            with html.Div(classes="stage-bg pa-8"):
                with html.Div(
                    classes="d-flex align-end justify-space-between ga-4 mb-6"
                ):
                    with html.Div():
                        html.Div(
                            classes="text-body-small text-medium-emphasis",
                            children="Migration readiness",
                        )
                        html.Div(
                            classes="text-headline-large font-weight-bold mt-1",
                            children="{{ migration_progress }}%",
                        )

                    html.Div(
                        classes="text-body-small text-medium-emphasis",
                        children="12 / 16 modules",
                    )

                v4.VProgress(
                    model_value=("migration_progress",),
                    label="Migration readiness",
                    color="primary",
                    bg_color="surface-variant",
                    rounded=True,
                    hide_label=True,
                    value_format=("({ percent }) => `${Math.round(percent)}% ready`",),
                )

                v4.VSlider(
                    v_model=("migration_progress",),
                    classes="mt-6",
                    min=10,
                    max=100,
                    step=1,
                    color="primary",
                    hide_details=True,
                )

                v4.VBtn(
                    classes="mt-6",
                    variant="tonal",
                    color="primary",
                    block=True,
                    rounded="lg",
                    append_icon="mdi-arrow-up",
                    # @click="randomizeMigration"
                    children="Ship another module",
                )


class HighlightExample:
    def __init__(self, app: DemoApp) -> None:
        """Highlight."""
        self.state = app.state

        self.state.search_copy = "Vuetify 4 turns migration work into product capability: richer scheduling, native heatmaps, first-party highlighting, better progress semantics, and a cleaner foundation for the next generation of Vuetify."
        self.state.search_query = "migration"

    def build_ui(self):
        with v4.VCard(
            classes="overflow-hidden",
            rounded="xl",
            elevation="0",
            height="100%",
            border=True,
        ):
            with html.Div(classes="pa-8"):
                with html.Div(
                    classes="d-flex align-center ga-3 text-label-medium font-weight-bold"
                ):
                    html.Span(classes="text-primary", children="04")
                    html.Span(" &lt;VHighlight /&gt;")
                html.H3(
                    classes="text-headline-medium font-weight-bold mt-6",
                    children="Search UIs no longer need string-splitting soup.",
                )
                html.P(
                    classes="text-body-large text-medium-emphasis mt-4",
                    children="Feed it text and a query. Vuetify handles matched segments while preserving a semantic text flow.",
                )
                v4.VDivider()

            with html.Div(classes="stage-bg pa-8"):
                v4.VTextField(
                    v_model=("search_query",),
                    label="Search this result",
                    placeholder="Try: migration",
                    variant="outlined",
                    rounded="lg",
                    hide_details=True,
                    clearable=True,
                )

                with v4.VSheet(
                    border=True,
                    rounded="lg",
                    color="surface",
                    classes="pa-6 mt-6",
                ):
                    with html.Div(
                        classes="d-flex ga-2 text-label-small text-medium-emphasis mb-3"
                    ):
                        html.Span("MIGRATION_GUIDE.md")
                        html.Span("·")
                        html.Span("84% match")

                    with html.Div(classes="text-body-large"):
                        v4.VHighlight(
                            text=("search_copy",),
                            query=("search_query",),
                            ignore_case=True,
                            match_all=True,
                            color="primary",
                            mark_class="migration-mark",
                        )


class DateRangePickerExample:
    def __init__(self, app: DemoApp) -> None:
        """DateRangePicker."""
        self.state = app.state

        self.state.date_range = ["2026-09-08", "2026-09-22"]
        self.state.independent_months = False

    def build_ui(self) -> None:
        with v4.VCard(  # noqa: SIM117
            classes="overflow-hidden mb-6", rounded="xl", elevation="0", border=True
        ):
            with v4.VRow(no_gutters=True):
                with v4.VCol(cols=12, lg=4, classes="pa-8"):
                    with html.Div(
                        classes="d-flex align-center ga-3 text-label-medium font-weight-bold"
                    ):
                        html.Span(classes="component-number", children="01")
                        html.Span(" &lt;VDateRangePicker /&gt;")

                    html.H3(
                        classes="text-headline-medium font-weight-bold mt-6",
                        children="Date ranges without assembling two calendars yourself.",
                    )
                    html.P(
                        classes="text-body-large text-medium-emphasis mt-4",
                        children="Two synchronized picker panels, range selection, cross-panel navigation, and an optional independent-month mode.",
                    )
                    # TODO: Figure this out, its computed
                    v4.VChip(
                        classes="mt-6",
                        variant="outlined",
                        size="small",
                        children="{{ formatted_date_range }}",
                    )

                    v4.VSwitch(
                        v_model=("independent_months",),
                        color="primary",
                        label="Independent months",
                        hide_details=True,
                        classes="mt-4",
                    )

                with v4.VCol(
                    cols=12, lg=4, classes="stage-bg border-s-lg pa-6 overflow-auto"
                ):
                    with html.Div(classes="d-flex justify-end mb-4"):
                        v4.VChip(
                            size="x-small", variant="tonal", children="Interactive"
                        )
                    with html.Div(classes="d-flex justify-center"):
                        v4.VDateRangePicker(
                            v_model=("date_range",),
                            independent_months=("independent_months",),
                            color="primary",
                        )


class HeatmapExample:
    def __init__(self, app: DemoApp) -> None:
        """Heatmap."""
        self.state = app.state

        self.state.week_rows = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        self.state.week_columns = [f"W{i + 1}" for i in range(12)]
        self.state.heatmap_items = [
            {
                "row": row,
                "column": column,
                "value": (
                    (col_idx + 3) * 17 + (row_idx + 2) * 23 + col_idx * row_idx * 7
                )
                % 100,
            }
            for col_idx, column in enumerate(self.state.week_columns)
            for row_idx, row in enumerate(self.state.week_rows)
        ]

        self.state.heatmap_thresholds = [
            {"min": "0", "color": "#172033"},
            {"min": "20", "color": "#193b4d"},
            {"min": "40", "color": "#1d6370"},
            {"min": "60", "color": "#20a08c"},
            {"min": "80", "color": "#55d6a9"},
        ]
        self.state.heatmap_legend = {
            "labels": [
                "Quiet",
                "Low",
                "Normal",
                "Busy",
                "Hot",
            ],
        }

        self.state.cell_size = [24, 24]

    def build_ui(self) -> None:
        with v4.VCard(
            classes="overflow-hidden",
            rounded="xl",
            elevation="0",
            height="100%",
            border=True,
        ):
            with html.Div(classes="pa-8"):
                with html.Div(
                    classes="d-flex align-center ga-3 text-label-medium font-weight-bold"
                ):
                    html.Span(classes="text-primary", children="03")
                    html.Span(" &lt;VHeatmap /&gt;")
                html.H3(
                    classes="text-headline-medium font-weight-bold mt-6",
                    children="Data density is now a first-party primitive.",
                )
                html.P(
                    classes="text-body-large text-medium-emphasis mt-4",
                    children="Activity grids, utilization matrices, risk maps, deployment history, engagement charts — without reaching for another UI library.",
                )
                v4.VDivider()

            with html.Div(classes="stage-bg pa-8"):
                with html.Div(
                    classes="d-flex align-center justify-space-between ga-4 mb-6"
                ):
                    with html.Div():
                        html.Strong(
                            classes="text-title-medium font-weight-bold",
                            children="Deploy activity",
                        )
                        html.Span(
                            classes="text-body-small text-medium-emphasis",
                            children="Last 12 weeks",
                        )

                    v4.VChip(
                        color="success",
                        size="small",
                        variant="tonal",
                        children="+18.4%",
                    )

                with html.Div(classes="overflow-auto pb-2"):
                    v4.VHeatmap(
                        items=("heatmap_items",),
                        rows=("week_rows",),
                        columns=("week_columns",),
                        thresholds=("heatmap_thresholds",),
                        cell_size=("cell_size",),
                        gap=5,
                        legend=("heatmap_legend",),
                        rounded="6",
                        hover=True,
                    )


class MonthPickerExample:
    def __init__(self, app: DemoApp) -> None:
        """MonthPicker."""
        self.state = app.state

        self.state.month_range = ["2026-09", "2026-12"]

    def build_ui(self) -> None:
        with v4.VCard(
            classes="overflow-hidden",
            rounded="xl",
            elevation="0",
            height="100%",
        ):
            with html.Div(classes="pa-8"):
                with html.Div(
                    classes="d-flex align-center ga-3 text-label-medium font-weight-bold"
                ):
                    html.Span(classes="text-primary", children="02")
                    html.Span(" &lt;VMonthPicker /&gt;")
                html.H3(
                    classes="text-headline-medium font-weight-bold mt-6",
                    children="Pick months, not fake dates.",
                )
                html.P(
                    classes="text-body-large text-medium-emphasis mt-4",
                    children="Billing periods, fiscal planning, reporting windows, and subscriptions finally get a purpose-built selector.",
                )
                # TODO: This uses computed
                # v4.VChip(classes="mt-6",  variant="outlined", size="small"< children="{{ formatted_month_range }}")

            v4.VDivider()
            with html.Div(classes="stage-bg pa-6 d-flex justify-center"):
                v4.VMonthPicker(
                    v_model=("month_range",),
                    multiple="range",
                    color="primary",
                    months_columns=3,
                    hide_header=True,
                )


class Hero:
    def __init__(self, app: DemoApp) -> None:
        """Hero."""
        self.state = app.state

    def build_ui(self) -> None:
        with html.Section(classes="py-16"):
            with html.Div(classes="d-flex align-center ga-3 mb-8"):
                v4.VChip(
                    color="primary",
                    variant="tonal",
                    size="small",
                    children="Vuetify 4.2.1",
                )
                html.Span(
                    classes="text-label-small text-medium-emphasis text-uppercase",
                    children="Migration propaganda",
                )

            with html.Div(classes="text-display-large font-weight-bold"):
                html.Span("Your Vuetify 3 app")
                html.Span(classes="text-medium-emphasis", children=" works. ")
                html.Br()
                html.Span("Vuetify 4 gives it")
                html.Span(classes="text-primary", children=" new tricks. ")

            html.P(
                classes="text-body-large text-medium-emphasis mt-8 mb-0",
                children=(
                    "Five genuinely new component families, seven former Labs"
                    " components promoted into core, and framework-level"
                    " improvements that make the migration about more than"
                    " changing a version number."
                ),
            )

            with html.Div(classes="d-flex flex-wrap align-center ga-3 mt-8"):
                v4.VBtn(
                    color="primary",
                    size="large",
                    rounded="lg",
                    elevation="0",
                    href="#new-components",
                    append_icon="mdi-arrow-down",
                    children="Show me the new stuff",
                )
                v4.VChip(
                    color="primary",
                    variant="tonal",
                    size="large",
                    children="v3.13 → v4.2",
                )

            v4.VDivider(classes="mt-16 mb-8")

            with v4.VRow():
                with v4.VCol(cols="12", md="4"):
                    html.Div(
                        classes="text-headline-large font-weight-bold",
                        children="5",
                    )
                    html.Div(
                        classes="text-body-medium text-medium-emphasis mt-2",
                        children="v4-only component families",
                    )

                with v4.VCol(cols="12", md="4"):
                    html.Div(
                        classes="text-headline-large font-weight-bold",
                        children="7",
                    )
                    html.Div(
                        classes="text-body-medium text-medium-emphasis mt-2",
                        children="Labs APIs promoted to core",
                    )

                with v4.VCol(cols="12", md="4"):
                    html.Div(
                        classes="text-headline-large font-weight-bold",
                        children="1",
                    )
                    html.Div(
                        classes="text-body-medium text-medium-emphasis mt-2",
                        children="good excuse to delete old glue code",
                    )


if __name__ == "__main__":
    app = DemoApp()
    app.server.start()
