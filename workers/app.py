from worker import Worker
from handlers import demo_handler, reporte_handler

print('Init workers')
Worker('reporte', reporte_handler.handler)
Worker('demo', demo_handler.handler)
