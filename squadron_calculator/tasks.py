from celery import shared_task


@shared_task(bind=True)
def count_a_lot(self):
    for i in range(10000):
        self.update_state(
            state='PROGRESS',
            meta={
                "number": f"{i}"
            }
        )
