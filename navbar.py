import reflex as rx
from govihara_.states.destinations_state import DestinationsState
from govihara_.states.auth_state import AuthState


def nav_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        label,
        href=href,
        class_name="text-gray-700 hover:text-blue-700 font-medium transition-colors px-3 py-2",
    )


def auth_controls() -> rx.Component:
    return rx.cond(
        AuthState.is_authenticated,
        rx.el.div(
            rx.cond(
                AuthState.is_admin,
                rx.el.a(
                    rx.icon("shield-check", class_name="h-4 w-4 mr-1"),
                    "Admin",
                    href="/admin",
                    class_name="hidden md:flex items-center text-purple-700 hover:text-purple-900 font-semibold px-3 py-2 text-sm",
                ),
                rx.fragment(),
            ),
            rx.el.div(
                rx.el.img(
                    src=f"https://api.dicebear.com/9.x/notionists/svg?seed={AuthState.user_email}",
                    class_name="h-8 w-8 rounded-full bg-gray-100",
                ),
                rx.el.span(
                    AuthState.display_name,
                    class_name="hidden md:inline ml-2 font-semibold text-gray-700 text-sm",
                ),
                class_name="flex items-center mr-2",
            ),
            rx.el.button(
                rx.icon("log-out", class_name="h-4 w-4"),
                rx.el.span(
                    "Sign out",
                    class_name="hidden md:inline ml-1 text-sm font-semibold",
                ),
                on_click=AuthState.logout,
                type="button",
                class_name="flex items-center text-gray-600 hover:text-red-600 px-3 py-2 transition-colors",
            ),
            class_name="flex items-center gap-1",
        ),
        rx.el.div(
            rx.el.a(
                "Log In",
                href="/login",
                class_name="hidden md:inline-block text-gray-700 hover:text-blue-700 font-semibold px-3 py-2 text-sm",
            ),
            rx.el.a(
                "Sign Up",
                href="/signup",
                class_name="bg-gradient-to-r from-blue-700 to-teal-500 text-white px-5 py-2.5 rounded-full font-semibold hover:shadow-lg transition-all text-sm",
            ),
            class_name="flex items-center gap-1",
        ),
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("compass", class_name="h-7 w-7 text-blue-700"),
                    rx.el.span(
                        "go",
                        class_name="text-2xl font-extrabold text-blue-900",
                    ),
                    rx.el.span(
                        "Vihara",
                        class_name="text-2xl font-extrabold text-orange-500",
                    ),
                    class_name="flex items-center gap-1",
                ),
                href="/",
                class_name="flex items-center",
            ),
            rx.el.div(
                nav_link("Explore", "/explore"),
                nav_link("Map", "/map"),
                nav_link("Planner", "/planner"),
                nav_link("Community", "/community"),
                nav_link("Dashboard", "/dashboard"),
                nav_link("Analytics", "/analytics"),
                nav_link("Deploy", "/deployment"),
                nav_link("About", "/about"),
                rx.el.a(
                    rx.icon("heart", class_name="h-5 w-5"),
                    rx.el.span(
                        DestinationsState.favorite_count,
                        class_name="ml-1 text-sm font-semibold",
                    ),
                    href="/dashboard",
                    class_name="flex items-center text-orange-500 hover:text-orange-600 font-medium px-3 py-2",
                ),
                class_name="hidden lg:flex items-center gap-1",
            ),
            auth_controls(),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16 gap-2",
        ),
        class_name="bg-white/80 backdrop-blur-md border-b border-gray-100 sticky top-0 z-50 shadow-sm",
    )