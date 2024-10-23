from fastapi.testclient import TestClient
from app.core.calculator import RPNCalculator
from app.main import app

client = TestClient(app)

def test_local_rpn_calculator():
    """
    Test RPNCalculator directly with valid and invalid operations.
    """
    calculator = RPNCalculator()

    # Test addition
    result = calculator.evaluate(["3", "4", "+"])
    assert result["result"] == 7

    # Test division by zero
    result = calculator.evaluate(["4", "0", "/"])
    assert "error" in result and result["error"] == "Division by zero"

    # Test invalid operation
    result = calculator.evaluate(["4", "+"])
    assert "error" in result

def test_calculate():
    """
    Test /calculate/ API with a valid RPN expression.
    """
    response = client.post("/calculate/", json={"operation": ["3", "4", "+", "2", "*"]})
    assert response.status_code == 200
    assert response.json() == {"result": 14}

def test_calculate_division_by_zero():
    """
    Test /calculate/ API with a division by zero operation.
    """
    response = client.post("/calculate/", json={"operation": ["4", "0", "/"]})
    assert response.status_code == 200
    assert "error" in response.json()
    assert response.json()["error"] == "Division by zero"
