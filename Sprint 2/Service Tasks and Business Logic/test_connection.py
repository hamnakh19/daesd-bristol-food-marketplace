
from camunda_orchestration_sdk import CamundaClient

try:
    with CamundaClient(
        configuration={"CAMUNDA_LOAD_ENVFILE": "true"}
    ) as client:
        client.get_topology()

    print("SUCCESS: Connected to Camunda!")

except Exception as error:
    print("Connection failed.")
    print("Error type:", type(error).__name__)
    print("Error:", str(error))
