import reflex as rx
from govihara_.states.destinations_state import DestinationsState, Destination


def rating_stars(rating: rx.Var[float]) -> rx.Component:
    return rx.el.div(
        rx.icon("star", class_name="h-4 w-4 text-orange-400 fill-orange-400"),
        rx.el.span(
            rating.to_string(), class_name="text-sm font-semibold text-gray-700"
        ),
        class_name="flex items-center gap-1",
    )


def destination_card(dest: rx.Var[Destination]) -> rx.Component:
    is_fav = DestinationsState.favorites.contains(dest["id"])
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src=dest["image"],
                    class_name="w-full h-56 object-cover group-hover:scale-110 transition-transform duration-700",
                    custom_attrs={
                        "onError": "this.onerror=null;this.src='/placeholder.svg';"
                    },
                ),
                rx.el.div(
                    rx.el.span(
                        dest["category"],
                        class_name="absolute top-3 left-3 bg-white/90 backdrop-blur-sm text-blue-800 text-xs font-bold px-3 py-1 rounded-full",
                    ),
                    rx.el.button(
                        rx.cond(
                            is_fav,
                            rx.icon(
                                "heart",
                                class_name="h-5 w-5 text-orange-500 fill-orange-500",
                            ),
                            rx.icon(
                                "heart", class_name="h-5 w-5 text-gray-700"
                            ),
                        ),
                        on_click=rx.cond(
                            False,
                            rx.event.stop_propagation,
                            DestinationsState.toggle_favorite(dest["id"]),
                        ),
                        type="button",
                        class_name="absolute top-3 right-3 bg-white/90 backdrop-blur-sm p-2 rounded-full hover:bg-white transition-all hover:scale-110",
                    ),
                ),
                class_name="relative overflow-hidden",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            dest["name"],
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        rx.el.div(
                            rx.icon(
                                "map-pin",
                                class_name="h-3.5 w-3.5 text-teal-600",
                            ),
                            rx.el.span(
                                dest["state"],
                                class_name="text-sm text-gray-600 font-medium",
                            ),
                            class_name="flex items-center gap-1 mt-1",
                        ),
                    ),
                    rating_stars(dest["rating"]),
                    class_name="flex justify-between items-start mb-3",
                ),
                rx.el.p(
                    dest["description"],
                    class_name="text-sm text-gray-600 line-clamp-2 mb-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("wallet", class_name="h-4 w-4 text-teal-600"),
                        rx.el.span(
                            dest["budget"],
                            class_name="text-xs font-semibold text-gray-700",
                        ),
                        class_name="flex items-center gap-1.5 bg-teal-50 px-3 py-1.5 rounded-full",
                    ),
                    rx.el.div(
                        "₹",
                        dest["budget_amount"].to_string(),
                        rx.el.span(
                            "/day",
                            class_name="text-xs font-normal text-gray-500",
                        ),
                        class_name="text-sm font-bold text-blue-800",
                    ),
                    class_name="flex items-center justify-between",
                ),
                class_name="p-5",
            ),
            class_name="bg-white rounded-2xl overflow-hidden border border-gray-100 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 group cursor-pointer",
        ),
        href=f"/destination/{dest['id']}",
        class_name="block",
    )