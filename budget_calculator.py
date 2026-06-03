import reflex as rx
from govihara_.states.budget_state import BudgetState


TOOLTIP_PROPS = {
    "content_style": {
        "background": "white",
        "borderColor": "#E8E8E8",
        "borderRadius": "0.75rem",
        "fontFamily": "Inter, sans-serif",
        "fontSize": "0.875rem",
        "fontWeight": "500",
        "padding": "0.5rem 0.75rem",
    },
    "label_style": {"color": "#1e3a8a", "fontWeight": "700"},
    "separator": "",
}


def style_chip(label: str) -> rx.Component:
    is_active = BudgetState.style == label
    return rx.el.button(
        label,
        on_click=BudgetState.set_style(label),
        type="button",
        class_name=rx.cond(
            is_active,
            "px-4 py-2 rounded-full bg-gradient-to-r from-blue-700 to-teal-500 text-white font-semibold text-sm",
            "px-4 py-2 rounded-full bg-white text-gray-700 font-medium text-sm border border-gray-200 hover:border-blue-400",
        ),
    )


def cost_card(label: str, value: rx.Var, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-6 w-6 {color}"),
            class_name=f"w-12 h-12 rounded-2xl flex items-center justify-center mb-3 backdrop-blur-md {color.replace('text-', 'bg-').replace('-700', '-100').replace('-600', '-100')}",
        ),
        rx.el.p(
            label,
            class_name="text-xs uppercase tracking-wider text-gray-500 font-bold",
        ),
        rx.el.p(
            "₹" + value.to_string(),
            class_name="text-2xl font-extrabold text-gray-900 mt-1",
        ),
        class_name="bg-white/80 backdrop-blur-md rounded-2xl p-5 border border-gray-100",
    )


def breakdown_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Breakdown by Category",
            class_name="text-lg font-bold text-gray-900 mb-3",
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                horizontal=True, vertical=False, class_name="opacity-25"
            ),
            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
            rx.recharts.bar(
                data_key="amount",
                fill="#0d9488",
                radius=[8, 8, 0, 0],
                bar_size=50,
            ),
            rx.recharts.x_axis(
                data_key="category",
                axis_line=False,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            rx.recharts.y_axis(
                axis_line=False,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            data=BudgetState.breakdown_data,
            width="100%",
            height=280,
            margin={"left": 20, "right": 20, "top": 25, "bottom": 5},
        ),
        class_name="bg-white rounded-2xl p-6 border border-gray-100",
    )


def budget_calculator() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("calculator", class_name="h-4 w-4 text-orange-500"),
                rx.el.span(
                    "Smart Budget Calculator",
                    class_name="text-sm font-semibold text-blue-900",
                ),
                class_name="inline-flex items-center gap-2 bg-orange-50 px-4 py-2 rounded-full mb-3",
            ),
            rx.el.h2(
                "Estimate your trip cost",
                class_name="text-3xl font-extrabold text-gray-900 mb-2",
            ),
            rx.el.p(
                "Enter your trip details and get a realistic cost breakdown across stay, food, transit, and sights.",
                class_name="text-gray-600 mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Destination",
                        class_name="block text-sm font-bold text-gray-700 mb-2",
                    ),
                    rx.el.input(
                        placeholder="e.g. Goa",
                        default_value=BudgetState.destination,
                        on_change=BudgetState.set_destination.debounce(300),
                        class_name="w-full px-4 py-3 rounded-xl bg-gray-50 border border-gray-200 focus:border-blue-500 outline-none",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Days",
                        class_name="block text-sm font-bold text-gray-700 mb-2",
                    ),
                    rx.el.input(
                        type="number",
                        min="1",
                        default_value=BudgetState.days.to_string(),
                        on_change=BudgetState.set_days.debounce(300),
                        class_name="w-full px-4 py-3 rounded-xl bg-gray-50 border border-gray-200 focus:border-blue-500 outline-none",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Travelers",
                        class_name="block text-sm font-bold text-gray-700 mb-2",
                    ),
                    rx.el.input(
                        type="number",
                        min="1",
                        default_value=BudgetState.travelers.to_string(),
                        on_change=BudgetState.set_travelers.debounce(300),
                        class_name="w-full px-4 py-3 rounded-xl bg-gray-50 border border-gray-200 focus:border-blue-500 outline-none",
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mb-5",
            ),
            rx.el.div(
                rx.el.label(
                    "Travel Style",
                    class_name="block text-sm font-bold text-gray-700 mb-2",
                ),
                rx.el.div(
                    style_chip("Budget"),
                    style_chip("Standard"),
                    style_chip("Luxury"),
                    class_name="flex gap-2 flex-wrap",
                ),
                class_name="mb-6",
            ),
            rx.el.button(
                rx.icon("calculator", class_name="h-4 w-4 mr-2"),
                "Calculate Budget",
                on_click=BudgetState.calculate,
                type="button",
                class_name="flex items-center justify-center bg-gradient-to-r from-blue-700 to-teal-500 text-white px-6 py-3 rounded-xl font-bold hover:shadow-xl transition-all w-full md:w-auto",
            ),
            class_name="bg-white rounded-3xl p-7 border border-gray-100 mb-6",
        ),
        rx.cond(
            BudgetState.show_breakdown,
            rx.el.div(
                rx.el.div(
                    cost_card(
                        "Accommodation",
                        BudgetState.accommodation,
                        "bed-double",
                        "text-blue-700",
                    ),
                    cost_card(
                        "Food & Drinks",
                        BudgetState.food,
                        "utensils",
                        "text-orange-600",
                    ),
                    cost_card(
                        "Local Transport",
                        BudgetState.transport,
                        "car",
                        "text-teal-600",
                    ),
                    cost_card(
                        "Attractions",
                        BudgetState.attractions,
                        "ticket",
                        "text-purple-600",
                    ),
                    class_name="grid grid-cols-2 md:grid-cols-4 gap-4 mb-5",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Estimated Total",
                            class_name="text-sm text-blue-100 font-semibold uppercase tracking-wider",
                        ),
                        rx.el.p(
                            "₹" + BudgetState.total.to_string(),
                            class_name="text-5xl font-extrabold text-white",
                        ),
                        rx.el.p(
                            "for "
                            + BudgetState.travelers.to_string()
                            + " travelers · "
                            + BudgetState.days.to_string()
                            + " days · "
                            + BudgetState.style
                            + " style",
                            class_name="text-sm text-blue-100 mt-1",
                        ),
                    ),
                    rx.icon(
                        "wallet",
                        class_name="h-16 w-16 text-white/30",
                    ),
                    class_name="bg-gradient-to-br from-blue-700 to-teal-500 rounded-3xl p-7 mb-5 flex items-center justify-between",
                ),
                breakdown_chart(),
            ),
            rx.fragment(),
        ),
    )