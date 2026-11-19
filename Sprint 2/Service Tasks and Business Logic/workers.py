import asyncio

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)

from validateProduct import validate_product
from publishProduct import publish_product
from verify_certification import verify_certification
from pending_verification import mark_pending_verification
from inventory_management import update_availability


# Product listing workers

async def handle_validation(job: ConnectedJobContext):
    result = validate_product(job.variables.to_dict())
    print("Product validation:", result)
    return result


async def handle_certification(job: ConnectedJobContext):
    result = verify_certification(job.variables.to_dict())
    print("Certification result:", result)
    return result


async def handle_pending(job: ConnectedJobContext):
    result = mark_pending_verification(job.variables.to_dict())
    print("Pending verification:", result)
    return result


async def handle_publication(job: ConnectedJobContext):
    result = publish_product(job.variables.to_dict())

    if result["listingStatus"] != "PUBLISHED":
        raise ValueError("Product cannot be published")

    print("Publication:", result)
    return result


# Inventory management workers

async def handle_inventory_validation(job: ConnectedJobContext):
    result = update_availability(job.variables.to_dict())
    print("Inventory validation:", result)
    return result


async def handle_inventory_save(job: ConnectedJobContext):
    product = job.variables.to_dict()

    if not update_availability(product)["inventoryValid"]:
        raise ValueError("Invalid inventory update")

    # Initial implementation: process variables only
    result = {
        "stockQuantity": product["stockQuantity"]
    }

    print("Inventory process variables updated:", result)
    return result


async def handle_available(job: ConnectedJobContext):
    result = {
        "availabilityStatus": "AVAILABLE",
        "isAvailable": True
    }
    print("Product available:", result)
    return result


async def handle_unavailable(job: ConnectedJobContext):
    result = update_availability(job.variables.to_dict())
    result["isAvailable"] = False

    print("Product unavailable:", result)
    return result


# Worker registration

async def main():

    workers = {
    "brfn31-validate-product": handle_validation,
    "brfn31-verify-organic-certification": handle_certification,
    "brfn31-set-listing-pending": handle_pending,
    "brfn31-publish-product": handle_publication,
    "brfn31-validate-inventory-update": handle_inventory_validation,
    "brfn31-save-inventory-update": handle_inventory_save,
    "brfn31-set-product-available": handle_available,
    "brfn31-set-product-unavailable": handle_unavailable
}

    async with CamundaAsyncClient(
        configuration={"CAMUNDA_LOAD_ENVFILE": "true"}
    ) as client:

        for job_type, handler in workers.items():

            client.create_job_worker(
                config=WorkerConfig(
                    job_type=job_type,
                    job_timeout_milliseconds=30000
                ),
                callback=handler
            )

            print("Worker registered:", job_type)

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())