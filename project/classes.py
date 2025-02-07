
from flask import Flask, render_template, request, redirect, url_for
from db import ItemDatabase

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('indexbefore.html')

@app.route("/indexbefore.html")
def index2():
    return render_template('indexbefore.html')

@app.route("/indexafter.html/<int:participant_id>")
def index3(participant_id):
    return render_template('indexafter.html', participant_id=participant_id)


class Participant:
    def __init__(self,participant_id=None, username=None, password=None, email=None, first_name=None, last_name=None, address=None, contact_info=None, credit_card_info=None):
        print("Participant object created")

       
    @app.route("/createAccount", methods = ['GET', 'POST'])
    def createAccount():
        if(request.method=='POST'):
            firstName = request.form.get('firstName')
            lastName = request.form.get('lastName')
            username = request.form.get('userName')
            creditCardNo = request.form.get('creditCardNo')
            address = request.form.get('address')
            phone = request.form.get('phone')
            email = request.form.get('email')
            password = request.form.get('password')
            participantType = request.form.get('participantType')

            if participantType == 'user':
                participantType = 'user'
                companyName = None
                description = None
                specialization = None

            elif participantType == 'mechanic':
                participantType = 'mechanic'
                companyName = request.form.get('companyName')
                description = request.form.get('description')
                specialization = request.form.get('specialization')
                
            elif participantType == 'seller':
                participantType = 'seller'
                companyName = request.form.get('companyName')
                description = request.form.get('description')
                specialization = None
                

            entry = ItemDatabase()
            entry.add_account(username, password, email, firstName, lastName, address, phone, creditCardNo, companyName, description, specialization, participantType)

            return render_template('accountCreated.html')
            
        return render_template('createAccount.html')
            
    @staticmethod
    @app.route("/login.html", methods = ['GET', 'POST'])
    def login():
        if(request.method=='POST'  and 'login' in request.form):
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
           
            entry = ItemDatabase()
            if entry.login(username, email, password):
                # Successful login
                #get participant id
                ID=entry.get_ParticipantID(username, email, password)
                return redirect(url_for('index3', participant_id=ID))

        elif(request.method=='POST'  and 'createAccount' in request.form):
            return render_template('createAccount.html')
        

        # Render the login template with the login_result
        return render_template('login.html')
    
    @app.route("/login1.html", methods = ['GET', 'POST'])
    def forgot_password():
        if(request.method=='POST'):
            email = request.form.get('email')
            password = request.form.get('password')
           
            entry = ItemDatabase()
            entry.reset_password(email, password)
            return redirect(url_for('login'))

        # Render the login template with the login_result
        return render_template('login1.html')

    @app.route('/participant_profile/<int:participant_id>')
    def participant_profile(participant_id):
        print(f"id={participant_id}")
        entry = ItemDatabase()
        participant_type = entry.getParticipantType(participant_id)
        print(f"type={participant_type}")
        if(participant_type == 'seller'):
            return Seller.sellerPage(participant_id)
        elif(participant_type == 'user'):
            return User.userPage(participant_id)
        elif(participant_type == 'mechanic'):
            return Mechanic.mechanicPage(participant_id)


class Buyer:
    def __init__(self):
        self.orderlist = []
        self.postlist = []
        self.tutoriallist = []

    
    @app.route("/cart/<int:participant_id>")
    def view_cart(participant_id):
        entry = ItemDatabase()
        #get all spare parts in cart
        spare_parts = entry.get_cart_spareParts(participant_id)
        return render_template('cart.html', products=spare_parts,participant_id=participant_id)


    @app.route("/remove_product/<int:participant_id>/<int:part_id>")
    def manageCart(participant_id,part_id):
        entry = ItemDatabase()
        print(f"partid={part_id}")
        entry.removefromCart(participant_id,part_id)
        spare_parts = entry.get_cart_spareParts(participant_id)
        return render_template('cart.html', products=spare_parts,participant_id=participant_id)


    @app.route("/checkout/<int:participant_id>", methods = ['GET', 'POST'])
    def checkout(participant_id):
        entry = ItemDatabase()
        if(entry.getParticipantType(participant_id)!='seller'):
            checkout_details = entry.getCheckoutDetails(participant_id)
            totalBill = entry.getTotalBill(participant_id)
            deliveryCharges = 200
            total = totalBill + deliveryCharges
            if(request.method=='POST'):
                payment_method = request.form.get('payment_method')
                # print(f"payment={payment_method}")
                entry.checkout(participant_id, payment_method)
                return redirect(url_for('index3', participant_id=participant_id))
            else:
                return render_template('checkout.html', participant_id=participant_id, checkout_details=checkout_details, totalBill=totalBill, total=total, deliveryCharges=deliveryCharges)
        else:
            return render_template('cart.html',participant_id=participant_id)
    
class Seller(Participant):
    def __init__(self, participant_id=None, username=None, password=None, email=None, first_name=None, last_name=None, address=None, contact_info=None, credit_card_info=None, company_name=None, description=None):
        super().__init__(participant_id, username, password, email, first_name, last_name, address, contact_info, credit_card_info)
        self.company_name = company_name
        self.description = description
        self.spare_parts_to_sell = []

    @app.route("/sellerProfile/<int:participant_id>", methods=['GET', 'POST'])
    def sellerPage(participant_id):
        entry = ItemDatabase()
        if request.method == 'POST' and 'submit_profile_changes' in request.form:
            new_firstName = request.form.get('new_firstName')
            new_lastName = request.form.get('new_lastName')
            new_email = request.form.get('new_email')
            new_description = request.form.get('new_description')
            new_company = request.form.get('new_company')
            new_address = request.form.get('new_address')
            new_phone = request.form.get('new_phone')
            new_creditCardNo = request.form.get('new_creditCardNo')
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            renew_password = request.form.get('renew_password')
            entry.update_info_seller(new_firstName, new_lastName, new_email, new_description, new_company, new_address, new_phone, new_creditCardNo, current_password, new_password, renew_password, participant_id)

        elif request.method == 'POST' and 'submit_spare_part' in request.form:
            add_name = request.form.get('spare_part_name')
            add_quantity = request.form.get('sp_quantity')
            add_price = request.form.get('sp_price')
            add_category = request.form.get('sp_category')
            add_description = request.form.get('sp_description')
            entry.addSparePart(add_name, add_quantity, add_price, add_category, add_description, participant_id)

        elif request.method == 'POST' and 'edit_spare_part' in request.form:
            edit_id = request.form.get('edit_spare_part_id')
            add_name = request.form.get('edit_spare_part_name')
            add_quantity = request.form.get('edit_sp_quantity')
            add_price = request.form.get('edit_sp_price')
            add_category = request.form.get('edit_sp_category')
            add_description = request.form.get('edit_sp_description')
            entry.EditSparePart(edit_id, add_name, add_quantity, add_price, add_category, add_description)
        
        elif request.method == 'POST' and 'edit_order_status' in request.form:
            edit_status_id = request.form.get('edit_order_status_id')
            edit_status = request.form.get('edit_status')
            entry.EditOrderStatus(edit_status_id, edit_status)

        data = entry.get_info(participant_id)
        # print({data})
        if data:
            email, fname, lname, address, phoneNo, creditCardNo, companyName, description, specialization = data
            full_name = f"{fname} {lname}"
        else:
            full_name = "No name available."
            description = "No description available."

        spare_parts_result = entry.getSellerSpareParts(participant_id)
        # print(spare_parts_result)
        # Convert spare parts result to a list
        spare_parts_list = [
            {'id': part[0], 'name': part[1], 'quantity': part[5], 'price': part[4], 'category': part[3], 'description': part[2]}
            for part in spare_parts_result
        ]

        spare_parts_orders_result = entry.getSellerOrders(participant_id)
        # Convert spare parts result to a list
        spare_parts__orders_list = [
            {
                'id': part[0],             # sparePartId from SparePartOrder
                'name': part[1],           # partName from SparePart
                'quantity': part[2],       # quantity from SparePartOrder
                'order_status': part[3],   # orderStatus from SparePartOrder
                'order_date': part[4],     # orderDate from SparePartOrder
                'total_bill': part[5],      # totalBill from SparePartOrder
                'payment_method': part[6]  # payment method
            }
            for part in spare_parts_orders_result
        ]

        return render_template('sellerProfile.html', participant_id=participant_id, full_name=full_name, companyName=companyName, description=description, address=address,
        phoneNo=phoneNo, creditCardNo=creditCardNo, email=email, fname=fname, lname=lname, spare_parts=spare_parts_list, specialization=specialization,
        spare_parts_orders=spare_parts__orders_list)
    



class User(Buyer, Participant):
    def __init__(self, participant_id, username, password, email, first_name, last_name, address, contact_info, credit_card_info):
        # Call constructors of both parent classes
        Buyer.__init__(self)
        Participant.__init__(self, participant_id, username, password, email, first_name, last_name, address, contact_info, credit_card_info)

    @app.route('/userProfile/<int:participant_id>', methods=['GET', 'POST'])
    def userPage(participant_id):
        entry = ItemDatabase()
        if request.method == 'POST' and 'submit_profile_changes' in request.form:
            new_firstName = request.form.get('new_firstName')
            new_lastName = request.form.get('new_lastName')
            new_email = request.form.get('new_email')
            new_address = request.form.get('new_address')
            new_phone = request.form.get('new_phone')
            new_creditCardNo = request.form.get('new_creditCardNo')
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            renew_password = request.form.get('renew_password')
            entry.update_info_user(new_firstName, new_lastName, new_email, new_address, new_phone, new_creditCardNo, current_password, new_password, renew_password, participant_id)

        elif request.method == 'POST' and 'cancel_order' in request.form:
            cancel_order_id = request.form.get('cancel_order_id')
            entry.cancelOrder(cancel_order_id)


        data = entry.get_info(participant_id)
        # print({data})
        if data:
            email, fname, lname, address, phoneNo, creditCardNo, companyName, description, specialization = data
            full_name = f"{fname} {lname}"
        else:
            full_name = "No name available."
            description = "No description available."

        spare_parts_orders_result = entry.getBuyerOrders(participant_id)
        # Convert spare parts result to a list
        spare_parts__orders_list = [
            {
                'id': part[0],             # sparePartId from SparePartOrder
                'name': part[1],           # partName from SparePart
                'quantity': part[2],       # quantity from SparePartOrder
                'order_status': part[3],   # orderStatus from SparePartOrder
                'order_date': part[4],     # orderDate from SparePartOrder
                'total_bill': part[5]      # totalBill from SparePartOrder
            }
            for part in spare_parts_orders_result
        ]


        return render_template('userProfile.html', participant_id=participant_id, full_name=full_name, companyName=companyName, description=description, address=address,
        phoneNo=phoneNo, creditCardNo=creditCardNo, email=email, fname=fname, lname=lname, spare_parts_orders=spare_parts__orders_list, specialization=specialization)
    



class Mechanic(Buyer, Participant):
    def __init__(self, participant_id, username, password, email, first_name, last_name, address, contact_info, credit_card_info, company_name, description, specialization):
        # Call constructors of both parent classes
        Buyer.__init__(self)
        Participant.__init__(self, participant_id, username, password, email, first_name, last_name, address, contact_info, credit_card_info)
        
        self.companyName = company_name
        self.description = description
        self.specialization = specialization
        self.reviewList = []

    @app.route("/mechanicProfile/<int:participant_id>", methods=['GET', 'POST'])
    def mechanicPage(participant_id):
        entry = ItemDatabase()
        if request.method == 'POST' and 'submit_profile_changes' in request.form:
            new_firstName = request.form.get('new_firstName')
            new_lastName = request.form.get('new_lastName')
            new_email = request.form.get('new_email')
            new_description = request.form.get('new_description')
            new_specialization = request.form.get('new_specialization')
            new_company = request.form.get('new_company')
            new_address = request.form.get('new_address')
            new_phone = request.form.get('new_phone')
            new_creditCardNo = request.form.get('new_creditCardNo')
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            renew_password = request.form.get('renew_password')
            entry.update_info_mechanic(new_firstName, new_lastName, new_email, new_description, new_specialization, new_company, new_address, new_phone, new_creditCardNo, current_password, new_password, renew_password, participant_id)
        
        elif request.method == 'POST' and 'cancel_order' in request.form:
            cancel_order_id = request.form.get('cancel_order_id')
            entry.cancelOrder(cancel_order_id)

        data = entry.get_info(participant_id)
        # print({data})
        if data:
            email, fname, lname, address, phoneNo, creditCardNo, companyName, description, specialization = data
            full_name = f"{fname} {lname}"
        else:
            full_name = "No name available."
            description = "No description available."

        spare_parts_orders_result = entry.getBuyerOrders(participant_id)
        # Convert spare parts result to a list
        spare_parts__orders_list = [
            {
                'id': part[0],             # sparePartId from SparePartOrder
                'name': part[1],           # partName from SparePart
                'quantity': part[2],       # quantity from SparePartOrder
                'order_status': part[3],   # orderStatus from SparePartOrder
                'order_date': part[4],     # orderDate from SparePartOrder
                'total_bill': part[5]      # totalBill from SparePartOrder
            }
            for part in spare_parts_orders_result
        ]
        return render_template('mechanicProfile.html', participant_id=participant_id, full_name=full_name, companyName=companyName, description=description, address=address,
        phoneNo=phoneNo, creditCardNo=creditCardNo, email=email, fname=fname, lname=lname, spare_parts_orders=spare_parts__orders_list, specialization=specialization)
    
    @app.route("/services.html/<int:participant_id>")
    def displayMechanics(participant_id):
        entry = ItemDatabase()
        #get all mechanics
        mechanics = entry.get_mechanics()
        return render_template('services.html', services=mechanics,participant_id=participant_id)

    @app.route("/search_mechanic/<int:participant_id>",methods=["POST"])
    def search_mechanic(participant_id):
        entry = ItemDatabase()
        #search the spare part from db that contains the word or letter entered in query field
        query = request.form.get('query')
        mechanics = entry.find_mechanic(query)
        return render_template('services.html', services=mechanics,participant_id=participant_id)

    @app.route("/mechanic_details/reviews/<int:participant_id>/<int:mechanic_id>", methods=['GET', 'POST'])
    def mechanic_details(mechanic_id,participant_id):
        entry = ItemDatabase()
        mechanic_details = entry.get_mechanic_details(mechanic_id)
        _review = Review(1, ' ')
        mechanic_reviews = _review.displayMreview(mechanic_id)

        if request.method == 'POST':
            name = request.form.get('name')
            content = request.form.get('message')
            rating = request.form.get('rating')
            # Save the review in the database
            _review.saveM_Review(name, content, rating, mechanic_id)
            # Get all the reviews again, including the new one
            mechanic_reviews = _review.displayMreview(mechanic_id)
            #flash('Review submitted successfully!', 'success')

        return render_template("mechanic_detail.html", mechanic_details=mechanic_details, mechanic_reviews=mechanic_reviews,participant_id=participant_id,mechanic_id=mechanic_id)


class Forum:
    def init(self, id):
        self.id = id
    
    @app.route("/forum.html/<int:participant_id>", methods = ['GET', 'POST'])
    def forumPost(participant_id):
        entry = ItemDatabase()
        #Add post
        if(request.method=='POST' and 'submit_post' in request.form):
            name = request.form.get('name')
            title = request.form.get('title')
            description = request.form.get('description')
            image = request.form.get('image')
            video = request.form.get('video')
            
            entry.addPost(name, title, description, image, video)
      
        #get posts with comments
        posts_and_comments = entry.getPostsAndComments()
        return render_template('forum.html', participant_id=participant_id, posts_and_comments=posts_and_comments)


    @app.route("/forum.html/<int:participant_id>/<int:post_id>", methods = ['GET', 'POST'])
    def forumComment(participant_id, post_id):
        entry = ItemDatabase()
        if(request.method == 'POST' and 'post_comment' in request.form):
            commenter_name = request.form.get('commenter_name')
            comment_text = request.form.get('comment_text')

            entry.addComment(commenter_name, comment_text, post_id)

        #get posts with comments
        posts_and_comments = entry.getPostsAndComments()

        return render_template('forum.html', participant_id=participant_id, posts_and_comments=posts_and_comments)
    

class Review:
    def __init__(self, reviewID, content):
        self.reviewID = reviewID
        self.content = content


    def displaySPreview(self,part_id):
        entry = ItemDatabase()
        reviews = entry.get_sparePartsReviews(part_id)
        return reviews

    def save_Review(self,name,content,rating,part_id):
        entry = ItemDatabase()
        entry.add_Review(name, content, rating,part_id)


    #For Mechanics
    def displayMreview(self,mechanic_id):
        entry = ItemDatabase()
        reviews = entry.get_mechanicReviews(mechanic_id)
        return reviews

    def saveM_Review(self,name,content,rating,mechanic_id):
        entry = ItemDatabase()
        entry.addM_Review(name, content, rating,mechanic_id)



class SparePart:
    def __init__(self, partID, name, description, category, price, stockQuantity):
        self.partID = partID
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.stockQuantity = stockQuantity
        self.carSparePart = []  
        self.reviewList = []


    @app.route("/product/<int:participant_id>")
    def displaySpareParts(participant_id):
        entry = ItemDatabase()
        #get all spare parts
        spare_parts = entry.get_spareParts()
        return render_template('product.html', products=spare_parts,participant_id=participant_id)
    
    @app.route("/search/<int:participant_id>",methods=["POST"])
    def search_products(participant_id):
        entry = ItemDatabase()
        #search the spare part from db that contains the word or letter entered in query field
        query = request.form.get('query')
        spare_parts = entry.find_spareParts(query)
        return render_template('product.html', products=spare_parts,participant_id=participant_id)
    
    @app.route("/product_details/reviews/<int:participant_id>/<int:part_id>", methods=['GET', 'POST'])
    def product_details(participant_id,part_id):
        entry = ItemDatabase()
        product_details = entry.get_product_details(part_id)
        _review = Review(1, ' ')
        product_reviews = _review.displaySPreview(part_id)

        if request.method == 'POST':
            # Check if the form is submitted for adding to the cart
            if 'add_to_cart' in request.form:
                # Process the form data for adding to the cart
                quantity =request.form.get('quantity')
                #check if quantity is less than or equal to available stock
                if entry.check_quantity(part_id,quantity) and entry.getParticipantType(participant_id)!='seller':
                    # Save the product to the cart in your database
                    entry.add_to_cart(participant_id,part_id,quantity)
       
            # Check if the form is submitted for submitting a review
            elif 'submit_review' in request.form:
                name = request.form.get('name')
                content = request.form.get('message')
                rating = request.form.get('rating')
                # Save the review in the database
                _review.save_Review(name, content, rating, part_id)
                # Get all the reviews again, including the new one
                product_reviews = _review.displaySPreview(part_id)
                #flash('Review submitted successfully!', 'success')

        return render_template("detail.html", product_details=product_details, product_reviews=product_reviews,participant_id=participant_id,part_id=part_id)

   
app.run()
