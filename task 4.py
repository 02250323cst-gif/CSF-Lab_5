service_queue = ["Sonam", "Pema", "Karma"]
print(f"Customers waiting: {service_queue}")

serving = service_queue.pop(0)
print(f"Serving customer: {serving}")

print(f"Remaining queue: {service_queue}")