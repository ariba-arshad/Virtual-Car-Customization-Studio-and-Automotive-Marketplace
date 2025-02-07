CREATE DATABASE sda_project

CREATE TABLE Participant(
	id int primary key IDENTITY(1,1),
	username VARCHAR(100) UNIQUE,
	password VARCHAR(20) CHECK(len(password)<=20),
	email VARCHAR(50) CHECK(email LIKE '%@gmail.com'),
	fname VARCHAR(100),
	lname VARCHAR(100),
	address VARCHAR(100),
	phoneNo VARCHAR(20),
	creditcardNo VARCHAR(20),
	participantType VARCHAR(20),
	companyName VARCHAR(100),
	description VARCHAR(500),
	specialization VARCHAR(200)
);

INSERT INTO Participant (username, password, email, fname, lname, address, phoneNo, creditcardNo, participantType, companyName, description, specialization)
VALUES 
('user1', 'pass123', 'user1@gmail.com', 'John', 'Doe', '123 Main St', '555-1234', '1111222233334444', 'user', NULL, NULL, NULL),
('user2', 'securePwd', 'user2@gmail.com', 'Jane', 'Smith', '456 Oak St', '555-5678', '4444555566667777', 'mechanic', 'ABC Corp', 'Software Engineer', 'Web Development'),
('user3', 'password321', 'user3@gmail.com', 'Bob', 'Johnson', '789 Elm St', '555-9012', '8888999900001111', 'user', NULL, NULL, NULL),
('user4', 'secretPass', 'user4@gmail.com', 'Alice', 'Williams', '101 Pine St', '555-3456', '2222333344445555', 'mechanic', 'XYZ Ltd', 'Marketing Specialist', 'Digital Marketing'),
('user5', 'myPass123', 'user5@gmail.com', 'Charlie', 'Brown', '202 Cedar St', '555-7890', '6666777788889999', 'user', NULL, NULL, NULL),
('user6', 'topSecret', 'user6@gmail.com', 'Eva', 'Jones', '303 Maple St', '555-2345', '3333444455556666', 'seller', 'LMN Inc', 'Data Scientist', NULL),
('user7', 'pass456', 'user7@gmail.com', 'David', 'Miller', '404 Birch St', '555-6789', '9999000011112222', 'user', NULL, NULL, NULL),
('user8', 'securePasswd', 'user8@gmail.com', 'Sophie', 'White', '505 Spruce St', '555-1234', '7777888899990000', 'seller', 'PQR Co', 'Graphic Designer', NULL),
('user9', 'mypassword', 'user9@gmail.com', 'Frank', 'Davis', '606 Pine St', '555-5678', '1111222233334444', 'user', NULL, NULL, NULL),
('user10', 'strongPass', 'user10@gmail.com', 'Olivia', 'Taylor', '707 Oak St', '555-9012', '4444555566667777', 'seller', 'RST Ltd', 'Network Engineer', NULL);

INSERT INTO Participant (username, password, email, fname, lname, address, phoneNo, creditcardNo, participantType, companyName, description, specialization)
VALUES 
('user11', 'pass789', 'user11@gmail.com', 'Sam', 'Roberts', '808 Elm St', '555-3456', '2222333344445555', 'user', NULL, NULL, NULL),
('user12', 'safePwd', 'user12@gmail.com', 'Lily', 'Clark', '909 Maple St', '555-7890', '6666777788889999', 'mechanic', 'UVW Corporation', 'Project Manager', 'Project Management'),
('user13', 'userpass', 'user13@gmail.com', 'Tom', 'Anderson', '1011 Cedar St', '555-2345', '3333444455556666', 'user', NULL, NULL, NULL),
('user14', 'pass987', 'user14@gmail.com', 'Sophia', 'Brown', '1213 Birch St', '555-6789', '9999000011112222', 'mechanic', 'XYZ Corp', 'UX/UI Designer', 'UX/UI Design'),
('user15', 'secure123', 'user15@gmail.com', 'Leo', 'Mitchell', '1415 Pine St', '555-1234', '7777888899990000', 'user', NULL, NULL, NULL),
('user16', 'password789', 'user16@gmail.com', 'Grace', 'Wilson', '1617 Oak St', '555-5678', '1111222233334444', 'mechanic', 'MNO Limited', 'Content Writer', 'Content Creation'),
('user17', 'pass432', 'user17@gmail.com', 'Daniel', 'Hall', '1819 Elm St', '555-9012', '4444555566667777', 'user', NULL, NULL, NULL),
('user18', 'safePass123', 'user18@gmail.com', 'Mia', 'Fisher', '2021 Maple St', '555-3456', '2222333344445555', 'seller', 'PQR Incorporated', 'Financial Analyst', NULL),
('user19', 'mypass123', 'user19@gmail.com', 'Ethan', 'Jones', '2223 Pine St', '555-7890', '6666777788889999', 'user', NULL, NULL, NULL),
('user20', 'strongPwd', 'user20@gmail.com', 'Ava', 'Baker', '2425 Oak St', '555-2345', '3333444455556666', 'seller', 'LMN Limited', 'Systems Analyst', NULL);



select * from Participant


CREATE TABLE SparePart(
	id int primary key IDENTITY(1,1),
	name VARCHAR(100),
	description VARCHAR(200),
	category VARCHAR(100),
	price FLOAT,
	stockQuantity INTEGER, 
	sellerId int foreign key references Participant(id)
);

-- Seller 1
INSERT INTO SparePart (name, description, category, price, stockQuantity, sellerId)
VALUES 
('Engine Oil', 'Premium synthetic engine oil for superior lubrication and engine protection. Suitable for all vehicle types.', 'Fluids', 799.99, 100, 6),
('Brake Pads', 'High-performance ceramic brake pads designed for exceptional stopping power and durability.', 'Brakes', 1299.99, 75, 6),
('Air Filter', 'Advanced air filtration technology for improved engine performance and fuel efficiency.', 'Filters', 599.99, 150, 6);

-- Seller 2
INSERT INTO SparePart (name, description, category, price, stockQuantity, sellerId)
VALUES 
('Spark Plugs', 'Iridium spark plugs engineered for efficient combustion and increased horsepower. Long-lasting and reliable.', 'Ignition', 899.99, 200, 8),
('Transmission Fluid', 'Synthetic transmission fluid for smooth and responsive gear shifts. Suitable for automatic and manual transmissions.', 'Fluids', 699.99, 80, 8),
('Wiper Blades', 'Premium silicone wiper blades for streak-free visibility in all weather conditions. Easy to install and long-lasting.', 'Wipers', 549.99, 120, 8);

-- Seller 3
INSERT INTO SparePart (name, description, category, price, stockQuantity, sellerId)
VALUES 
('Headlight Bulbs', 'High-intensity LED headlight bulbs for enhanced brightness and visibility on the road. Easy to install and energy-efficient.', 'Lights', 799.99, 100, 10),
('Battery', 'High-performance car battery with advanced technology for reliable and consistent power supply. Maintenance-free design.', 'Electrical', 1499.99, 50, 10),
('Tire Pressure Gauge', 'Digital tire pressure gauge with an ergonomic design for accurate readings. Compact and easy to use.', 'Tools', 599.99, 30, 10);

-- Seller 4
INSERT INTO SparePart (name, description, category, price, stockQuantity, sellerId)
VALUES 
('Oil Filter', 'High-efficiency synthetic oil filter designed to trap contaminants and protect the engine. Durable and easy to replace.', 'Filters', 599.99, 120, 18),
('Cabin Air Filter', 'Activated carbon cabin air filter for trapping dust, pollen, and odors. Provides clean and fresh air inside the vehicle.', 'Filters', 699.99, 80, 18),
('Radiator Coolant', 'Extended-life radiator coolant for optimal engine cooling. Protects against corrosion and overheating.', 'Cooling', 799.99, 100, 18);

-- Seller 5
INSERT INTO SparePart (name, description, category, price, stockQuantity, sellerId)
VALUES 
('Oxygen Sensor', 'High-quality oxygen sensor for monitoring and optimizing fuel efficiency. Ensures proper combustion and emission control.', 'Sensors', 1299.99, 50, 20),
('Fuel Filter', 'Performance fuel filter for maintaining clean and efficient fuel delivery to the engine. Enhances overall engine performance.', 'Filters', 699.99, 70, 20),
('Car Wax', 'Professional-grade car wax for a long-lasting glossy finish and protection against environmental elements. Easy to apply and buff.', 'Detailing', 549.99, 40, 20);


select * from SparePart
 

CREATE TABLE SparePartsOrder(
	id int primary key IDENTITY(1,1),
	orderId int,
	sparePartId int foreign key references SparePart(id),
	quantity int,
	orderStatus VARCHAR(100),
	orderDate date,
	totalBill int,
	paymentType VARCHAR(100),
	sellerID int foreign key references participant(id),
	buyerID int foreign key references participant(id)
)

select * from SparePartsOrder

CREATE TABLE Cart (
    user_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES Participant(id),
    FOREIGN KEY (product_id) REFERENCES SparePart(id)
);

select * from Cart


CREATE TABLE ReviewTable (
    reviewID INT PRIMARY KEY IDENTITY(1,1),
	name VARCHAR(255),
	date DATE,
    content VARCHAR(255),
	rating INT,
	spID INT foreign key references SparePart(id)
);

INSERT INTO ReviewTable (name, date, content, rating, spID)
VALUES 
('John Doe', '2023-01-15', 'Excellent engine oil! My car runs smoother than ever.', 5, 1),
('Alice Smith', '2023-02-02', 'Good quality brake pads, noticeable improvement in braking performance.', 4, 2),
('Robert Johnson', '2023-03-10', 'The air filter works great, increased fuel efficiency and engine responsiveness.', 5, 3);

INSERT INTO ReviewTable (name, date, content, rating, spID)
VALUES 
('Emily White', '2023-04-05', 'These spark plugs are fantastic! Noticed a significant boost in horsepower.', 5, 4),
('Michael Brown', '2023-05-20', 'Smooth gear shifts with this transmission fluid. Highly recommended!', 5, 5),
('Sarah Taylor', '2023-06-08', 'Wiper blades are excellent, even in heavy rain. Clear visibility all the time.', 4, 6);

INSERT INTO ReviewTable (name, date, content, rating, spID)
VALUES 
('Chris Wilson', '2023-07-12', 'LED headlight bulbs are bright and illuminate the road well. Great purchase!', 5, 7),
('Olivia Davis', '2023-08-25', 'The car battery has been reliable. No issues with power supply so far.', 4, 8),
('Daniel Miller', '2023-09-18', 'Accurate tire pressure gauge. Handy tool for regular maintenance.', 5, 9);

INSERT INTO ReviewTable (name, date, content, rating, spID)
VALUES 
('Sophie Baker', '2023-10-22', 'Synthetic oil filter is effective, and it is easy to replace. Keeps the engine clean.', 5, 10),
('Jackson Hall', '2023-11-15', 'Cabin air filter works well in filtering out dust and odors. Noticeable difference.', 4, 11),
('Ava Fisher', '2023-12-01', 'Radiator coolant does its job. Engine temperature stays within the normal range.', 4, 12);

INSERT INTO ReviewTable (name, date, content, rating, spID)
VALUES 
('Liam Anderson', '2023-01-02', 'Oxygen sensor improved fuel efficiency. Engine runs more smoothly now.', 5, 13),
('Eva Roberts', '2023-02-15', 'Fuel filter is doing its job well. Engine performance is consistent.', 4, 14),
('Noah Clark', '2023-03-30', 'Car wax provides a glossy finish. Easy to apply and adds a protective layer.', 5, 15);


select * from ReviewTable

CREATE TABLE ReviewTable_M (
    reviewID INT PRIMARY KEY IDENTITY(1,1),
	name VARCHAR(255),
	date DATE,
    content VARCHAR(255),
	rating INT,
	mechanicID INT foreign key references Participant(id)
);

INSERT INTO ReviewTable_M (name, date, content, rating, mechanicID)
VALUES 
('John Doe', '2023-01-15', 'Mechanic did an excellent job on my car. Engine runs smoother now.', 5, 2),
('Alice Smith', '2023-02-02', 'Brake pad replacement was quick and effective. Brakes feel much better.', 4, 2),
('Robert Johnson', '2023-03-10', 'The air filter replacement was done professionally. Noticed immediate improvement.', 5, 2);

INSERT INTO ReviewTable_M (name, date, content, rating, mechanicID)
VALUES 
('Emily White', '2023-04-05', 'Spark plug replacement was swift. Car now has better acceleration.', 5, 4),
('Michael Brown', '2023-05-20', 'Transmission fluid change was done efficiently. Smooth gear shifts afterward.', 5, 4),
('Sarah Taylor', '2023-06-08', 'Wiper blade installation was quick, and they work perfectly in the rain.', 4, 4);

INSERT INTO ReviewTable_M (name, date, content, rating, mechanicID)
VALUES 
('Chris Wilson', '2023-07-12', 'Headlight bulb replacement was done professionally. Lights are much brighter now.', 5, 12),
('Olivia Davis', '2023-08-25', 'Car battery installation was quick and hassle-free. No issues with power.', 4, 12),
('Daniel Miller', '2023-09-18', 'Tire pressure gauge calibration was accurate. Mechanic was knowledgeable.', 5, 12);

INSERT INTO ReviewTable_M (name, date, content, rating, mechanicID)
VALUES 
('Sophie Baker', '2023-10-22', 'Oil filter replacement was done efficiently. Engine performance has improved.', 5, 14),
('Jackson Hall', '2023-11-15', 'Cabin air filter change was quick. The air inside the car feels fresher.', 4, 14),
('Ava Fisher', '2023-12-01', 'Radiator coolant refill was done professionally. Engine temperature is stable.', 4, 14);

INSERT INTO ReviewTable_M (name, date, content, rating, mechanicID)
VALUES 
('Liam Anderson', '2023-01-02', 'Oxygen sensor replacement improved fuel efficiency. Mechanic was skilled.', 5, 16),
('Eva Roberts', '2023-02-15', 'Fuel filter change was done efficiently. Car has consistent performance.', 4, 16),
('Noah Clark', '2023-03-30', 'Car wax application was thorough. The car has a glossy and protective finish.', 5, 16);


select * from ReviewTable_M

CREATE TABLE Posts (
    postID INT PRIMARY KEY IDENTITY(1,1),
	name VARCHAR(100),
    title VARCHAR(255) NOT NULL,
    content VARCHAR(2000),
    datePosted DATE,
    imageURL VARCHAR(255),
    videoURL VARCHAR(255) 
);

-- Post 1
INSERT INTO Posts (name, title, content, datePosted, imageURL, videoURL)
VALUES 
('John Doe', 'Choosing the Right Engine Oil for Your Car', 'Understanding the importance of selecting the right engine oil for optimal performance and longevity.', '2023-01-05', NULL, 'https://youtu.be/Yncral31rL4');

-- Post 2
INSERT INTO Posts (name, title, content, datePosted, imageURL, videoURL)
VALUES 
('Alice Smith', 'The Importance of Quality Brake Pads', 'Exploring the crucial role that high-quality brake pads play in ensuring safe and effective braking.', '2023-02-10', 'https://petespaint.ca/wp-content/uploads/2018/04/canstockphoto7108449-300x200.jpg', NULL);

-- Post 3
INSERT INTO Posts (name, title, content, datePosted, imageURL, videoURL)
VALUES 
('Robert Johnson', 'Maximizing Fuel Efficiency with the Right Air Filter', 'Tips on selecting and maintaining the right air filter to improve fuel efficiency and engine performance.', '2023-03-15', NULL, NULL);

-- Post 4
INSERT INTO Posts (name, title, content, datePosted, imageURL, videoURL)
VALUES 
('Emily White', 'Upgrading Spark Plugs for Better Engine Performance', 'Discussing the benefits of upgrading spark plugs and the impact on overall engine performance.', '2023-04-20', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcb2zWi_SEdC-UuTIEeZGmO8EAU44G0fI0NX3oqzxItCoPX5qXoqofF-IBxk1y3WmmLos&usqp=CAU', 'https://youtu.be/DYMK69DedTU');

-- Post 5
INSERT INTO Posts (name, title, content, datePosted, imageURL, videoURL)
VALUES 
('Michael Brown', 'Air Filter', 'Is your car feeling sluggish? It might be time to replace the air filter! Follow these steps for a quick and easy swap: <br> Step 1: Locate the air filter housing under the hood. <br> Step 2: Unclamp or unscrew the housing cover. <br> Step 3: Remove the old air filter and inspect for dirt or damage. <br> Step 4: Insert the new air filter, ensuring it is properly seated. <br> Step 5: Secure the housing cover back in place. <br> Feel the difference right away! Share your experience below!
', '2023-05-25', NULL, 'https://www.youtube.com/embed/RdXVxbd59es');

-- Post 6
INSERT INTO Posts (name, title, content, datePosted, imageURL, videoURL)
VALUES 
('Sarah Taylor', 'Brake Pad', 'Tips on choosing and maintaining high-performance brake pad in various weather conditions.', '2023-06-30', 'https://assets.firestonecompleteautocare.com/content/dam/bsro-sites/fcac/blog/images/2020/10/brake_pad_comparison.jpg', NULL);

select * from Posts


CREATE TABLE Comments(
    commentID INT PRIMARY KEY IDENTITY(1,1),
    postID INT,
    commenterName VARCHAR(100),
    commentText VARCHAR(1000),
    commentDate DATE,
    FOREIGN KEY (PostID) REFERENCES Posts(PostID)
);

select * from Comments

-- Comments for Post 1
INSERT INTO Comments (postID, commenterName, commentText, commentDate)
VALUES 
(1, 'CarEnthusiast21', 'Great video! Choosing the right engine oil is crucial for the car longevity.', '2023-01-06'),
(1, 'AutoExpert', 'I agree! Regular oil changes with the right oil can significantly improve engine performance.', '2023-01-07'),
(1, 'SpeedDemon', 'I switched to synthetic oil recently, and I can feel the difference in my car performance.', '2023-01-08');

-- Comments for Post 2
INSERT INTO Comments (postID, commenterName, commentText, commentDate)
VALUES 
(2, 'BrakeGuru', 'Quality brake pads are a game-changer! They make such a difference in stopping power.', '2023-02-11'),
(2, 'SafetyFirst', 'I upgraded my brake pads recently, and it made a huge improvement in my car safety.', '2023-02-12'),
(2, 'CarOwner123', 'How often should brake pads be replaced for optimal performance?', '2023-02-13');

-- Comments for Post 3
INSERT INTO Comments (postID, commenterName, commentText, commentDate)
VALUES 
(3, 'FuelEfficiencyFan', 'Maximizing fuel efficiency is key! Thanks for the tips on air filters.', '2023-03-16'),
(3, 'GreenDriving', 'I have been neglecting my air filter. Time to replace it and save on fuel!', '2023-03-17'),
(3, 'CarCareTips', 'A clean air filter also contributes to a cleaner engine and reduces emissions.', '2023-03-18');

-- Comments for Post 4
INSERT INTO Comments (postID, commenterName, commentText, commentDate)
VALUES 
(4, 'SparkPlugMaster', 'Upgrading spark plugs is a must for any car enthusiast. Great video!', '2023-04-21'),
(4, 'SpeedRacer', 'Changed my spark plugs last week. Smoother acceleration and better fuel efficiency!', '2023-04-22'),
(4, 'DIYMechanic', 'Is it difficult to change spark plugs yourself, or should I go to a mechanic?', '2023-04-23');

-- Comments for Post 5
INSERT INTO Comments (postID, commenterName, commentText, commentDate)
VALUES 
(5, 'CarMaintenance101', 'Thanks for the quick tutorial on checking and replacing the air filter!', '2023-05-26'),
(5, 'DIYCarCare', 'Air filter replacement is so simple, and it makes a big difference in engine performance.', '2023-05-27'),
(5, 'MotorHead', 'Great video! Regular maintenance is key to keeping our cars running smoothly.', '2023-05-28');

-- Comments for Post 6
INSERT INTO Comments (postID, commenterName, commentText, commentDate)
VALUES 
(6, 'VisibilityExpert', 'Choosing the right wiper blades is essential, especially during the rainy season.', '2023-07-01'),
(6, 'RainyDayDriver', 'I upgraded to silicone wiper blades, and they really do provide streak-free visibility.', '2023-07-02'),
(6, 'AutoCareTips', 'Do not forget to check and replace your wiper blades regularly for optimal performance.', '2023-07-03');



select * from Participant
select * from SparePart
select * from SparePartsOrder
select * from Cart
select * from ReviewTable
select * from ReviewTable_M
select * from Posts
select * from Comments

