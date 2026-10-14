import json
import logging
from datetime import datetime, timezone

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="adf_poc", methods=["GET", "POST"])
def adf_poc(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP trigger called from the ADF Azure Function activity.

    ADF requires the response body to be a JSON object (JObject).
    """
    logging.info("adf_poc triggered")
    try:
        body = req.get_json()
    except ValueError:
        body = {}

    name = req.params.get("name") or body.get("name") or "ADF"
    result = {
        "status": "Succeeded",
        "message": f"Hello {name}, from Python New v2 Azure Function",
        "received": body,
        "pipelineRunId": body.get("pipelineRunId"),
        "utcNow": datetime.now(timezone.utc).isoformat(),
    }
    return func.HttpResponse(json.dumps(result), status_code=200, mimetype="application/json")
