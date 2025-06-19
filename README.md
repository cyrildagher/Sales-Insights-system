# 📊 Sales Insights System

## Overview

The **Sales Insights System** is a lightweight analytics platform built to help consumer goods companies transform raw transactional data into **clear, actionable business insights**. Designed with simplicity and clarity in mind, this tool enables even non-technical users to explore and understand their sales performance across products, regions, and time periods.

---

## 🧠 The Problem

Consumer goods companies manage large volumes of sales data—but raw numbers alone don’t support smart decision-making. Without effective analysis:

- 🚫 Top-performing products go unrecognized
- 🚫 Regional trends and anomalies stay hidden
- 🚫 Promotions and seasonal effects are hard to track
- 🚫 Strategy becomes guesswork, not data-driven

---

## 💡 The Solution

This system delivers a **simple, structured** and **insightful sales analysis workflow** that:

- 📦 Centralizes sales data in a **clean MySQL database**
- 📈 Analyzes key sales metrics like:
  - Top sellers
  - Revenue by region
  - Weekly/monthly sales trends
- 🧑‍💼 Presents insights clearly for **quick business decision-making**

### Sample Insights
- *“Lotion is the top seller in Kumasi in Q2”*
- *“Sales dipped in Tamale during July”*
- *“Shampoo revenue peaked during promotional week 34”*

---

## 🔧 Tech Stack

- **Backend / Analysis**: Python, FastAPI, Pandas, PyMySQL, Uvicorn
- **Database**: MySQL
- **Frontend**: Next.js, React, Tailwind CSS, react-icons
- **Data Input Format**: CSV or Excel

---

## 📁 Project Structure
sales-insights-system/
├── data/ # Sample raw sales data files
├── db/ # SQL scripts for table setup
├── analysis/ # Core Python scripts for insights
├── visualizations/ # Graphs & charts generated
├── app.py # Main dashboard or CLI entry point
├── requirements.txt
└── README.md

