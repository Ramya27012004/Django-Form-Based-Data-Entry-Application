# Django Form-Based Data Entry Application

This project is a **Django Form-Based Web Application** that allows users to insert and view data for three modules: **Topic**, **Webpage**, and **AccessRecord**.  
It demonstrates how Django handles form submission, data storage, and data display using the MVT (Model–View–Template) architecture.

---

## Project Overview

This application enables users to:

- Submit data through HTML forms  
- Store the submitted data in a database  
- View all stored records on display pages  
- Work with linked data through model relationships  

---

##  Features

### **Topic**
- Insert topic name using a form  
- View all stored topics  

### **Webpage**
- Select a topic from a dropdown  
- Add webpage name and URL  
- View all webpages  

### **AccessRecord**
- Select a webpage  
- Enter author name and date  
- View all access records  

---

## Technologies Used

- Python  
- Django Framework  
- HTML Templates  
- SQLite Database  

---

## Application Structure

- **Models:** Define Topic, Webpage, AccessRecord  
- **Views:** Handle form submission and data processing  
- **Templates:** Display forms and stored records  
- **Relationships:**  
  - One Topic → Many Webpages  
  - One Webpage → Many AccessRecords  

---

## How It Works

1. User fills in a form (Topic/Webpage/AccessRecord).  
2. Django processes the request using the POST method.  
3. Data is saved into the database.  
4. Display pages show all stored data.  
5. CSRF protection ensures form submission security.

---

## Purpose of the Project

This project helps users understand:

- Django form handling  
- How data flows from frontend to backend  
- How database tables relate to each other  
- How to create a simple data-entry web application  

---

## Advantages

- Beginner-friendly  
- Demonstrates Django MVT architecture  
- Shows secure form handling  
- Helps understand relational databases  
- Useful for learning backend development  

---

##  AccessRecord Display Page (Explanation)

The **AccessRecord Display Page** displays all stored access records in a clear and organized table format. It allows users to easily view, validate, and understand the data submitted through the AccessRecord form.

### Purpose of the Display Page
- To show all AccessRecord entries stored in the database  
- To present the information in a structured and readable table  
- To allow users to review previously submitted records  
- To demonstrate how Django templates handle dynamic data rendering  

### How the Page Works
- All AccessRecord objects are fetched from the database in the view  
- These records are sent to the template through a context dictionary  
- The template iterates over each record and displays it inside a table row  
- Each row represents a single AccessRecord with relevant details  

### Information Displayed in the Table
- **ID** → Unique identifier for each access record  
- **Name** → The webpage associated with the access record  
- **Author** → The person who created or accessed the record  
- **Date** → The date when the record was added  

### Importance of This Display Page
- Provides a complete overview of stored access records  
- Makes it easy to verify correct data entry  
- Shows relational data between Webpage and AccessRecord  
- Enhances user experience with organized data presentation  

### Learning Outcome
Understanding this page helps users learn:
- How Django passes database data to templates  
- How to loop over data and display it in tabular format  
- How relationships between models are shown in UI  
- How MVT architecture enables dynamic content rendering  

