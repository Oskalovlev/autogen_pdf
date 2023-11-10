from src.app.core.routes.routes import Routes
from src.app.internal.routes import report

__routes__ = Routes(routers=(report.router,))
