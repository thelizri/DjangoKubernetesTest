import multiprocessing
import time
import random
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locustfile import WebsiteUser


def run_locust_instance(
    max_users,
    duration,
    users_per_second,
    start_timer=0,
    host_url="http://william.discworld.cc/",
    web_port=8089,
):
    print(
        f"Process starting with {max_users} users for {duration} seconds at {users_per_second} users/s after {start_timer} seconds delay, Web UI on port {web_port}."
    )
    time.sleep(start_timer)

    # Setup Environment and Runner
    env = Environment(user_classes=[WebsiteUser], host=host_url)
    env.create_local_runner()

    # Start Web UI
    env.create_web_ui("127.0.0.1", web_port)

    # Start the test
    env.runner.start(user_count=max_users, spawn_rate=users_per_second)
    time.sleep(duration)

    # Stop the test
    env.runner.quit()

    # Stop Web UI
    env.web_ui.stop()

    print(f"Process completed for {max_users} users.")


if __name__ == "__main__":
    processes = []
    start_port = 8089  # Initial port for Web UI
    configurations = [
        (5_000, 60, 70, 0, "http://william.discworld.cc/", start_port),
        (1_000, 120, 100, 30, "http://william.discworld.cc/", start_port + 1),
        (
            5_000,
            random.randint(30, 60),
            100,
            60,
            "http://william.discworld.cc/",
            start_port + 2,
        ),
    ]

    for config in configurations:
        p = multiprocessing.Process(target=run_locust_instance, args=config)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All simulations completed.")
