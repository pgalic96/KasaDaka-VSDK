def process_orders(orders):
    orders_new = []
    orders_in_progress = []
    orders_done = []
    for order in orders:
        order.pickup_address = f'{order.farmer.street} {order.farmer.house_nr} ' \
            f'{order.farmer.house_nr_extension}, {order.farmer.zipcode}' if order.farmer else ''

        if order.arrival_time is None and order.driver is None:
            orders_new.append(order.to_dict())
        elif order.arrival_time is None and order.driver is not None:
            orders_in_progress.append(order.to_dict())
        elif order.arrival_time is not None:
            orders_done.append(order)

    return {
        'orders_new': orders_new,
        'orders_in_progress': orders_in_progress,
        'orders_done': orders_done
    }


def process_drivers(drivers):
    available_drivers = []
    for driver in drivers:
        available_drivers.append(driver.to_dict())
    return available_drivers
