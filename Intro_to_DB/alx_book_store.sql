CREATE DATABASE IF NOT EXISTS alx_book_store;


-- 1) Authors
CREATE TABLE Authors (
  author_id      INT PRIMARY KEY,
  author_name    VARCHAR(215)
);

-- 2) Customers
CREATE TABLE Customers (
  customer_id    INT PRIMARY KEY,
  customer_name  VARCHAR(215),
  email          VARCHAR(215),
  address        TEXT
);

-- 3) Books
CREATE TABLE Books (
  book_id            INT PRIMARY KEY,
  title              VARCHAR(130),
  author_id          INT,
  price              DOUBLE,
  publication_date   DATE,
  FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- 4) Orders
CREATE TABLE Orders (
  order_id     INT PRIMARY KEY,
  customer_id  INT,
  order_date   DATE,
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- 5) Order_Details
CREATE TABLE Order_Details (
  orderdetailid  INT PRIMARY KEY,
  order_id       INT,
  book_id        INT,
  quantity       DOUBLE,
  FOREIGN KEY (order_id) REFERENCES Orders(order_id),
  FOREIGN KEY (book_id)  REFERENCES Books(book_id)
);
