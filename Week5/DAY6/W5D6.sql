CREATE TABLE Customer (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL
);

CREATE TABLE CustomerProfile(
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT false,
	customer_id INTEGER UNIQUE,
	CONSTRAINT fk_customer
	FOREIGN KEY (customer_id)
	REFERENCES Customer(id)
	ON DELETE CASCADE 
);

INSERT INTO Customer(first_name, last_name)
VALUES
('John','Doe'),
('Jerome','Lalu'),
('Lea','Rive')

select * from Customer

Select first_name, last_name, COUNT(*) 
FROM Customer
GROUP BY first_name, last_name
HAVING COUNT(*) > 1;

DELETE FROM Customer
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Customer
    GROUP BY first_name, last_name
);

INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (
  true,
  (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')
);

INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (
  false,
  (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')
);

select * from CustomerProfile 
SELECT c.first_name 
FROM Customer c
JOIN CustomerProfile p ON c.id = p.customer_id
WHERE p.isLoggedIn = true; 

SELECT 
  c.first_name,
  p.isLoggedIn
FROM Customer c
LEFT JOIN CustomerProfile p ON c.id = p.customer_id;

SELECT COUNT(*) AS not_logged_in_count
FROM Customer c
JOIN CustomerProfile p ON c.id = p.customer_id
WHERE p.isLoggedIn = false;


CREATE TABLE Book (
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
	author VARCHAR(50) NOT NULL
);

INSERT INTO Book (title, author)
VALUES 
    ('Alice In Wonderland', 'Lewis Carroll'),
    ('Harry Potter', 'J.K Rowling'),
    ('To kill a mockingbird', 'Harper Lee');

CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    age INTEGER CHECK (age <= 15)
);

INSERT INTO Student (name, age)
VALUES 
    ('John', 12),
    ('Lera', 11),
    ('Patrick', 10),
    ('Bob', 14);

CREATE TABLE Library (
    book_fk_id INTEGER NOT NULL,
    student_fk_id INTEGER NOT NULL,
    borrowed_date DATE NOT NULL,

    PRIMARY KEY (book_fk_id, student_fk_id),

    CONSTRAINT fk_book
        FOREIGN KEY (book_fk_id)
        REFERENCES Book(book_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_student
        FOREIGN KEY (student_fk_id)
        REFERENCES Student(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- John borrowed Alice In Wonderland on 2022-02-15
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
);

-- Bob borrowed To kill a mockingbird on 2021-03-03
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-03-03'
);

-- Lera borrowed Alice In Wonderland on 2021-05-23
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    '2021-05-23'
);

-- Bob borrowed Harry Potter on 2021-08-12
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE_title = 'Harry Potter'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-08-12'
);


SELECT * FROM Library;
SELECT s.name, b.title
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id;

SELECT AVG(s.age) AS avg_age
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

DELETE FROM Student WHERE name = 'Bob';

