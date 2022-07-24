from worker import Worker
from handlers import demo_handler

Worker('demo', demo_handler.handler)
