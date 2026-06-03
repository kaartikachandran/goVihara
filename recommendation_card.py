import reflex as rx


def recommendation_card(rec: rx.Var) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src=rec["image"],
                    class_name="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-700",
                    custom_attrs={
                        "onError": "this.onerror=null;this.src='/placeholder.svg';"
                    },
                ),
                rx.el.div(
                    rx.el.span(
                        rec["category"],
                        class_name="bg-white/90 backdrop-blur-md text-blue-800 text-xs font-bold px-3 py-1 rounded-full",
                    ),
                    class_name="absolute top-3 left-3",
                ),
                rx.el.div(
                    rx.icon(
                        "sparkles",
                        class_name="h-3.5 w-3.5 text-orange-500",
                    ),
                    rx.el.span(
                        "For You",
                        class_name="text-[10px] font-bold text-blue-900 ml-1",
                    ),
                    class_name="absolute top-3 right-3 flex items-center bg-white/90 backdrop-blur-md px-2.5 py-1 rounded-full",
                ),
                class_name="relative overflow-hidden",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            rec["name"],
                            class_name="text-lg font-extrabold text-gray-900",
                        ),
                        rx.el.div(
                            rx.icon(
                                "map-pin",
                                class_name="h-3.5 w-3.5 text-teal-600",
                            ),
                            rx.el.span(
                                rec["state"],
                                class_name="text-xs text-gray-600 font-medium",
                            ),
                            class_name="flex items-center gap-1 mt-0.5",
                        ),
                    ),
                    rx.el.div(
                        rx.icon(
                            "star",
                            class_name="h-3.5 w-3.5 text-orange-400 fill-orange-400",
                        ),
                        rx.el.span(
                            rec["rating"].to_string(),
                            class_name="text-xs font-bold text-gray-700",
                        ),
                        class_name="flex items-center gap-0.5",
                    ),
                    class_name="flex justify-between items-start mb-2",
                ),
                rx.el.p(
                    rec["description"],
                    class_name="text-xs text-gray-600 line-clamp-2 mb-3",
                ),
                rx.el.div(
                    rx.icon(
                        "wand-sparkles",
                        class_name="h-3 w-3 text-orange-500 flex-shrink-0",
                    ),
                    rx.el.span(
                        rec["reason"],
                        class_name="text-[11px] font-semibold text-orange-700",
                    ),
                    class_name="flex items-center gap-1.5 bg-orange-50 px-2.5 py-1.5 rounded-full",
                ),
                class_name="p-4",
            ),
            class_name="bg-white/90 backdrop-blur-md rounded-2xl overflow-hidden border border-gray-100 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 group cursor-pointer h-full",
        ),
        href=f"/explore?cat={rec['category']}",
        class_name="block h-full",
    )


def recommendations_section(
    title: str, subtitle: str, recs: rx.Var, icon: str = "wand-sparkles"
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name="h-5 w-5 text-orange-500"),
                rx.el.span(
                    "Recommended For You",
                    class_name="text-sm font-semibold text-orange-700",
                ),
                class_name="inline-flex items-center gap-2 bg-orange-50 px-4 py-1.5 rounded-full mb-3",
            ),
            rx.el.h2(
                title, class_name="text-3xl font-extrabold text-gray-900 mb-1"
            ),
            rx.el.p(subtitle, class_name="text-gray-600"),
            class_name="mb-6",
        ),
        rx.cond(
            recs.length() > 0,
            rx.el.div(
                rx.foreach(recs, recommendation_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
            rx.el.div(
                rx.icon(
                    "wand-sparkles",
                    class_name="h-12 w-12 text-gray-300 mx-auto mb-2",
                ),
                rx.el.p(
                    "Save a few favorites and we'll personalize this for you.",
                    class_name="text-gray-500",
                ),
                class_name="text-center py-12 bg-white/50 rounded-2xl border border-gray-100",
            ),
        ),
    )