from celery import shared_task


@shared_task
def demo_add(x, y):
    return x + y
