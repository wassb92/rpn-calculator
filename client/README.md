# RPN Calculator Frontend

This is the frontend for the RPN Calculator project, built using React and styled with Tailwind CSS. The frontend allows users to perform Reverse Polish Notation (RPN) calculations and download previous calculations as a CSV file.

## Features

- **RPN Calculator**: Allows input of numbers and operators for RPN calculations.
- **Token Separation**: Users can separate tokens during input.
- **CSV Download**: Users can download their previous calculations as a CSV file.

## Prerequisites

- **Node.js**: Required to run the React frontend.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/wassb92/rpn-calculator.git
   cd client
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

This will start the React development server on `http://localhost:3000`.

## Usage

- Enter numbers and operators to perform RPN calculations.
- Click the "Séparer" button to separate tokens (e.g., between two numbers like 25 and 7).
- Click "=" to send the RPN operation to the backend and get the result.
- Use the "Télécharger CSV" button to download a CSV file with past calculations.

## Technologies Used

- **React**: JavaScript library for building the user interface.
- **Tailwind CSS**: Utility-first CSS framework for styling.
- **Axios**: HTTP client for sending API requests.
