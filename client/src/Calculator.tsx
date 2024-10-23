import React, { useState } from "react";
import axios from "axios";

interface Operation {
  operation: string[];
}

const Calculator: React.FC = () => {
  const [input, setInput] = useState<string[]>([]);

  const [currentNumber, setCurrentNumber] = useState<string>("");

  const [result, setResult] = useState<number | null>(null);

  const [error, setError] = useState<string>("");

  const handleNumberClick = (value: string) => {
    setCurrentNumber(currentNumber + value);
  };

  const handleSeparateClick = () => {
    if (currentNumber !== "") {
      setInput([...input, currentNumber]);
      setCurrentNumber("");
    }
  };

  const handleOperatorClick = (operator: string) => {
    if (currentNumber !== "") {
      setInput([...input, currentNumber, operator]);
      setCurrentNumber("");
    } else if (input.length > 0) {
      setInput([...input, operator]);
    }
  };

  const clearInput = () => {
    setInput([]);
    setCurrentNumber("");
    setResult(null);
    setError("");
  };

  const calculate = async () => {
    if (currentNumber !== "" || input.length > 0) {
      let operationArray = [...input];
      if (currentNumber !== "") {
        operationArray.push(currentNumber);
      }

      if (operationArray[operationArray.length - 1] === "") {
        operationArray.pop();
      }
      const operation: Operation = { operation: operationArray };
      try {
        const { data } = await axios.post(
          "http://localhost:8000/calculate",
          operation
        );

        if (data.error) {
          setError(data.error);
          setResult(null);
        } else {
          setResult(data.result);
          setError("");
        }
      } catch (err) {
        setError("Échec du calcul");
      }
    }
  };

  const downloadCSV = async () => {
    try {
      const response = await axios.get("http://localhost:8000/export-csv/", {
        responseType: "blob",
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "calculations.csv");
      document.body.appendChild(link);
      link.click();
    } catch (err) {
      setError("Failed to download CSV");
    }
  };

  return (
    <div className="min-h-screen bg-indigo-500 flex items-center justify-center">
      <div className="bg-white p-8 rounded shadow-lg w-full max-w-sm">
        <h1 className="text-2xl font-bold mb-4 text-center">
          Calculatrice NPI
        </h1>
        <div className="mb-4">
          <div className="bg-gray-200 p-4 rounded h-12 mb-2 flex items-center justify-end">
            {input.length > 0 || currentNumber !== ""
              ? `${input.join(" ")} ${currentNumber}`
              : "0"}
          </div>
          <div className="bg-gray-200 p-4 rounded h-12 flex items-center justify-end">
            {error ? <span className="text-red-500">{error}</span> : result}
          </div>
        </div>

        <div className="grid grid-cols-4 gap-2">
          {[
            "1",
            "2",
            "3",
            "+",
            "4",
            "5",
            "6",
            "-",
            "7",
            "8",
            "9",
            "*",
            "0",
            "/",
            "C",
            "=",
          ].map((btn, idx) => (
            <button
              key={idx}
              onClick={() =>
                btn === "="
                  ? calculate()
                  : btn === "C"
                  ? clearInput()
                  : ["+", "-", "*", "/"].includes(btn)
                  ? handleOperatorClick(btn)
                  : handleNumberClick(btn)
              }
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
              {btn}
            </button>
          ))}
          <button
            onClick={handleSeparateClick}
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded col-span-4"
          >
            Séparer
          </button>
        </div>

        <button
          onClick={downloadCSV}
          className="mt-4 bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded w-full"
        >
          Télécharger CSV
        </button>
      </div>
    </div>
  );
};

export default Calculator;
