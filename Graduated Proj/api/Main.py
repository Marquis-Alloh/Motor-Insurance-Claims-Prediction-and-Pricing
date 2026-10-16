from flask import Flask, request, jsonify
from pydantic import BaseModel, Field, ValidationError

app = Flask(__name__)


# Define the request schema
class PolicyInput(BaseModel):
    DrivAge: int = Field(ge=18)
    VehAge: int = Field(ge=0)
    BonusMalus: int
    Exposure: float = Field(gt=0)

@app.post("/predict")
def predict():
    # 1. Read the incoming JSON
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(error="Expected a JSON object"), 400

    # 2. Validate it against the schema
    try:
        policy = PolicyInput.model_validate(data)
    except ValidationError as exc:
        return jsonify(
            error="Invalid policy data",
            details=exc.errors()
        ), 400

    # 3. Validated data is available to your model
    policy_data = policy.model_dump()

    # Replace this with your actual prediction logic
    return jsonify(
        message="Input validated successfully",
        received_policy=policy_data
    )