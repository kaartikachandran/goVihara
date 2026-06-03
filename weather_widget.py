import reflex as rx
from govihara_.states.weather_state import WeatherState


def weather_card_destination() -> rx.Component:
    w = WeatherState.current_dest_weather
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("cloud-sun", class_name="h-6 w-6 text-white"),
                class_name="w-12 h-12 rounded-2xl bg-white/20 flex items-center justify-center backdrop-blur-md",
            ),
            rx.el.div(
                rx.el.p(
                    "Live Weather",
                    class_name="text-xs uppercase tracking-wider text-blue-100 font-bold",
                ),
                rx.el.p(
                    w["desc"],
                    class_name="text-lg font-bold text-white",
                ),
                class_name="ml-3",
            ),
            rx.cond(
                w["source"] == "live",
                rx.el.span(
                    "LIVE",
                    class_name="ml-auto text-[10px] bg-green-400 text-blue-900 font-extrabold px-2 py-0.5 rounded-full",
                ),
                rx.el.span(
                    "TYPICAL",
                    class_name="ml-auto text-[10px] bg-orange-300 text-blue-900 font-extrabold px-2 py-0.5 rounded-full",
                ),
            ),
            class_name="flex items-center mb-5",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    w["temp"],
                    class_name="text-5xl font-extrabold text-white",
                ),
                rx.el.p(
                    "Feels like " + w["feels"],
                    class_name="text-sm text-blue-100",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "droplets", class_name="h-4 w-4 text-blue-100 mr-1"
                    ),
                    rx.el.span(
                        w["humidity"],
                        class_name="text-sm text-white font-semibold",
                    ),
                    class_name="flex items-center mb-2",
                ),
                rx.el.div(
                    rx.icon("wind", class_name="h-4 w-4 text-blue-100 mr-1"),
                    rx.el.span(
                        w["wind"], class_name="text-sm text-white font-semibold"
                    ),
                    class_name="flex items-center",
                ),
            ),
            class_name="flex items-end justify-between",
        ),
        on_mount=WeatherState.load_for_current_destination,
        class_name="bg-gradient-to-br from-blue-700 via-blue-600 to-teal-500 rounded-3xl p-6 border border-white/10 shadow-xl",
    )


def weather_summary_card(card: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(card["icon"], class_name="h-8 w-8 text-white"),
            class_name="w-14 h-14 rounded-2xl bg-white/20 backdrop-blur-md flex items-center justify-center mb-3",
        ),
        rx.el.p(
            card["name"],
            class_name="text-lg font-extrabold text-white",
        ),
        rx.el.p(
            card["state"],
            class_name="text-xs text-blue-100 mb-3",
        ),
        rx.el.div(
            rx.el.p(
                card["temp"],
                class_name="text-3xl font-extrabold text-white",
            ),
            rx.el.p(
                card["desc"],
                class_name="text-xs text-blue-100",
            ),
            class_name="",
        ),
        class_name="bg-gradient-to-br from-blue-700 to-teal-500 rounded-2xl p-5 border border-white/10",
    )


def weather_dashboard_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Weather Across India",
                    class_name="text-2xl font-extrabold text-gray-900",
                ),
                rx.el.p(
                    "Live conditions at top destinations.",
                    class_name="text-sm text-gray-600",
                ),
            ),
            rx.el.div(
                rx.el.span(
                    "via Open-Meteo",
                    class_name="text-xs text-gray-500 font-medium",
                ),
                class_name="hidden md:block",
            ),
            class_name="flex items-end justify-between mb-5",
        ),
        rx.el.div(
            rx.foreach(
                WeatherState.dashboard_weather_cards, weather_summary_card
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-4",
        ),
        on_mount=WeatherState.load_dashboard_summary,
    )