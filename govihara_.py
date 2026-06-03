import reflex as rx
import reflex_enterprise as rxe
from govihara_.pages.landing import landing_page
from govihara_.pages.explore import explore_page
from govihara_.pages.destination_detail import detail_page
from govihara_.pages.planner import planner_page
from govihara_.pages.map import map_page
from govihara_.pages.dashboard import dashboard_page
from govihara_.pages.community import community_page
from govihara_.pages.about import about_page
from govihara_.pages.login import login_page
from govihara_.pages.signup import signup_page
from govihara_.pages.admin import admin_page
from govihara_.pages.deployment import deployment_page
from govihara_.pages.analytics import analytics_page


def index() -> rx.Component:
    return landing_page()


app = rxe.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(
            rel="stylesheet",
            href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
            integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=",
            cross_origin="",
        ),
    ],
)
app.add_page(detail_page, route="/destination/[dest_id]")
app.add_page(explore_page, route="/explore")
app.add_page(planner_page, route="/planner")
app.add_page(map_page, route="/map")
app.add_page(dashboard_page, route="/dashboard")
app.add_page(community_page, route="/community")
app.add_page(about_page, route="/about")
app.add_page(login_page, route="/login")
app.add_page(signup_page, route="/signup")
app.add_page(admin_page, route="/admin")
app.add_page(deployment_page, route="/deployment")
app.add_page(analytics_page, route="/analytics")
app.add_page(index, route="/")