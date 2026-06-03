import reflex as rx
from govihara_.states.reviews_state import ReviewsState, Review


def render_star(idx: rx.Var[int], rating: rx.Var[int]) -> rx.Component:
    return rx.icon(
        "star",
        class_name=rx.cond(
            idx <= rating,
            "h-3.5 w-3.5 text-orange-400 fill-orange-400",
            "h-3.5 w-3.5 text-gray-300",
        ),
    )


def top_review_card(review: rx.Var[Review]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=review["avatar"],
                class_name="w-10 h-10 rounded-full bg-gray-100 flex-shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    review["username"],
                    class_name="font-bold text-gray-900 text-sm",
                ),
                rx.el.div(
                    rx.foreach(
                        [1, 2, 3, 4, 5],
                        lambda i: render_star(i, review["rating"]),
                    ),
                    rx.el.span(
                        review["visit_date"],
                        class_name="text-xs text-gray-500 ml-2",
                    ),
                    class_name="flex items-center gap-0.5",
                ),
                class_name="flex-1",
            ),
            class_name="flex items-start gap-3 mb-3",
        ),
        rx.el.h4(
            review["title"],
            class_name="font-bold text-gray-900 mb-1.5",
        ),
        rx.el.p(
            review["content"],
            class_name="text-sm text-gray-600 line-clamp-3 mb-3",
        ),
        rx.el.button(
            rx.icon("thumbs-up", class_name="h-3.5 w-3.5 mr-1.5"),
            rx.el.span(
                "Helpful (",
                review["helpful"].to_string(),
                ")",
                class_name="text-xs font-semibold",
            ),
            on_click=ReviewsState.mark_helpful(review["id"]),
            type="button",
            class_name="flex items-center text-gray-600 hover:text-teal-600 transition-colors",
        ),
        class_name="bg-white rounded-2xl p-5 border border-gray-100 hover:shadow-lg transition-all",
    )


def top_reviews_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Traveler Reviews",
                    class_name="text-3xl font-extrabold text-gray-900",
                ),
                rx.cond(
                    ReviewsState.review_count_for_current > 0,
                    rx.el.div(
                        rx.icon(
                            "star",
                            class_name="h-5 w-5 text-orange-400 fill-orange-400 mr-1",
                        ),
                        rx.el.span(
                            ReviewsState.average_rating_for_current.to_string(),
                            class_name="text-lg font-extrabold text-gray-900",
                        ),
                        rx.el.span(
                            " · ",
                            ReviewsState.review_count_for_current.to_string(),
                            " reviews",
                            class_name="text-sm text-gray-600 ml-1",
                        ),
                        class_name="flex items-center mt-1",
                    ),
                    rx.fragment(),
                ),
            ),
            rx.el.a(
                "All Reviews",
                rx.icon("arrow-right", class_name="h-4 w-4 ml-1"),
                href="/community",
                class_name="hidden md:flex items-center text-blue-700 hover:text-blue-900 font-semibold text-sm",
            ),
            class_name="flex items-end justify-between mb-5",
        ),
        rx.cond(
            ReviewsState.top_reviews_for_current.length() > 0,
            rx.el.div(
                rx.foreach(
                    ReviewsState.top_reviews_for_current,
                    top_review_card,
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-5",
            ),
            rx.el.div(
                rx.icon(
                    "message-square",
                    class_name="h-12 w-12 text-gray-300 mx-auto mb-2",
                ),
                rx.el.p(
                    "Be the first to share your experience.",
                    class_name="text-gray-500",
                ),
                rx.el.a(
                    "Write a review",
                    href="/community",
                    class_name="inline-block mt-3 text-blue-700 font-semibold hover:text-blue-900",
                ),
                class_name="text-center py-12 bg-white rounded-2xl border border-gray-100",
            ),
        ),
    )