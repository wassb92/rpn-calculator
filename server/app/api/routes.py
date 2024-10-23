import csv
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.database import Calculation
from app.models.operation import Operation
from app.core.calculator import RPNCalculator
from io import StringIO
from fastapi.responses import StreamingResponse

router = APIRouter()

calculator = RPNCalculator()

@router.post("/calculate/")
async def calculate(operation: Operation, db: AsyncSession = Depends(get_db)):
    """
    Perform RPN calculation, save expression and result in DB.
    """
    result = calculator.evaluate(operation.operation)

    if "result" in result:
        new_calc = Calculation(expression=" ".join(operation.operation), result=str(result["result"]))
        db.add(new_calc)
        await db.commit()
        await db.refresh(new_calc)

    return result


@router.get("/export-csv/")
async def export_csv(db: AsyncSession = Depends(get_db)):
    """
    Export calculations as CSV.
    """
    calculations = await db.execute(Calculation.__table__.select())
    calculations = calculations.fetchall()

    output = StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerow(["id", "expression", "result"])

    for calc in calculations:
        csv_writer.writerow([calc.id, calc.expression, calc.result])

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=calculations.csv"})
