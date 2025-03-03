#!/usr/bin/env python3
"""
Supply Chain Dashboard - Interview Task

This file contains the starter code for a technical interview task.
The candidate is expected to implement the process_supply_chain_data function
according to the requirements specified in the comments.

Time Allocation: 15 minutes
"""

import json
import os

def process_supply_chain_data(orders_file, inventory_file):
    """
    TASK: Process supply chain data to identify unfulfilled orders and calculate missing quantities.
    
    Your function should:
    1. Parse the JSON data from the provided files
    2. Identify pending orders that cannot be fulfilled due to insufficient inventory
    3. Calculate the total missing quantity across all unfulfilled orders
    4. Return a JSON summary of unfulfilled orders and the total missing quantity
    
    Args:
        orders_file (str): Path to the JSON file containing orders data
        inventory_file (str): Path to the JSON file containing inventory data
        
    Returns:
        dict: JSON summary of unfulfilled orders and total missing quantity
        
    Expected Output Format:
    {
        "unfulfilled_orders": [
            {"order_id": 101, "part_id": 5, "missing_quantity": 2},
            {"order_id": 104, "part_id": 7, "missing_quantity": 5},
            ...
        ],
        "total_missing_quantity": 8
    }
    """
    # TODO: Implement this function
    pass


def main():
    """
    Main function to test your implementation
    
    Sample data is loaded from the files 'orderstest.json' and 'inventorytest.json'
    Your implementation should work with these files.
    """
    # Ensure the test files exist
    orders_file = "orderstest.json"
    inventory_file = "inventorytest.json"
    
    if not os.path.exists(orders_file):
        print(f"ERROR: {orders_file} not found!")
        print("Please create this file with the following contents:")
        print("""
{
    "orders": [
        {"order_id": 101, "part_id": 5, "quantity_ordered": 10, "status": "pending"},
        {"order_id": 102, "part_id": 8, "quantity_ordered": 5, "status": "shipped"},
        {"order_id": 103, "part_id": 5, "quantity_ordered": 2, "status": "pending"},
        {"order_id": 104, "part_id": 7, "quantity_ordered": 15, "status": "pending"},
        {"order_id": 105, "part_id": 6, "quantity_ordered": 20, "status": "shipped"},
        {"order_id": 106, "part_id": 8, "quantity_ordered": 4, "status": "pending"}
    ]
}""")
        return

    if not os.path.exists(inventory_file):
        print(f"ERROR: {inventory_file} not found!")
        print("Please create this file with the following contents:")
        print("""
{
    "inventory": [
        {"part_id": 5, "quantity_available": 8},
        {"part_id": 8, "quantity_available": 3},
        {"part_id": 7, "quantity_available": 10},
        {"part_id": 6, "quantity_available": 25}
    ]
}""")
        return
    
    # Call your implementation
    try:
        result = process_supply_chain_data(orders_file, inventory_file)
        print("Result:")
        print(json.dumps(result, indent=4))
        
        # Expected output
        print("\nExpected output:")
        expected = {
            "unfulfilled_orders": [
                {"order_id": 101, "part_id": 5, "missing_quantity": 2},
                {"order_id": 104, "part_id": 7, "missing_quantity": 5},
                {"order_id": 106, "part_id": 8, "missing_quantity": 1}
            ],
            "total_missing_quantity": 8
        }
        print(json.dumps(expected, indent=4))
    except Exception as e:
        print(f"Error in your implementation: {e}")


if __name__ == "__main__":
    main()
