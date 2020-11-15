

# Database SQL Server Notes:

## Perscholas: aws re/Start
  ### Done By: Hiba Abbaker

**Selecting Data from a Database:**

- Use the SELECT statement when you want to see a subset of rows, columns or both.
- The result of the SELECT statement is called a result set. It lists rows that contain the same number of columns.

```sql
SELECT column1, column2, ...
FROM table_name;
```

Optional Clauses of the SELECT Statement:

Optional Clause: Purpose

- **WHERE** : Request only certain rows from a table

    The following SQL statement selects all customers that are located in "Germany", "France" or "UK":

    ```sql
    SELECT * FROM Customers
    WHERE Country IN ('Germany', 'France', 'UK');
    ```

    The following SQL statement selects all customers that are NOT located in "Germany", "France" or "UK":

    ```sql
    SELECT * FROM Customers
    WHERE Country NOT IN ('Germany', 'France', 'UK');
    ```

- **GROUP BY** : Use a column identifier to organize the data in the result set into groups.
- **ORDER BY**: Sort query results by one or more columns and in ascending or descending order.

The following SQL statement lists the number of customers in each country, sorted high to low:

```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;
```

- **BY HAVING**: Use in conjunction with GROUP BY to specify which groups to include in results.
- The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.

    The following SQL statement lists the number of customers in each country, sorted high to   low (Only include countries with more than 5 customers):

```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC;
```

**Guidelines for Constructing SQL Statements:**

•Separate words in the statement as follows: 

– Enter extra spaces or line breaks if you like, and the statement will still execute correctly. 

• Type SQL keywords in upper or lowercase. 

• Type table, column, and index names that: 

– Begin with a letter. 

– Limit length to 30 characters. 

– Include no spaces.

**Performing a Conditional Search:**

![Conditionalclauses](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(161).png)

![Single search condition](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(169).png)

![Multiple Conditional Operators](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(166).png)

**Types of Functions:**

Configuration  —  Metadata — Cursor —  Security —  System Statistical  —   Date & Time **—** 

String  — Text & Image — Mathematical  — System.

![Functions](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(175).png)

![Date Functions](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(176).png)

![Nested Functions](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(177).png)

![Addregated Functions](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(178).png)

![Keywords](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(180).png)

# The SQL SELECT DISTINCT Statement:

 **The SELECT DISTINCT** statement is used to return only distinct (different) values. The following SQL statement selects only the DISTINCT values from the "Country" column in the "Customers" table:

```sql
SELECT DISTINCT Country FROM Customers;
```

**DISTINCT in a COUNT Function**: The following SQL statement lists the number of different (distinct) customer countries.

```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```

**String functions**

are used to perform an operation on input string and return an output string.

Following are the string functions defined in SQL: 

```sql
**Remove leading spaces from a string:**
SELECT LTRIM('     SQL Tutorial') AS LeftTrimmedString;
```

![Substring Function](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(182).png)

**Retrieving Data from Multiple Tables :**

• Combine the Results of Two Queries 

• Retrieve Data by Joining Tables

![Union Operator](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(184).png)

**Entity Relationships Training Database:** 

• Courses are delivered by Instructors 

• Courses take place in Classrooms

![ER Database](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(186).png)

**Joins: A JOIN** clause is used to combine rows from two or more tables, based on a related column between them.

**Different Types of SQL JOINs:** 

**Here are the different types of the JOINs in SQL:**

- **(INNER) JOIN**: Returns records that have matching values in both tables

    ![INNER JOIN](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/img_innerjoin.gif)

- **LEFT (OUTER) JOIN**: Returns all records from the left table, and the matched records from the right table

    ![LEFT JOIN](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/img_leftjoin.gif)

- **RIGHT (OUTER) JOIN**: Returns all records from the right table, and the matched records from the left table

    ![RIGHT JOIN](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/img_rightjoin.gif)

- **FULL (OUTER) JOIN**: Returns all records when there is a match in either left or right table

![FULL JOIN](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/img_fulljoin.gif)

- **SQL Self JOIN:** A self JOIN is a regular join, but the table is joined with itself.

```sql
The following SQL statement matches customers that are from the same city.

SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
	FROM Customers A, Customers B
	WHERE A.CustomerID <> B.CustomerID
	AND A.City = B.City
	ORDER BY A.City;
```

**Qualified Column Names:**

Every column contains one value for each row of a table. SQL statements often refer to such values. A fully qualified column reference consists of the table name, a period, and then the column name (for example, PRICING.Product).

```sql
SELECT PRICING.Cost
 FROM PRICING
 WHERE PRICING.Product = 'F-35' ;
```

![TABLE ALIAS](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(188).png)

# Indexes:

An index is a smaller lookup table that can be used to jump to the specified search result. Indexes are used to retrieve data from the database more quickly than otherwise. The users cannot see the indexes, they are just used to speed up searches/queries.

**An index can:** 

• Increase the speed of operations in a table 

• Be created using one or more column 

• This is the foundation for fast random lookups 

• Which helps with effective ordering of the access to the records

**Types of Keys in Database Management System:** There are mainly seven different types of Keys in DBMS and each key has it’s different functionality:

- **Super Key -**  A super key is a group of single or multiple keys which identifies rows in a table.
- **Primary Key -**  is a column or group of columns in a table that uniquely identify every row in that table.
- **Candidate Key -**  is a set of attributes that uniquely identify tuples in a table. Candidate Key is a super key with no repeated attributes.
- **Alternate Key -**  is a column or group of columns in a table that uniquely identify every row in that table.
- **Foreign Key -**  is a column that creates a relationship between two tables. The purpose of Foreign keys is to maintain data integrity and allow navigation between two different instances of an entity.
- **Compound Key -**  has two or more attributes that allow you to uniquely recognize a specific record. It is possible that each column may not be unique by itself within the database.
- **Composite Key -**  An artificial key which aims to uniquely identify each record is called a surrogate key. These kind of key are unique because they are created when you don't have any natural primary key.
- **Surrogate Key -**  An artificial key which aims to uniquely identify each record is called a surrogate key. These kind of key are unique because they are created when you don't have any natural primary key.

**SQL PRIMARY KEY Constraint :**  

       The PRIMARY KEY constraint uniquely identifies each record in a table.

 • Primary keys must contain UNIQUE values, and cannot contain NULL values.

• A table can have only ONE primary key; and in the table, this primary key can consist of single or multiple columns (fields).

• A column is useful and appropriate for a key if it is: – Unique – Stable – Valid – Familiar – Brief – Simple – Efficient – Verifiable – Secure

```sql
The following SQL creates a PRIMARY KEY on the "ID" column when the "Persons" table 
is created:
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);
```

**Partitioning:**

•Splits a large table into smaller, separate tables, yet it still gets treated as a single table by the SQL layer 

• Allows queries to run much faster due to having less data to scan from the smaller tables 

• Must be added into the primary key 

• Is always numbered automatically and in order when created

**Table Relationships**:

 • There are three types of relationships you will encounter at this stage in the design: 

   **one-to-many,** **one-to-one**, **and many-to-many**. 

• To determine which relationships your tables should use: 

– Examine the concepts represented in the tables. 

– Consider how many columns in one table can relate to columns in the other table. 

– Perform this analysis in both directions.

![One-To-One Relationship](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(196).png)

![One-To-Many Relationship](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(195).png)

![Many-To-Many Relationship](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(194).png)

![Database%20SQL%20Server%20Notes%20fad42401e17f4d7bb4a50f9d3d88f492/Screenshot_(190).png](Database%20SQL%20Server%20Notes%20fad42401e17f4d7bb4a50f9d3d88f492/Screenshot_(190).png)

![Junction Table](https://raw.githubusercontent.com/Hiba-A/Shared_Codes/master/Database/Screenshot_(190).png)

**Updating/Deleting Tables:**

**Transactions:** 

• Are a sequential group of database operations that are performed as one unit 

• Denote any alteration in a database 

• Will never be complete unless each operation is successful.

**Transactions must be:** 

• **Atomic**: Makes sure all operations are successful 

• **Consistent:** Confirms the database correctly changes states after a transaction has been effectively committed 

• **Isolated:** Allows transactions to function autonomously of and visible to each other 

• **Durable** (ACID): Provide an uncompromising plan, meaning that each work-unit performed in the database must either complete fully or have no effect at all.

### **The following commands are used to control transactions.**

- **COMMIT** − to save the changes.

```sql
DELETE from Customer where State = 'Texas';
COMMIT;
```

- **ROLLBACK** − to roll back the changes.

```sql
/*Post the DELETE command if we publish ROLLBACK it will revert the change that is 
performed due to the delete command.*/

DELETE from Customer where State = 'Texas';
ROLLBACK;
```

- **SAVEPOINT** − creates points within the groups of transactions in which to ROLLBACK.
- **SET TRANSACTION** − Places a name on a transaction.

### Deleting Tables:

**To delete a table**, you will use the following MySQL DROP TABLE statement. Note: This statement will remove the table and data permanently from the database.

**To delete multiple tables**, in your DROP TABLE statement, separate each table by a comma. Note: When performing a DELETE and UPDATE, be careful with delete and update clauses, like counts, select, etc., to verify the output is as expected.

### Guidelines for Identifying Database Anomalies:

Anomalies may occur when database content changes: 

• Insertion anomaly: When you can't insert vital data into the database because other data is missing. For example, a clerk can't add customer information for a new customer who has not yet made a purchase. 

• Update anomaly: Happens when data is stored redundantly within the same table, making it hard to ensure that all copies of a particular information value are updated when the value needs to be changed. 

• Deletion anomaly: Happens when you delete unwanted information, and this results in wanted information getting deleted as well.

### Qualities Resulting from a Good Design Process:

    Clear, Essential, Cooperative, Efficient, Precise, Flexible, and Reusable.

# Backup and Restore:

 **It is recommended to have multiple backups** 

• In case something happens to your main backup 

• On-site and off-site—On-site conserves time to replace the content and off-site is needed in    case of a disaster.

**Recovering with a Backup:**

• If a database is lost, the backup will be needed to restore data to the closest time. 

• This is why it’s important to back up data often. If a disaster strikes, you want current information, not the information from 4 months ago. Otherwise, this could be detrimental to a business.

**Different Backup Types:**

Full,  Differential, and Incremental/ Transactional.

**Transaction Logs:** We can create a backup based on a combination of the database transaction log and the last full backup.

**Built-in/Native Backups:** These backups are commonly used to migrate databases between different SQL Server instances running on-premises or in the cloud. They can be used for data ingestion, disaster recovery, and so forth. The native backups also simplify the process of importing data and schemas from on-premises SQL Server instances, and will be easy for SQL Server DBAs to understand and use.

**Commercial Backups:**  Commercial tools can provide some risk transference for data loss.

### Importing and Exporting:

• **A simple method of backup and restore is with import/export.** 

– Exporting the database into a file (the backup) 

– Importing the DB into the database management system (the restore) 

• **Use redirection from Linux to do this.** 

– Simply open MySQL with the standard input of a backup to restore the database 

– You can also run a command to output the content of a database to a file that is creating the backup.

**Dump Files:** MY SQL package comes with mysqldump which allows you to dump a database into a file, and it's is great for backups

**Automated Backups:** SQL Server backup automation is a process that includes at least the following steps: Run SQL Server backup for selected databases on schedule. Compress & encrypt the backups.
