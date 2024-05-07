import docker

def run_postgres_container():
    client = docker.from_env()

    print("Pulling PostgreSQL image...")
    client.images.pull("postgres:latest")

    print("Starting PostgreSQL container...")
    container = client.containers.run(
        "postgres:latest",
        name="my_postgres",
        detach=True,
        ports={"5432/tcp": 5432},
        environment={
            "POSTGRES_USER": "admin",
            "POSTGRES_PASSWORD": "Albionmc123?",
            "POSTGRES_DB": "AlbionMC"
        }
    )

    print("PostgreSQL container started successfully.")

if __name__ == "__main__":
    run_postgres_container()