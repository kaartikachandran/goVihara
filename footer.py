import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("compass", class_name="h-7 w-7 text-blue-300"),
                        rx.el.span(
                            "go",
                            class_name="text-2xl font-extrabold text-white",
                        ),
                        rx.el.span(
                            "Vihara",
                            class_name="text-2xl font-extrabold text-orange-400",
                        ),
                        class_name="flex items-center gap-1 mb-4",
                    ),
                    rx.el.p(
                        "Discover incredible India — curated journeys, hidden gems, and unforgettable experiences.",
                        class_name="text-blue-100 text-sm leading-relaxed",
                    ),
                    class_name="md:col-span-2",
                ),
                rx.el.div(
                    rx.el.h4("Explore", class_name="font-bold text-white mb-3"),
                    rx.el.a(
                        "Home",
                        href="/",
                        class_name="block text-blue-200 hover:text-white py-1 text-sm",
                    ),
                    rx.el.a(
                        "Destinations",
                        href="/explore",
                        class_name="block text-blue-200 hover:text-white py-1 text-sm",
                    ),
                    rx.el.a(
                        "Heritage",
                        href="/explore",
                        class_name="block text-blue-200 hover:text-white py-1 text-sm",
                    ),
                    rx.el.a(
                        "Hill Stations",
                        href="/explore",
                        class_name="block text-blue-200 hover:text-white py-1 text-sm",
                    ),
                ),
                rx.el.div(
                    rx.el.h4("Connect", class_name="font-bold text-white mb-3"),
                    rx.el.div(
                        rx.icon(
                            "inbox",
                            class_name="h-5 w-5 text-blue-200 hover:text-white cursor-pointer",
                        ),
                        rx.icon(
                            "wifi",
                            class_name="h-5 w-5 text-blue-200 hover:text-white cursor-pointer",
                        ),
                        rx.icon(
                            "wifi",
                            class_name="h-5 w-5 text-blue-200 hover:text-white cursor-pointer",
                        ),
                        rx.icon(
                            "video",
                            class_name="h-5 w-5 text-blue-200 hover:text-white cursor-pointer",
                        ),
                        class_name="flex gap-4 mt-2",
                    ),
                ),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-8",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2025 goVihara. Crafted with ❤ for travelers.",
                    class_name="text-blue-200 text-sm text-center",
                ),
                class_name="border-t border-blue-800 mt-10 pt-6",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="bg-gradient-to-br from-blue-900 to-blue-950 mt-20",
    )