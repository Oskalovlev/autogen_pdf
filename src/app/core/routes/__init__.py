from src.app.core.routes.routes import Routes
from src.app.internal.routes import report, uploading

__routes__ = Routes(routers=(uploading.router, report.router))
