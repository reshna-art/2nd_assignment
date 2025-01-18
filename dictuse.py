from collections import defaultdict

def create_inventory_tracker():
    """
    Create an inventory tracker using defaultdict where each product
    is stored under its category.
    
    Returns:
        dict: An inventory tracker.
    """
    return defaultdict(list)

def add_product(inventory, category, product):
    """
    Add a product to a category in the inventory.
    
    Args:
        inventory (defaultdict): The inventory tracker.
        category (str): The category to which the product belongs.
        product (str): The product to add.
    """
    inventory[category].append(product)
    print(f"Added {product} to category {category}.")

def remove_product(inventory, category, product):
    """
    Remove a product from a category in the inventory.
    
    Args:
        inventory (defaultdict): The inventory tracker.
        category (str): The category from which to remove the product.
        product (str): The product to remove.
    """
    if category in inventory and product in inventory[category]:
        inventory[category].remove(product)
        print(f"Removed {product} from category {category}.")
        # Clean up the category if empty
        if not inventory[category]:
            del inventory[category]
    else:
        print(f"{product} not found in category {category}.")

def display_inventory(inventory):
    """
    Display the entire inventory.
    
    Args:
        inventory (defaultdict): The inventory tracker.
    """
    if not inventory:
        print("Inventory is empty.")
    else:
        for category, products in inventory.items():
            print(f"Category: {category}")
            for product in products:
                print(f"  - {product}")

def get_products_by_category(inventory, category):
    """
    Get all products in a specific category.
    
    Args:
        inventory (defaultdict): The inventory tracker.
        category (str): The category to retrieve products from.
    
    Returns:
        list: The list of products in the category.
    """
    return inventory.get(category, [])

# Example usage
if __name__ == "__main__":
    inventory = create_inventory_tracker()
    
    # Adding products
    add_product(inventory, "Fruits", "Apple")
    add_product(inventory, "Fruits", "Banana")
    add_product(inventory, "Vegetables", "Carrot")
    add_product(inventory, "Beverages", "Juice")

    # Display inventory
    print("\nCurrent Inventory:")
    display_inventory(inventory)

    # Remove a product
    remove_product(inventory, "Fruits", "Apple")

    # Display inventory after removal
    print("\nUpdated Inventory:")
    display_inventory(inventory)

    # Get products by category
    print("\nProducts in Beverages:", get_products_by_category(inventory, "Beverages"))
