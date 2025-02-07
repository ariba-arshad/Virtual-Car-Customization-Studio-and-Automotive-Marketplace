import pyodbc

from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def add_account(self, username, password, email, firstName, lastName, address, phone, creditCardNo, companyName, description, specialization, participantType):
        pass

    @abstractmethod
    def login(self, username, email, password):
        pass

    @abstractmethod
    def get_ParticipantID(self, username, email, password):
        pass

    @abstractmethod
    def getParticipantType(self, participant_id):
        pass

    @abstractmethod
    def reset_password(self, email, password):
        pass

    @abstractmethod
    def get_info(self, participant_id):
        pass

    @abstractmethod
    def verify_password(self, current_password, participant_id):
        pass

    @abstractmethod
    def update_info_seller(self, new_firstName, new_lastName, new_email, new_description, new_company, new_address, new_phone, new_creditCardNo, current_password, new_password, reenter_new_password, participant_id):
        pass

    @abstractmethod
    def update_info_user(self, new_firstName, new_lastName, new_email, new_address, new_phone, new_creditCardNo, current_password, new_password, reenter_new_password, participant_id):
        pass

    @abstractmethod
    def update_info_mechanic(self, new_firstName, new_lastName, new_email, new_description, new_specialization, new_company, new_address, new_phone, new_creditCardNo, current_password, new_password, reenter_new_password, participant_id):
        pass

    @abstractmethod
    def getSellerSpareParts(self, participant_id):
        pass

    @abstractmethod
    def getSellerOrders(self, participant_id):
        pass
    
    @abstractmethod
    def getBuyerOrders(self, participant_id):
        pass

    @abstractmethod
    def cancelOrder(self, order_id):
        pass

    @abstractmethod
    def addSparePart(self, name, quantity, price, category, description, participant_id):
        pass

    @abstractmethod
    def EditOrderStatus(self, edit_status_id, edit_status):
        pass

    @abstractmethod
    def EditSparePart(self, id, name=None, quantity=None, price=None, category=None, description=None):
        pass

    @abstractmethod
    def getCheckoutDetails(self, participant_id):
        pass

    @abstractmethod
    def getTotalBill(self, participant_id):
        pass

    @abstractmethod
    def get_next_order_id(self):
        pass

    @abstractmethod
    def checkout(self, participant_id, payment_method):
        pass

    @abstractmethod
    def get_spareParts(self):
        pass

    @abstractmethod
    def get_product_details(self, item_id):
        pass

    @abstractmethod
    def find_spareParts(self, string):
        pass

    @abstractmethod
    def get_sparePartsReviews(self, productID):
        pass

    @abstractmethod
    def add_Review(self, name, message, rating, product_id):
        pass

    @abstractmethod
    def add_to_cart(self, participant_id, product_id, quantity):
        pass

    @abstractmethod
    def check_quantity(self, part_id, quantity):
        pass

    @abstractmethod
    def get_mechanics(self):
        pass

    @abstractmethod
    def find_mechanic(self, string):
        pass

    @abstractmethod
    def get_mechanic_details(self, mechanic_id):
        pass

    @abstractmethod
    def get_mechanicReviews(self, mechanicID):
        pass

    @abstractmethod
    def addM_Review(self, name, message, rating, mechanic_id):
        pass

    @abstractmethod
    def get_cart_spareParts(self, participant_id):
        pass

    @abstractmethod
    def removefromCart(self, participant_id, part_id):
        pass

    @abstractmethod
    def addPost(self, name, title, description, image, video):
        pass

    @abstractmethod
    def addComment(self, commenter_name, comment_text, post_id):
        pass

    @abstractmethod
    def getPostsAndComments(self):
        pass


class ItemDatabase(DatabaseInterface):
    def __init__(self):
        self.conn = pyodbc.connect('')
        self.cursor = self.conn.cursor()
    
    def add_account(self, username, password, email, firstName, lastName, address, phone, creditCardNo, companyName, description, specialization, participantType):
        try:
            query = "INSERT INTO Participant (username, password, email, fname, lname, address, phoneNo, creditCardNo, companyName, description, specialization, participantType) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            values = (username, password, email, firstName, lastName, address, phone, creditCardNo, companyName, description, specialization, participantType)
            self.cursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise 

    def login(self,username2,email2,password2):
        query = "SELECT * FROM participant WHERE username = ? AND email = ? AND password = ?"
        self.cursor.execute(query, (username2, email2, password2))
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True

    def get_ParticipantID(self, username2, email2, password2):
        query = "SELECT id FROM participant WHERE username = ? AND email = ? AND password = ?"
        self.cursor.execute(query, (username2, email2, password2))
        row = self.cursor.fetchone()  # Fetch one row
        if row:
            ID = row[0]
            return ID
        else:
            return None  # Or any value that indicates no matching record found
    
    def getParticipantType(self, participant_id):
        query = "SELECT participantType FROM Participant WHERE id = ?"
        self.cursor.execute(query, (participant_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0] 
        else:
            return None
        
    def reset_password(self, email2, password2):
        query = "UPDATE participant SET password = ? WHERE email = ?"
        self.cursor.execute(query, (password2, email2))
        self.conn.commit()

    def get_info(self, participant_id):
        query = "SELECT email, fname, lname, address, phoneNo, creditCardNo, companyName, description, specialization FROM Participant where id = ?"
        self.cursor.execute(query, (participant_id,))
        result = self.cursor.fetchone()

        if result:
            email, fname, lname, address, phoneNo, creditCardNo, companyName, description, specialization = result
            return email, fname, lname, address, phoneNo, creditCardNo, companyName, description, specialization
            # print(f"{email}, {fname}, {lname}, {address}, {phoneNo}, {creditCardNo}, {companyName}, {description}")


    def verify_password(self, current_password, participant_id):
        query = "SELECT password FROM Participant WHERE id = ?"
        self.cursor.execute(query, (participant_id,))
        saved_password = self.cursor.fetchone()[0]
        # print(f"currentpassword={current_password} and databasepassword={saved_password}")
        if current_password==saved_password:
            return True
        else:
            return False
        
        
    def update_info_seller(self, new_firstName, new_lastName, new_email, new_description, new_company, new_address, new_phone, new_creditCardNo, current_password, new_password, reenter_new_password, participant_id):
        if(current_password):
            print(f"{current_password}")
            if not self.verify_password(current_password, participant_id):
                raise ValueError("Current password is incorrect.")

            if not (new_password and reenter_new_password):
                raise ValueError("New password is not entered.")

            if new_password and new_password != reenter_new_password:
                raise ValueError("New password and re-entered password do not match.") 

        query = "UPDATE Participant SET fName = ?, lName = ?, email = ?, description = ?, companyName = ?, address = ?, phoneNo = ?, creditCardNo = ?"
        if(current_password and new_password and reenter_new_password):
            query += ", password = ?"
            values = (new_firstName, new_lastName, new_email, new_description, new_company, new_address, new_phone, new_creditCardNo, new_password)
        else:
            values = (new_firstName, new_lastName, new_email, new_description, new_company, new_address, new_phone, new_creditCardNo)
        
        query += " WHERE id = ?"
        values += (participant_id,)

        self.cursor.execute(query, values)
        self.conn.commit()

    
    def update_info_user(self, new_firstName, new_lastName, new_email, new_address, new_phone, new_creditCardNo, current_password, new_password, reenter_new_password, participant_id):
        if(current_password):
            print(f"{current_password}")
            if not self.verify_password(current_password, participant_id):
                raise ValueError("Current password is incorrect.")

            if not (new_password and reenter_new_password):
                raise ValueError("New password is not entered.")

            if new_password and new_password != reenter_new_password:
                raise ValueError("New password and re-entered password do not match.") 

        query = "UPDATE Participant SET fName = ?, lName = ?, email = ?, address = ?, phoneNo = ?, creditCardNo = ?"
        if(current_password and new_password and reenter_new_password):
            query += ", password = ?"
            values = (new_firstName, new_lastName, new_email, new_address, new_phone, new_creditCardNo, new_password)
        else:
            values = (new_firstName, new_lastName, new_email, new_address, new_phone, new_creditCardNo)
        
        query += " WHERE id = ?"
        values += (participant_id,)

        self.cursor.execute(query, values)
        self.conn.commit()


    def update_info_mechanic(self, new_firstName, new_lastName, new_email, new_description, new_specialization, new_company, new_address, new_phone, new_creditCardNo, current_password, new_password, reenter_new_password, participant_id):
        if(current_password):
            print(f"{current_password}")
            if not self.verify_password(current_password, participant_id):
                raise ValueError("Current password is incorrect.")

            if not (new_password and reenter_new_password):
                raise ValueError("New password is not entered.")

            if new_password and new_password != reenter_new_password:
                raise ValueError("New password and re-entered password do not match.") 

        query = "UPDATE Participant SET fname = ?, lname = ?, email = ?, description = ?, specialization = ?, companyName = ?, address = ?, phoneNo = ?, creditCardNo = ?"
        if(current_password and new_password and reenter_new_password):
            query += ", password = ?"
            values = (new_firstName, new_lastName, new_email, new_description, new_specialization, new_company, new_address, new_phone, new_creditCardNo, new_password)
        else:
            values = (new_firstName, new_lastName, new_email, new_description, new_specialization, new_company, new_address, new_phone, new_creditCardNo)
        print(f"name={new_firstName} {new_lastName}")
        query += " WHERE id = ?"
        values += (participant_id,)

        self.cursor.execute(query, values)
        self.conn.commit()


    def getSellerSpareParts(self, participant_id):
        
        query = """
            SELECT id, name, description, category, price, stockQuantity
            FROM SparePart
            WHERE sellerId = ?
        """

        self.cursor.execute(query, (participant_id,))
        result = self.cursor.fetchall()
        return result
    
    def getSellerOrders(self, participant_id):
        
        query = """
        SELECT o.id, s.name, o.quantity, o.orderStatus, o.orderDate, o.totalBill, o.paymentType
        FROM SparePartsOrder o
        INNER JOIN SparePart s ON o.sparePartId = s.id
        WHERE o.sellerId = ?
        """

        self.cursor.execute(query, (participant_id,))
        result = self.cursor.fetchall()
        return result
        
    def getBuyerOrders(self, participant_id):
        
        query = """
        SELECT o.id, s.name, o.quantity, o.orderStatus, o.orderDate, o.totalBill
        FROM SparePartsOrder o
        INNER JOIN SparePart s ON o.sparePartId = s.id
        WHERE o.buyerID = ?
        """

        self.cursor.execute(query, (participant_id,))
        result = self.cursor.fetchall()
        return result
        

    def cancelOrder(self, order_id):
        query_check_status = """
            SELECT s.id, s.stockQuantity, o.quantity
            FROM SparePartsOrder o
            INNER JOIN SparePart s ON o.sparePartId = s.id
            WHERE o.id = ?
        """
        self.cursor.execute(query_check_status, (order_id,))
        order_data = self.cursor.fetchone()

        if order_data and order_data[0] and order_data[1] and order_data[2]:
            sparepart_id, current_stock, ordered_quantity = order_data

            query_cancel_order = """
                UPDATE SparePartsOrder
                SET orderStatus = 'Cancelled'
                WHERE id = ? and orderStatus = 'Processing'
            """
            self.cursor.execute(query_cancel_order, (order_id,))

            # Increase the stockQuantity in SparePart
            new_stock = current_stock + ordered_quantity
            query_update_stock = """
                UPDATE SparePart
                SET stockQuantity = ?
                WHERE id = ?
            """
            self.cursor.execute(query_update_stock, (new_stock, sparepart_id))

            self.conn.commit()
            print(f"Order {order_id} has been cancelled. Stock updated.")
        else:
            print(f"Order {order_id} cannot be cancelled. Order not found or incomplete data.")




    def addSparePart(self, name, quantity, price, category, description, participant_id):
        check_query = "SELECT COUNT(*) FROM SparePart WHERE name = ? AND stockQuantity = ? AND price = ? AND category = ? AND description = ? AND sellerId = ?"
        check_values = (name, quantity, price, category, description, participant_id)
        self.cursor.execute(check_query, check_values)
        existing_count = self.cursor.fetchone()[0]

        if existing_count == 0:
            insert_query = "INSERT INTO SparePart (name, stockQuantity, price, category, description, sellerId) VALUES (?, ?, ?, ?, ?, ?)"
            insert_values = (name, quantity, price, category, description, participant_id)
            self.cursor.execute(insert_query, insert_values)
            self.conn.commit()
        else:
            print("Spare part with the same details already exists.")    

    def EditOrderStatus(self, edit_status_id, edit_status):
        update_query = "UPDATE SparePartsOrder SET orderStatus = ? WHERE id = ?"
        update_values = (edit_status, edit_status_id)
        self.cursor.execute(update_query, update_values)
        self.conn.commit()

    def EditSparePart(self, id, name=None, quantity=None, price=None, category=None, description=None):
    # Check if the spare part with the given ID exists
        check_query = "SELECT COUNT(*) FROM SparePart WHERE id = ?"
        check_values = (id,)
        self.cursor.execute(check_query, check_values)
        existing_count = self.cursor.fetchone()[0]

        if existing_count > 0:
            # If the spare part exists, update the specified fields
            update_query = "UPDATE SparePart SET "
            update_values = []

            if name != '':
                update_query += "name = ?, "
                update_values.append(name)

            if quantity != '':
                update_query += "stockQuantity = ?, "
                update_values.append(quantity)

            if price != '':
                update_query += "price = ?, "
                update_values.append(price)

            if category != '':
                update_query += "category = ?, "
                update_values.append(category)

            if description != '':
                update_query += "description = ?, "
                update_values.append(description)

            # Remove the trailing comma and space
            update_query = update_query.rstrip(', ')

            # Add the WHERE clause
            update_query += " WHERE id = ?"
            update_values.append(id)

            # Execute the update query
            self.cursor.execute(update_query, update_values)
            self.conn.commit()

            print(f"Spare part with ID {id} updated successfully.")
        else:
            # If the spare part doesn't exist, you can handle this situation (e.g., show a message)
            print(f"Spare part with ID {id} not found.")


    def getCheckoutDetails(self, participant_id):
        query = """
            SELECT fname, lname, address, email, phoneNo, companyName
            FROM Participant
            WHERE id = ?
        """

        self.cursor.execute(query, (participant_id,))
        result = self.cursor.fetchall()
        return result
    

    def getTotalBill(self, participant_id):
        query = """
            SELECT SUM(S.price * C.quantity) AS totalBill
            FROM Cart C
            JOIN SparePart S ON C.product_id = S.id
            WHERE C.user_id = ?
        """

        self.cursor.execute(query, (participant_id,))
        result = self.cursor.fetchone()

        if result and result[0] is not None:
            totalBill = result[0]
            # print(f"{total_bill}")
            return totalBill
        else:
            return 0  
        
    
    def get_next_order_id(self):
        # Query the maximum orderId from SparePartsOrder
        max_order_query = "SELECT MAX(orderId) FROM SparePartsOrder"
        self.cursor.execute(max_order_query)
        max_order_id = self.cursor.fetchone()[0]

        # If there are no orders yet, start with orderId = 1, otherwise increment the maximum orderId
        return 1 if max_order_id is None else max_order_id + 1


    def checkout(self, participant_id, payment_method):
        # Get cart items
        cart_query = """
            SELECT c.product_id, c.quantity, s.price, s.sellerId
            FROM Cart c
            JOIN SparePart s ON c.product_id = s.id
            WHERE c.user_id = ?
        """
        self.cursor.execute(cart_query, (participant_id,))
        cart_items = self.cursor.fetchall()
        

        # Initialize total bill and order ID
        total_bill = 0
        order_id = self.get_next_order_id()  

        # Loop through cart items and transfer to SparePartsOrder
        for item in cart_items:
            product_id, quantity, price, seller_id = item

            # Calculate total bill for the item
            item_total = quantity * price
            total_bill += item_total
            
            # Insert into SparePartsOrder
            order_query = """
                INSERT INTO SparePartsOrder (orderId, sparePartId, quantity,  totalBill, paymentType, sellerID, buyerID, orderDate, orderStatus)
                VALUES (?, ?, ?, ?, ?, ?, ?, GetDate(), 'Processing')
            """
        
            params = (order_id, product_id, quantity, item_total, payment_method, seller_id, participant_id)
            self.cursor.execute(order_query, params)

            # Subtract quantity from stockQuantity in SparePart
            update_stock_query = """
                UPDATE SparePart
                SET stockQuantity = stockQuantity - ?
                WHERE id = ?
            """
            self.cursor.execute(update_stock_query, (quantity, product_id))

        # Remove items from Cart after successful checkout
        delete_cart_query = "DELETE FROM Cart WHERE user_id = ?"
        self.cursor.execute(delete_cart_query, (participant_id,))

        # Commit the transaction
        self.conn.commit()


            
    def get_spareParts(self):
        query = "SELECT * FROM SparePart"
        self.cursor.execute(query)

        spare_parts_list = []

        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["partID"] = row[0]
            item_dict["name"] = row[1]
            item_dict["description"] = row[2]
            item_dict["category"] = row[3]
            item_dict["price"] = row[4]
            spare_parts_list.append(item_dict)

        return spare_parts_list

    def get_product_details(self, item_id):
        query = f"select * from SparePart where id = '{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["id"] = row[0]
            item_dict["name"] = row[1]
            item_dict["description"] = row[2]
            item_dict["category"] = row[3]
            item_dict["price"] = row[4]
        return item_dict
   
    def find_spareParts(self, string):
        query = f"SELECT * FROM SparePart WHERE name LIKE '%{string}%' OR description LIKE '%{string}%' OR category LIKE '%{string}%' "
        self.cursor.execute(query)
        spare_parts_list = []

        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["partID"] = row[0]
            item_dict["name"] = row[1]
            item_dict["description"] = row[2]
            item_dict["category"] = row[3]
            item_dict["price"] = row[4]
            spare_parts_list.append(item_dict)

        return spare_parts_list
    

    def get_sparePartsReviews(self,productID):
        query = f"SELECT * FROM ReviewTable where spID='{productID}'"
        self.cursor.execute(query)
        review_list = []
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["reviewID"] = row[0]
            item_dict["name"] = row[1]
            item_dict["date"] = row[2]
            item_dict["content"] = row[3]
            item_dict["rating"] = row[4]
            review_list.append(item_dict)

        return review_list

    def add_Review(self, name, message,rating,product_id):
        query = f"insert into ReviewTable (name, date, content,rating,spID) values ('{name}',getdate(), '{message}', '{rating}','{product_id}')"
        self.cursor.execute(query)
        self.conn.commit()

    def add_to_cart(self,participant_id, product_id, quantity):
        user_id = participant_id  # Replace with the actual user ID
        query = "INSERT INTO Cart (user_id, product_id, quantity) VALUES (?, ?, ?)"

        # Execute the query with parameters
        self.cursor.execute(query, (user_id, product_id, quantity))

        # Commit the changes to the database
        self.conn.commit()

    def check_quantity(self,part_id,quantity):
        query = "SELECT * FROM SparePart WHERE id =? AND  stockQuantity>= ? "
        self.cursor.execute(query, (part_id,quantity))
        if self.cursor.rowcount == 0:
            return False
        else:
            return True
        

    def get_mechanics(self):
        query = f"SELECT * FROM Participant WHERE participantType IN ('Mechanic', 'mechanic')"
        self.cursor.execute(query)

        mechanic_list = []

        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["id"] = row[0]
            item_dict["username"] = row[1]
            item_dict["password"] = row[2]
            item_dict["email"] = row[3]
            item_dict["fname"] = row[4]
            item_dict["lname"] = row[5]
            item_dict["address"] = row[6]
            item_dict["phoneNo"] = row[7]
            item_dict["creditcardNo"] = row[8]
            item_dict["participantType"] = row[9]
            item_dict["companyName"] = row[10]
            item_dict["description"] = row[11]
            item_dict["specialization"] = row[12]
            mechanic_list.append(item_dict)

        return mechanic_list


    def find_mechanic(self, string):
        query = f"SELECT * FROM Participant WHERE fname LIKE '%{string}%' OR lname LIKE '%{string}%' OR companyName LIKE '%{string}%' OR description LIKE '%{string}%' OR specialization LIKE '%{string}%'"
        self.cursor.execute(query)
        mechanic_list = []

        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["id"] = row[0]
            item_dict["username"] = row[1]
            item_dict["password"] = row[2]
            item_dict["email"] = row[3]
            item_dict["fname"] = row[4]
            item_dict["lname"] = row[5]
            item_dict["address"] = row[6]
            item_dict["phoneNo"] = row[7]
            item_dict["creditcardNo"] = row[8]
            item_dict["participantType"] = row[9]
            item_dict["companyName"] = row[10]
            item_dict["description"] = row[11]
            item_dict["specialization"] = row[12]
            mechanic_list.append(item_dict)

        return mechanic_list

    def get_mechanic_details(self, mechanic_id):
        query = f"select * from Participant where id = '{mechanic_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["id"] = row[0]
            item_dict["username"] = row[1]
            item_dict["password"] = row[2]
            item_dict["email"] = row[3]
            item_dict["fname"] = row[4]
            item_dict["lname"] = row[5]
            item_dict["address"] = row[6]
            item_dict["phoneNo"] = row[7]
            item_dict["creditcardNo"] = row[8]
            item_dict["participantType"] = row[9]
            item_dict["companyName"] = row[10]
            item_dict["description"] = row[11]
            item_dict["specialization"] = row[12]
        return item_dict


    def get_mechanicReviews(self,mechanicID):
        query = f"SELECT * FROM ReviewTable_M where mechanicID='{mechanicID}'"
        self.cursor.execute(query)

        review_list = []


        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["reviewID"] = row[0]
            item_dict["name"] = row[1]
            item_dict["date"] = row[2]
            item_dict["content"] = row[3]
            item_dict["rating"] = row[4]
            review_list.append(item_dict)

        return review_list

    def addM_Review(self, name, message,rating,mechanic_id):
        query = f"insert into ReviewTable_M (name, date, content,rating,mechanicID) values ('{name}',getdate(), '{message}', '{rating}','{mechanic_id}')"
        self.cursor.execute(query)
        self.conn.commit()


    def get_cart_spareParts(self, participant_id):
        query = """
            SELECT c.user_id, c.product_id, c.quantity, s.id, s.name, s.description, s.category, s.price, s.stockQuantity
            FROM Cart c
            JOIN SparePart s ON c.product_id = s.id
            WHERE c.user_id = ?
        """
        self.cursor.execute(query, (participant_id,))

        spare_parts_list = []

        for row in self.cursor.fetchall():
            item_dict = {
                "user_id": row[0],
                "product_id": row[1],
                "quantity": row[2],
                "id": row[3],
                "name": row[4],
                "description": row[5],
                "category": row[6],
                "price": row[7],
                "stockQuantity": row[8],
            }
            spare_parts_list.append(item_dict)

        return spare_parts_list

    def removefromCart(self,participant_id,part_id):
        query = f"delete from Cart where user_id = '{participant_id}' AND product_id='{part_id}'"
        self.cursor.execute(query)
        self.conn.commit()

    def addPost(self, name, title, description, image, video):
        
        query = "INSERT INTO Posts (name, title, content, datePosted, imageURL, videoURL) VALUES (?, ?, ?, GetDate(), ?, ?)"
        values = (name, title, description, image, video)  

        self.cursor.execute(query, values)
        self.conn.commit()


    def addComment(self, commenter_name, comment_text, post_id):
        

        # Insert the comment data into the Comments table
        query = "INSERT INTO Comments (postID, commenterName, commentText, commentDate) VALUES (?, ?, ?, GetDate())"
        values = (post_id, commenter_name, comment_text)

        self.cursor.execute(query, values)
        self.conn.commit()
        
  
    def getPostsAndComments(self):
        query = """
        SELECT 
            p.postID, p.name, p.title, p.content, p.datePosted, p.imageURL, p.videoURL,
            c.commenterName, c.commentDate, c.commentText
        FROM 
            Posts p
            LEFT JOIN Comments c ON p.postID = c.postID
        ORDER BY 
            p.postID, c.commentID
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        posts_and_comments_dict = {}  # Use a dictionary to store posts by their IDs

        for row in data:
            post_id = row[0]

            # If the post ID is not in the dictionary, add it with an empty list for comments
            if post_id not in posts_and_comments_dict:
                posts_and_comments_dict[post_id] = {
                    'postID': post_id,
                    'name': row[1],
                    'title': row[2],
                    'content': row[3],
                    'datePosted': row[4],
                    'imageURL': row[5],
                    'videoURL': row[6],
                    'comments': []  # Initialize an empty list for comments
                }

            # Add comment to the current post
            comment_data = {
                        'commenter_name': row[7],
                        'datetime_posted': row[8],
                        'message': row[9]
                    }
            posts_and_comments_dict[post_id]['comments'].append(comment_data)

        # Convert the dictionary values to a list
        posts_and_comments = list(posts_and_comments_dict.values())

        return posts_and_comments