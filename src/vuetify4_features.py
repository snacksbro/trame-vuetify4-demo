"""Demo to show off some of the new features present in Vuetify v4.

These are all lab components for now, but notably they aren't available in v3 or v3 lab.
"""

from __future__ import annotations

from typing import cast

from trame.app import get_server
from trame.decorators import TrameApp
from trame.ui.vuetify4 import SinglePageLayout
from trame.widgets import html
from trame.widgets import vuetify4 as v4
from trame_server import Server

# Note: The components in this example are exclusive to v4 labs, to ensure they're available:
v4.enable_lab()


@TrameApp()
class Vuetify4FeaturesExample:
    """Mini Trame app."""

    def __init__(self) -> None:
        self.server = cast("Server", get_server(None))
        self.state = self.server.state

        self.progress_example = ProgressExample(app=self)
        self.highlight_example = HighlightExample(app=self)
        self.date_range_picker_example = DateRangePickerExample(app=self)
        self.heatmap_example = HeatmapExample(app=self)
        self.month_picker_example = MonthPickerExample(app=self)
        self.graduated_components = GraduatedLabsSection(app=self)
        self.hero = Hero(app=self)
        self.build_ui()

    def build_ui(self) -> None:
        with SinglePageLayout(self.server) as layout, layout.content:  # noqa: SIM117
            with v4.VSheet(color="background", classes="showcase-bg min-h-screen"):
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
                            v4.VChip(
                                color="warning", variant="tonal", children="Labs APIs"
                            )
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
                    with html.Section(classes="mt-16 pt-16"):
                        self.graduated_components.build_ui()


class ProgressExample:
    def __init__(self, app: Vuetify4FeaturesExample) -> None:
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


class HighlightExample:
    def __init__(self, app: Vuetify4FeaturesExample) -> None:
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
    def __init__(self, app: Vuetify4FeaturesExample) -> None:
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
                    v4.VChip(
                        classes="mt-6",
                        variant="outlined",
                        size="small",
                        children=(
                            (
                                "{{ date_range.length < 2 ? 'Select a range' : "
                                "`${date_range[0].toLocaleDateString("
                                "'en-US', { year: 'numeric', month: 'short', day: 'numeric', }) } → "
                                "${date_range.at(-1).toLocaleDateString("
                                "'en-US', { year: 'numeric', month: 'short', day: 'numeric', }) }` }}"
                            ),
                        ),
                    )

                    v4.VSwitch(
                        v_model=("independent_months",),
                        color="primary",
                        label="Independent months",
                        hide_details=True,
                        classes="mt-4",
                    )

                with v4.VCol(
                    classes="stage-bg border-s-lg pa-6 overflow-auto flex-grow-1",
                    cols=12,
                    lg=4,
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
                            width="100%",
                        )


class HeatmapExample:
    def __init__(self, app: Vuetify4FeaturesExample) -> None:
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
                        classes="w-66",
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
    def __init__(self, app: Vuetify4FeaturesExample) -> None:
        """MonthPicker."""
        self.state = app.state

        self.state.month_range = ["2026-09", "2026-12"]

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


class GraduatedLabsSection:
    def __init__(self, app: Vuetify4FeaturesExample) -> None:
        """Components that are no-longer in labs as of V4."""

        self.state = app.state
        self.state.graduated_components = [
            {
                "name": "VColorInput",
                "value": "Structured color input without hand-rolling picker + field glue.",
            },
            {
                "name": "VDateInput",
                "value": "Date entry graduated from experimental API to normal core usage.",
            },
            {
                "name": "VFileUpload",
                "value": "A real upload surface instead of styling a file input yourself.",
            },
            {
                "name": "VIconBtn",
                "value": "Purpose-built icon buttons with consistent Vuetify behavior.",
            },
            {
                "name": "VPicker",
                "value": "Reusable picker infrastructure is now part of the core surface.",
            },
            {
                "name": "VPullToRefresh",
                "value": "Mobile refresh interactions without maintaining custom gestures.",
            },
            {
                "name": "VStepperVertical",
                "value": "Vertical workflows are now a first-class core component.",
            },
        ]

    def build_ui(self) -> None:
        with html.Div(
            classes="d-flex flex-column flex-sm-row align-sm-end justify-space-between ga-4 mb-4"
        ):
            with html.Div():
                html.Div(
                    classes="text-label-small text-success text-uppercase font-weight-bold mb-3",
                    children="Out of the lab",
                )
                html.H2(
                    classes="text-display-small font-weight-bold",
                    children="Experimental yesterday. Core today.",
                )

            v4.VChip(
                color="success",
                variant="tonal",
                children="Stable surface",
            )

        html.P(
            classes="text-body-large text-medium-emphasis mb-10",
            children=(
                "These existed in v3 as Labs components, so they aren't "
                "technically v4-only. The upgrade still matters: v4 promotes "
                "them into the normal component package."
            ),
        )

        with v4.VRow():  # noqa: SIM117
            with v4.VCol(
                v_for=("component in graduated_components"),
                key=("component", "name"),
                cols="12",
                md="6",
            ):
                with v4.VSheet(
                    border=True,
                    rounded="xl",
                    color="surface",
                    classes="pa-6 h-100",
                ):
                    with html.Div(classes="d-flex align-start ga-4"):
                        with v4.VSheet(
                            color="success",
                            rounded="lg",
                            width="36",
                            height="36",
                            classes="d-flex align-center justify-center flex-shrink-0",
                        ):
                            v4.VIcon(icon="mdi-check", size="small")

                        with html.Div():
                            html.Code(
                                classes="text-title-medium",
                                children="{{ component.name }}",
                            )
                            html.P(
                                classes="text-body-medium text-medium-emphasis mt-2 mb-0",
                                children="{{ component.value }}",
                            )


class Hero:
    def __init__(self, app: Vuetify4FeaturesExample) -> None:
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
    app = Vuetify4FeaturesExample()
    app.server.start()
