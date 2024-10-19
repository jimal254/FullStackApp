import React, { useState, useEffect } from "react";
import api from "./api";
import "./App.css";

function App() {
  const [transactions, setTransactions] = useState([]); // get from api all data
  const [formData, setFormData] = useState({
    amount: "",
    category: "",
    description: "",
    is_income: false,
    date: "",
  }); // for post new data

  const fetchTransactions = async () => {
    const response = await api.get("/transactions/");
    setTransactions(response.data);
  };

  //when any effect occure like load app or rerander call func
  useEffect(() => {
    fetchTransactions();
  }, []);

  const handleInputChange = (event) => {
    const value =
      event.target.type === "checkbox"
        ? event.target.checked
        : event.target.value;

    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault(); // prevent react from handle this
    await api.post("/transactions/", formData);
    fetchTransactions();
    // reload the data
    setFormData({
      amount: "",
      category: "",
      description: "",
      is_income: false,
      date: "",
    });
  };

  return (
    <div className="App">
      <nav className="navbar">
        <div className="navbar-container">
          <a href="#">Finance App</a>
        </div>
      </nav>
      <section className="body">
        <form onSubmit={handleFormSubmit}>
          <div className="mb-mt">
            <label htmlFor="amount" className="form-label">
              Amount
            </label>
            <input
              type="number"
              className="form-input"
              name="amount"
              id="amount"
              onChange={handleInputChange}
              value={formData.amount}
            />
          </div>

          <div className="mb-mt">
            <label htmlFor="category" className="form-label">
              Category
            </label>
            <input
              type="text"
              className="form-input"
              name="category"
              id="category"
              onChange={handleInputChange}
              value={formData.category}
            />
          </div>

          <div className="mb-mt">
            <label htmlFor="description" className="form-label">
              Description
            </label>
            <input
              type="text"
              className="form-input"
              name="description"
              id="description"
              onChange={handleInputChange}
              value={formData.description}
            />
          </div>

          <div className="mb-mt">
            <label htmlFor="is_income" className="form-label">
              Is Income
            </label>
            <input
              type="checkbox"
              className="form-input"
              name="is_income"
              id="is_income"
              onChange={handleInputChange}
              checked={formData.isIncome}
            />
          </div>

          <div className="mb-mt">
            <label htmlFor="date" className="form-label">
              Date
            </label>
            <input
              type="date"
              className="form-input"
              name="date"
              id="date"
              onChange={handleInputChange}
              value={formData.date}
            />
          </div>
          <button type="submit">Submit</button>
        </form>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Amount</th>
              <th>Category</th>
              <th>Description</th>
              <th>Is Income</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map((transaction) => (
              <tr key={transaction.id}>
                <td>{transaction.id}</td>
                <td>{transaction.amount}</td>
                <td>{transaction.category}</td>
                <td>{transaction.description}</td>
                <td>{transaction.is_income ? "Yes" : "No"}</td>
                <td>{transaction.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}

export default App;
