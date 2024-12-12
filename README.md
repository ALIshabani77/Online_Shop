

```markdown
# Online Shopping System

A web-based e-commerce platform built using Python, Django, HTML, and CSS. The system allows users to browse and purchase products, manage their accounts, and track their orders.

## Features

- **Product Management**: Browse and purchase products with the ability to specify quantity.
- **Order Management**: Add, edit, and delete products from the shopping cart.
- **Account Management**: Register, login, logout, and edit user profile information.
- **Search and Filtering**: Search products by name or category, and filter results by price, brand, and more.
- **Payment Management**: Enter payment information (credit card number, expiration date, security code) and track order status.
- **Shipping Address Management**: Enter shipping address information (address, city, state, zip code) and track order status.
- **Order Tracking**: View order history, track order status, and receive notifications when orders are shipped or delivered.

## Technical Requirements

- **Python**: 3.8+
- **Django**: 3.2+
- **MySQL**: 8.0+
- **HTML5**
- **CSS3**

## Installation

To run the application locally:

1. Clone the repository:
   
   git clone https://github.com/ALIshabani77/Online-Shop.git
   
2. Navigate to the project directory:
   
   cd online-shopping-system
   
3. Install dependencies:
   
   pip install -r requirements.txt
   
4. Start the server:
   
   python manage.py runserver
   
5. Open the application in your web browser: `http://localhost:8000`

  ```
## Usage

1. **Register** for an account by providing basic information (name, email, password).
2. **Login** to your account using your email and password.
3. **Browse** products and add them to your shopping cart.
4. **Review** and edit your cart as needed.
5. Proceed to **checkout** and enter payment information.
6. Review and confirm your **order**.

## Database Schema

The application uses a MySQL database to store user information, product data, and order details. The database schema includes the following tables:

- `users`: Stores user information (id, name, email, password)
- `products`: Stores product information (id, name, description, price)
- `orders`: Stores order information (id, user_id, product_id, quantity)
- `payments`: Stores payment information (id, order_id, payment_method)
- `shipping_addresses`: Stores shipping address information (id, user_id, address)

## Contributions

If you'd like to contribute to this project or report issues:

1. Fork this repository.
2. Make changes to the codebase.
3. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For more information or inquiries, contact alishabaniara123@example.com
