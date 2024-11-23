1. What is a Database?
-> A database is an organized collection of structured data that is stored electronically. It allows for efficient storage, retrieval, and management 
   of data. Databases are crucial for applications that require handling large amounts of data, ensuring that the data can be accessed, updated, 
   and managed effectively.


2. What is Normalization?
-> Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. This process involves dividing 
   large tables into smaller, related tables and defining relationships between them. The main goal of normalization is to eliminate duplicate data, 
   minimize anomalies during data operations, and ensure that data dependencies are logical.


3. What is the Difference Between DBMS and RDBMS?
-> DBMS (Database Management System):
   - A DBMS is software that provides an interface for users to create, manage, and manipulate databases.
   - It can manage various types of databases (e.g., hierarchical, network, etc.).
   - DBMSs do not enforce relationships between tables.

-> RDBMS (Relational Database Management System):
   - An RDBMS is a type of DBMS that is based on the relational model introduced by E.F. Codd.
   - Data is stored in tables (relations) with rows and columns.
   - RDBMS enforces relationships between tables using foreign keys and supports ACID (Atomicity, Consistency, Isolation, Durability) properties 
     to ensure data integrity.


4. What is the E.F. Codd Rule of RDBMS Systems?
-> E.F. Codd introduced 12 rules (often referred to as Codd's 12 rules) that define what is required for a database management system to be 
   considered a true relational database management system (RDBMS). These rules include concepts like data being represented in tables, ensuring 
   systematic treatment of null values, maintaining data independence, supporting relational integrity, and more. Some key rules include:

  Here are E. F. Codd's 12 rules with one-line descriptions:

   1. The Information Rule: All information is represented by data in tables.
   2. The Guaranteed Access Rule: Every data element is accessible by a unique combination of table name, primary key, and column name.
   3. Systematic Treatment of Null Values: Nulls must be uniformly treated as unknown or inapplicable.
   4. Active Online Catalog Based on the Relational Model: The database catalog is stored as tables and can be queried like any other data.
   5. The Comprehensive Data Sublanguage Rule: The system must support a comprehensive language for data definition, manipulation, and transaction management.
   6. The View Updating Rule: All theoretically updatable views must be updatable by the system.
   7. High-Level Insert, Update, and Delete: The system must support set-level operations, not just single-row or single-column.
   8. Physical Data Independence: Changes in physical storage should not affect how data is accessed.
   9. Logical Data Independence: Changes to logical structure (like tables) should not affect applications.
   10. Integrity Independence: Integrity constraints must be stored independently in the catalog, enforceable by the system.
   11. Distribution Independence: Users should not be aware of the data's distribution across different locations.
   12. The Nonsubversion Rule: Low-level operations must not bypass integrity constraints set at a higher level.

   Rule 0: The Foundation Rule**: The system must manage the database using only its relational capabilities.


5. What is Data Redundancy?
-> Data redundancy occurs when the same piece of data is stored in multiple places within a database. While it can sometimes be intentional for 
   performance reasons, excessive redundancy can lead to inconsistencies, increased storage costs, and difficulties in maintaining data integrity.


6. What is a DDL Interpreter?
-> A DDL Interpreter processes Data Definition Language (DDL) statements in SQL. DDL statements are used to define the structure of the database, 
   such as creating, altering, or dropping tables and indexes. The DDL interpreter takes these statements, parses them, and updates the metadata 
   that describes the database schema.


7. What is a DML Compiler in SQL?
-> A DML Compiler processes Data Manipulation Language (DML) statements in SQL. DML statements include operations like `SELECT`, `INSERT`, `UPDATE`, 
   and `DELETE`, which are used to retrieve and manipulate data within a database. The DML compiler translates these high-level SQL statements 
   into low-level instructions that the database engine can execute.


8. What are SQL Key Constraints? Provide an Example.
-> SQL Key Constraints are rules applied to columns in a database table to enforce data integrity. Some common key constraints include:

  -   Primary Key:   Uniquely identifies each row in a table.
  -   Foreign Key:   Establishes a link between the data in two tables.
  -   Unique:   Ensures all values in a column are unique.
  -   Not Null:   Ensures that a column cannot have a null value.
  -   Check:   Ensures that all values in a column satisfy a specific condition.

  Example:  

    CREATE TABLE Employees (
        EmployeeID INT PRIMARY KEY,
        LastName VARCHAR(255) NOT NULL,
        FirstName VARCHAR(255) NOT NULL,
        DepartmentID INT,
        CONSTRAINT FK_Department FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
    );

In this example, `EmployeeID` is a primary key, and `DepartmentID` is a foreign key that references the `Departments` table.


9. What is a Savepoint? How to Create a Savepoint? Write a Query.
-> A Savepoint is a marker within a transaction that allows you to roll back to a specific point without rolling back the entire transaction. 
   This is useful when you want to partially undo changes without discarding all changes made during a transaction.

  Creating a Savepoint Example:  

    BEGIN TRANSACTION;

    INSERT INTO Employees (EmployeeID, LastName, FirstName, DepartmentID) 
    VALUES (1, 'Smith', 'John', 10);

    SAVEPOINT Savepoint1;

    UPDATE Employees SET LastName = 'Doe' WHERE EmployeeID = 1;

    ROLLBACK TO Savepoint1;

    COMMIT;

In this example, the `ROLLBACK TO Savepoint1` undoes the update but keeps the initial insert.


10. What is a Trigger and How to Create a Trigger in SQL?
-> A Trigger is a set of SQL statements that automatically execute in response to certain events on a particular table or view. Triggers are 
   often used to enforce business rules, maintain audit trails, or synchronize data across tables.

  Creating a Trigger Example:  

    CREATE TRIGGER trg_AuditLog 
    AFTER INSERT ON Employees
    FOR EACH ROW 
    BEGIN
        INSERT INTO AuditLog (Action, EmployeeID, ActionDate) 
        VALUES ('INSERT', NEW.EmployeeID, NOW());
    END;

In this example, the trigger `trg_AuditLog` inserts a record into the `AuditLog` table every time a new row is inserted into the `Employees` table.