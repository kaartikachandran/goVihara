import reflex as rx
from govihara_.states.attractions_state import AttractionsState, Attraction


def attraction_card(attr: rx.Var[Attraction]) -> rx.Component:
    is_saved = AttractionsState.saved_ids.contains(attr["id"])
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=attr["image"],
                class_name="w-full h-44 object-cover group-hover:scale-110 transition-transform duration-700",
                custom_attrs={
                    "onError": "this.onerror=null;this.src='/placeholder.svg';"
                },
            ),
            rx.el.div(
                rx.el.span(
                    attr["category"],
                    class_name="bg-white/90 backdrop-blur-md text-blue-800 text-xs font-bold px-3 py-1 rounded-full",
                ),
                class_name="absolute top-3 left-3",
            ),
            rx.el.div(
                rx.icon("map-pin", class_name="h-3 w-3 text-white"),
                rx.el.span(
                    attr["distance"],
                    class_name="text-xs font-bold text-white ml-1",
                ),
                class_name="absolute top-3 right-3 flex items-center bg-blue-700/90 backdrop-blur-md px-2.5 py-1 rounded-full",
            ),
            class_name="relative overflow-hidden rounded-t-2xl",
        ),
        rx.el.div(
            rx.el.h4(
                attr["name"],
                class_name="text-lg font-extrabold text-gray-900 mb-1",
            ),
            rx.el.p(
                attr["description"],
                class_name="text-sm text-gray-600 line-clamp-2 mb-4",
            ),
            rx.el.button(
                rx.cond(
                    is_saved,
                    rx.el.div(
                        rx.icon("circle_check", class_name="h-4 w-4 mr-1.5"),
                        "Added to itinerary",
                        class_name="flex items-center justify-center",
                    ),
                    rx.el.div(
                        rx.icon("plus", class_name="h-4 w-4 mr-1.5"),
                        "Add to itinerary",
                        class_name="flex items-center justify-center",
                    ),
                ),
                on_click=AttractionsState.add_to_itinerary(
                    attr["id"], attr["dest_id"]
                ),
                type="button",
                disabled=is_saved,
                class_name=rx.cond(
                    is_saved,
                    "w-full bg-teal-50 text-teal-700 font-semibold py-2.5 rounded-xl border border-teal-200 cursor-default",
                    "w-full bg-gradient-to-r from-blue-700 to-teal-500 text-white font-semibold py-2.5 rounded-xl hover:shadow-lg hover:scale-[1.02] transition-all",
                ),
            ),
            class_name="p-5",
        ),
        class_name="bg-white rounded-2xl overflow-hidden border border-gray-100 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group",
    )