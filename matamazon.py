# TODO add all imports needed here
import json
import sys
import argparse

class InvalidIdException(Exception):
    pass

class InvalidPriceException(Exception):
    pass

class MatamzonParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write("Usage: python3 matamazon.py -l < matamazon_log > -s < matamazon_system > -o <output_file> -os <out_matamazon_system>\n")
        sys.exit(1)
    
    @staticmethod
    def get_parser():
        parser = MatamzonParser(description='Matamazon System', 
        usage="Usage: python3 matamazon.py -l < matamazon_log > -s < matamazon_system > -o <output_file> -os <out_matamazon_system>")
        parser.add_argument('-l', '--l',type=str, required=True, help='Path to matamazon log file', dest ='l')
        parser.add_argument('-s', '--s', type=str, required=False, help='Path to matamazon system file', dest ='s')
        parser.add_argument('-o', '--o', type=str, required=False, help='Output file path', dest ='o')
        parser.add_argument('-os', '--os', type=str, required=False, help='Output matamazon system file path', dest ='os')
        return parser
        pass

class Person:
    type = "Person"
    def __init__(self, id, name, city, address):
        if not isinstance(id, int) or id < 0:
            raise InvalidIdException(f'{self.type} ID must be a non-negative integer.')
        self.id = id
        self.name = name
        self.city = city
        self.address = address

    pass

class Customer(Person):
    """
    Represents a customer in the Matamazon system.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Customer name.
        - city (str): Customer city.
        - address (str): Customer shipping address.

    Exceptions:
        InvalidIdException: If 'id' is not valid according to the specification.

    Printing:
        Must support printing in the following format (example):
            Customer(id=42, name='Daniel Elgarici', city='Karmiel, address='123 Main Street')
        Exact formatting requirements appear in the assignment PDF.
    """
    # TODO implement this class as instructed
    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.name}', city='{self.city}', address='{self.address}')"

class Supplier(Person):
    """
    Represents a supplier in the Matamazon system.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Supplier name.
        - city (str): Warehouse city (origin city for shipping).
        - address (str): Warehouse address.

    Exceptions:
        InvalidIdException: If 'id' is not valid according to the specification.

    Printing:
        Must support printing in the following format (example):
            Supplier(id=42, name='Yinon Goldshtein', city='Haifa, address='32 David Rose Street')
    """

    # TODO implement this class as instructed
    def __repr__(self):
        return f"Supplier(id={self.id}, name='{self.name}', city='{self.city}', address='{self.address}')"


class Product:
    """
    Represents a product sold on the Matamazon website.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Product name.
        - price (float): Non-negative price.
        - supplier_id (int): ID of the supplier that provides the product.
        - quantity (int): Non-negative quantity in stock.

    Exceptions:
        InvalidIdException:
            - If id/supplier_id/quantity is invalid per specification.
        InvalidPriceException:
            - If price is invalid (e.g., negative).

    Printing:
        Must support printing in the following format (example):
            Product(id=101, name='Harry Potter Cushion', price=29.99, supplier_id=42, quantity=555)
    """

    # TODO implement this class as instructed
    def __init__(self, id, name, price, supplier_id, quantity):
        if not isinstance(id, int) or id < 0:
            raise InvalidIdException('Product ID must be a non-negative integer.')
        if not isinstance(price, (int, float)) or price < 0:
            raise InvalidPriceException('Product price must be a non-negative number.')
        if not isinstance(supplier_id, int) or supplier_id < 0:
            raise InvalidIdException('Product supplier ID must be a non-negative integer.')
        self.id = id
        self.name = name
        self.price = price
        self.supplier_id = supplier_id
        self.quantity = quantity  
    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, supplier_id={self.supplier_id}, quantity={self.quantity})"  
    def __lt__(self, other):
        return self.price < other.price
    pass


class Order:
    """
    Represents a placed order.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier (assigned by the system).
        - customer_id (int): ID of the customer who placed the order.
        - product_id (int): ID of the ordered product.
        - quantity (int): Ordered quantity (non-negative integer).
        - total_price (float): Total price for the order (non-negative).

    Exceptions:
        InvalidIdException:
            - If one of the ID fields is invalid.
        InvalidPriceException:
            - If total_price is invalid.

    Printing:
        Must support printing in the following format (example):
            Order(id=1, customer_id=42, product_id=101, quantity=10, total_price=299.9)

    """

    # TODO implement this class as instructed
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        if not isinstance(id, int) or id < 0:
            raise InvalidIdException('Order ID must be a non-negative integer.')
        if not isinstance(customer_id, int) or customer_id < 0:
            raise InvalidIdException('Customer ID must be a non-negative integer.')
        if not isinstance(product_id, int) or product_id < 0:
            raise InvalidIdException('Product ID must be a non-negative integer.')
        if not isinstance(total_price, (int, float)) or total_price < 0:
            raise InvalidPriceException('Total price must be a non-negative number.')
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
    def __repr__(self):
        return f"Order(id={self.id}, customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity}, total_price={self.total_price})"
    pass


class MatamazonSystem:
    """
    Main system class that stores and manages customers, suppliers, products and orders.

    The system must support:
        - Registering customers/suppliers (with unique IDs across both types).
        - Adding/updating products (must validate supplier existence).
        - Placing orders (validate product existence and stock).
        - Removing objects by ID and type (with dependency constraints).
        - Searching products by name/query and optional max price.
        - Exporting system state to a text file (customers/suppliers/products only).
        - Exporting orders to JSON grouped by supplier origin city.

    Notes:
        - The specification does not require specific internal fields. Any data structures are allowed,
          as long as the behaviors match the spec.
        - A parameterless constructor is required.
    """

    def __init__(self):
        """
        Initialize an empty Matamazon system.

        Requirements:
            - Must be parameterless.
            - Internal collections may be chosen freely (dict/list, etc.).
        """
        # TODO implement this method if needed
        self.customers = {}
        self.suppliers = {}
        self.products = {}
        self.orders = {}
        self.next_order_id = 1 
        pass

    def register_entity(self, entity, is_customer):
        """
        Register a Customer or Supplier in the system.

        Args:
            entity: A Customer or Supplier object.
            is_customer (bool): True if entity is Customer, False if entity is Supplier.

        Raises:
            InvalidIdException:
                - If the entity ID is invalid.
                - If the entity ID already exists in the system (note: IDs must be unique across
                  customers AND suppliers).
        """
        # TODO implement this method as instructed

        if is_customer:
            if entity.id in self.customers.keys():
                raise InvalidIdException('Customer ID already exists in the system.')
            self.customers[entity.id] = entity
        else:
            if entity.id in self.suppliers.keys():
                raise InvalidIdException('Supplier ID already exists in the system.')
            self.suppliers[entity.id] = entity
        pass

    def add_or_update_product(self, product):
        """
        Add a new product or update an existing product.

        Behavior:
            - If product does not exist in system: add it.
            - If product exists:
                - It must belong to the same supplier as the existing one (same supplier_id),
                  otherwise raise InvalidIdException.
                - Update the stored product's fields according to the new product.

        Args:
            product: A Product object.

        Raises:
            InvalidIdException:
                - If the supplier_id does not exist in the system.
                - If attempting to update a product but supplier_id differs from the existing product.
        """
        # TODO implement this method as instructed
        if product.supplier_id not in self.suppliers.keys():
            raise InvalidIdException('Supplier ID does not exist in the system.')
        if product.id in self.products.keys() :
            if product.supplier_id != self.products[product.id].supplier_id:
                raise InvalidIdException('Supplier ID does not match existing product supplier ID.')
            else :
                self.products[product.id] = product
        else :
            self.products[product.id] = product
        pass

    def place_order(self, customer_id, product_id, quantity=1):
        """
        Place an order for a product by a customer.

        Args:
            customer_id (int): Customer ID.
            product_id (int): Product ID.
            quantity (int, optional): Quantity to order. Defaults to 1.

        Returns:
            str: Status message according to specification:
                - "The order has been accepted in the system"
                - "The product does not exist in the system"
                - "The quantity requested for this product is greater than the quantity in stock"

        Behavior:
            - If product does not exist: return the relevant message.
            - If quantity requested > stock: return the relevant message.
            - Otherwise:
                - Decrease product stock by quantity.
                - Create a new Order with an auto-incremented system ID (starting at 1).
                - Store the order in the system.
                - Return success message.

        Notes:
            - The specification assumes quantity is an integer.
        """
        # TODO implement this method as instructed
        if customer_id not in self.customers.keys():
            raise InvalidIdException('Customer ID does not exist in the system.')
        if product_id not in self.products.keys():
            return "The product does not exist in the system"
        product = self.products[product_id]
        if quantity > product.quantity:
            return "The quantity requested for this product is greater than the quantity in stock"
        product.quantity -= quantity
        total_price = product.price * quantity
        order = Order(self.next_order_id, customer_id, product_id, quantity, total_price)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        return "The order has been accepted in the system"

    def remove_object(self, _id, class_type):
        """
        Remove an object from the system by ID and type.

        Args:
            _id (int): Object ID to remove.
            class_type (str): One of: "Customer", "Supplier", "Product", "Order"
                              (exact casing/spelling per assignment).

        Returns:
            int | None:
                - If removing an Order: return the ordered quantity of that order (to restore stock).
                - Otherwise: no return value required.

        Raises:
            InvalidIdException:
                - If _id is not a valid non-negative integer.
                - If attempting to remove a Customer/Supplier/Product that still has dependent orders
                  in the system (i.e., orders that were not removed).
                - Additional InvalidIdException conditions as required by specification.
        """
        # TODO implement this method as instructed
        class_type = class_type.strip().lower()
        if class_type == "order":
            if _id not in self.orders.keys():
                raise InvalidIdException('Order ID does not exist.')
            order = self.orders.pop(_id)
            product = self.products[order.product_id]
            product.quantity += order.quantity
            return order.quantity
        elif class_type == "customer":
            if _id not in self.customers.keys():
                raise InvalidIdException('Customer ID does not exist.')
            for order in self.orders.values():
                if order.customer_id == _id:
                    raise InvalidIdException('Cannot remove customer with existing orders.')
            del self.customers[_id]
        elif class_type == "supplier":
            if _id not in self.suppliers.keys():
                raise InvalidIdException('Supplier ID does not exist.')
            for order in self.orders.values():
                product = self.products[order.product_id]
                if product.supplier_id == _id:
                    raise InvalidIdException('Cannot remove supplier with existing orders.')
            del self.suppliers[_id]
        elif class_type == "product":
            if _id not in self.products.keys():
                raise InvalidIdException('Product ID does not exist.')
            for order in self.orders.values():
                if order.product_id == _id:
                    raise InvalidIdException('Cannot remove product with existing orders.')
            del self.products[_id]
        else:
            raise InvalidIdException('Invalid class type for removal.')
        pass

    def search_products(self, query, max_price=None):
        """
        Search products by query in the product name, and optionally filter by max_price.

        Args:
            query (str): Product name or part of product name.
            max_price (float, optional): If provided, only return products with price <= max_price.

        Returns:
            list[Product]:
                - Products that match the query and have quantity != 0,
                - Sorted by ascending price.
                - If no matching products exist, return an empty list.
        """
        # TODO implement this method as instructed
        sorted = []
        for product in self.products.values():
            if query.lower() in product.name.lower() and product.quantity != 0:
                if max_price is None or product.price <= max_price:
                    sorted.append(product)
        sorted.sort()
        return sorted

    def export_system_to_file(self, path):
        """
        Export system state (customers, suppliers, products) to a text file.

        Args:
            path (str): Output file path.

        Behavior:
            - Write each object on its own line, using the object's print/str representation.
            - Orders must NOT be included.
            - No constraint on the ordering of objects in the output.

        Raises:
            OSError (or any file-open exception): Must be propagated to the caller.
        """
        # TODO implement this method as instructed
        try:
            if path is sys.stdout:
                for customer in self.customers.values():
                    print(repr(customer))
                for supplier in self.suppliers.values():
                    print(repr(supplier))
                for product in self.products.values():
                    print(repr(product))
            else:
                with open(path, 'w') as f:
                    for customer in self.customers.values():
                        f.write(repr(customer) + '\n')
                    for supplier in self.suppliers.values():
                        f.write(repr(supplier) + '\n')
                    for product in self.products.values():
                        f.write(repr(product) + '\n')
        except OSError as e:
            raise e
        pass
    
    def export_orders(self, out_file):
        """
        Export orders in JSON format grouped by origin city.

        Args:
            out_file (file-like)

        Behavior (per specification):
            - Produce a JSON object where:
                - Keys: origin city (supplier city) for each order.
                - Values: list of strings representing orders (format as specified in section 4.1.4).
            - Order lists can be in any order.
            - No requirement on key ordering.

        Raises:
            Any exception during writing: Must be propagated to the caller.

        Notes:
            - The order origin city is the supplier city of the ordered product.
        """
        # TODO implement this method as instructed
        try:
            orders_by_city = {}
            for order in self.orders.values():
                # Extract city via product -> supplier
                product = self.products[order.product_id]
                supplier = self.suppliers[product.supplier_id]
                city = supplier.city
            
                # Format order as string using repr()
                order_str = repr(order)
            
                if city not in orders_by_city:
                    orders_by_city[city] = []
                orders_by_city[city].append(order_str)
        
            # Write the dictionary directly to the file-like object
            json.dump(orders_by_city, out_file, indent=4)
        except Exception as e:
            raise e
        pass

def load_system_from_file(path):
    """
    Load a MatamazonSystem from an input file.

    Args:
        path (str): Path to a text file containing customers, suppliers and products.

    Returns:
        MatamazonSystem: Initialized system with the data found in the file.

    Behavior:
        - The file lines contain objects in the format produced by export_system_to_file (section 4.2).
        - Lines may appear in any order (e.g., product lines can appear before supplier lines).
        - Illegal lines may be ignored.
        - If an exception occurs during the creation of any required object due to invalid data,
          the function should stop and propagate the exception (as specified).

    Notes:
        - The assignment hints that eval() may be used.
    """
    # TODO implement this function as instructed
    system = MatamazonSystem()
    
    suppliers = []
    products = []
    customers = []

    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            
            obj = eval(line)

            if line.startswith("Supplier"):
                suppliers.append(obj)
            elif line.startswith("Product"):
                products.append(obj)
            elif line.startswith("Customer"):
                customers.append(obj)

    # Now add them to the system in the correct order
    for supplier in suppliers:
        system.register_entity(supplier, is_customer=False)
    for product in products:
        system.add_or_update_product(product)
    for customer in customers:
        system.register_entity(customer, is_customer=True)
    return system
    pass

# TODO all the main part here

def apply_register(system, line):
    parts = line.strip().split()
    entity_type = parts[1].strip().capitalize()
    id = int(parts[2].strip())
    name = parts[3].strip().replace("_", " ")
    city = parts[4].strip().replace("_", " ")
    address = parts[5].strip().replace("_", " ")
    if entity_type == "Customer":
        customer = Customer(id, name, city, address)
        system.register_entity(customer, True)
    elif entity_type == "Supplier":
        supplier = Supplier(id, name, city, address)
        system.register_entity(supplier, False)
    pass

def apply_add(system, line):
    parts = line.strip().split()
    id = parts[1].strip()
    name = parts[2].strip().replace("_", " ")
    price = parts[3].strip()
    supplier_id = parts[4].strip()
    quantity = parts[5].strip()
    product = Product(int(id), name, float(price), int(supplier_id), int(quantity))
    system.add_or_update_product(product)
    pass

def apply_order(system, line):
    parts = line.strip().split()
    customer_id = parts[1].strip()
    product_id = parts[2].strip()
    if len(parts) > 3:
        quantity = parts[3].strip()
    else:
        quantity = 1
    system.place_order(int(customer_id), int(product_id), int(quantity))
    pass

def apply_remove(system, line):
    parts = line.strip().split()
    class_type = parts[1].strip()
    id = parts[2].strip()
    system.remove_object(int(id), class_type)
    pass

def apply_search(system, line):
    parts = line.strip().split()
    query = parts[1].strip()
    if len(parts) > 2:
        max_price = float(parts[2].strip())
    else:
        max_price = None
    results = system.search_products(query, max_price)
    print(results)
    pass

SUCCESS = 0
FAILED = 1

def __main__():
    try:    
        parser = MatamzonParser.get_parser()
        args = parser.parse_args(sys.argv[1:])
        if args.s is not None:
            matamazon_system = load_system_from_file(args.s)
        else:
            matamazon_system = MatamazonSystem()
        try:    
            with open(args.l, 'r') as log_file:
                for line in log_file:
                
                    if line.startswith("register"):               
                        apply_register(matamazon_system, line)
                    elif line.startswith("add") or line.startswith("update"):
                        apply_add(matamazon_system, line)
                    elif line.startswith("order"):
                        apply_order(matamazon_system, line)
                    elif line.startswith("remove"):
                        apply_remove(matamazon_system, line)
                    elif line.startswith("search"):
                        apply_search(matamazon_system, line)
        except (FileNotFoundError, IOError):
            print("The matamazon script has encountered an error", file=sys.stdout)
            print("The matamazon script has encountered an error", file=sys.stderr)
            sys.exit(SUCCESS)
        if args.o is not None:
            with open(args.o, 'w') as f:
                matamazon_system.export_orders(f)
        else:
            matamazon_system.export_orders(sys.stdout)
        if args.os is not None:
            matamazon_system.export_system_to_file(args.os)
        else:
            print(matamazon_system, file=sys.stdout)
        return SUCCESS
    except SystemExit as e:
        if e.code == 0:
            sys.exit(0)
        sys.exit(FAILED)
    except Exception:
        print("The matamazon script has encountered an error", file=sys.stderr)
        print("The matamazon script has encountered an error", file=sys.stdout)                
        sys.exit(SUCCESS)
if __name__ == "__main__":
    __main__()