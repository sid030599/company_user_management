def allocate_boxes(time, capacity, costs):
    """
    Allocate ice boxes to minimize cost.

    Args:
        time (int): Hours the boxes are needed for.
        capacity (int): Total capacity required in units.
        costs (dict): A dictionary where keys are regions and values are lists of tuples (box type, volume, cost).

    Returns:
        dict: Optimal allocation for each region with total cost and selected boxes.
    """
    result = []

    for region, box_data in costs.items():
        # Sort by cost-efficiency (cost per unit volume)
        box_data.sort(key=lambda x: x[2] / x[1])

        remaining_capacity = capacity
        total_cost = 0
        selected_boxes = []

        for box_type, volume, cost in box_data:
            if remaining_capacity <= 0:
                break

            num_boxes = remaining_capacity // volume

            if num_boxes > 0:
                selected_boxes.append((box_type, num_boxes))
                total_cost += num_boxes * cost * time
                remaining_capacity -= num_boxes * volume

        # If there's still capacity left, consider partial allocation
        if remaining_capacity > 0:
            for box_type, volume, cost in box_data:
                if remaining_capacity <= 0:
                    break
                if remaining_capacity < volume:
                    selected_boxes.append((box_type, 1))
                    total_cost += cost * time
                    remaining_capacity = 0

        result.append(
            {"region": region, "total_cost": total_cost, "boxes": selected_boxes}
        )

    return {"Output": result}


# Example input
costs_data = {
    "Delhi": [
        ("XS", 10, 12),
        ("S", 20, 23),
        ("M", 40, 45),
        ("L", 80, 77.4),
        ("XL", 160, 140),
        ("XXL", 320, 282),
    ],
    "Mumbai": [
        ("XS", 10, 14),
        ("S", 20, 20),
        ("M", 40, 41.3),
        ("L", 80, 89),
        ("XL", 160, 130),
        ("XXL", 320, 297),
    ],
    "Kolkata": [
        ("XS", 10, 11),
        ("S", 20, 20),
        ("M", 40, 41.3),
        ("L", 80, 67),
        ("XL", 160, 118),
        ("XXL", 320, 297),
    ],
}

# Example test case
capacity_needed = 1150
time_needed = 1

output = allocate_boxes(time_needed, capacity_needed, costs_data)
print("Test Case 1:", output)

# Test Case 1
capacity_needed = 800
output = allocate_boxes(time_needed, capacity_needed, costs_data)
print("Test Case 2:", output)

# Test Case 2
capacity_needed = 500
output = allocate_boxes(time_needed, capacity_needed, costs_data)
print("Test Case 3:", output)

# Test Case 3
capacity_needed = 2500
time_needed = 2
output = allocate_boxes(time_needed, capacity_needed, costs_data)
print("Test Case 4:", output)

# Test Case 4
capacity_needed = 320
time_needed = 3
output = allocate_boxes(time_needed, capacity_needed, costs_data)
print("Test Case 5:", output)

# output of test cases:
# Test Case 1: {'Output': [{'region': 'Delhi', 'total_cost': 1015, 'boxes': [('XL', 7), ('S', 1), ('XS', 1)]}, {'region': 'Mumbai', 'total_cost': 944, 'boxes': [('XL', 7), ('S', 1), ('XS', 1)]}, {'region': 'Kolkata', 'total_cost': 857, 'boxes': [('XL', 7), ('S', 1), ('XS', 1)]}]}
# Test Case 2: {'Output': [{'region': 'Delhi', 'total_cost': 700, 'boxes': [('XL', 5)]}, {'region': 'Mumbai', 'total_cost': 650, 'boxes': [('XL', 5)]}, {'region': 'Kolkata', 'total_cost': 590, 'boxes': [('XL', 5)]}]}
# Test Case 3: {'Output': [{'region': 'Delhi', 'total_cost': 443, 'boxes': [('XL', 3), ('S', 1)]}, {'region': 'Mumbai', 'total_cost': 410, 'boxes': [('XL', 3), ('S', 1)]}, {'region': 'Kolkata', 'total_cost': 374, 'boxes': [('XL', 3), ('S', 1)]}]}
# Test Case 4: {'Output': [{'region': 'Delhi', 'total_cost': 4400.8, 'boxes': [('XL', 15), ('L', 1), ('S', 1)]}, {'region': 'Mumbai', 'total_cost': 4100, 'boxes': [('XL', 15), ('S', 5)]}, {'region': 'Kolkata', 'total_cost': 3714, 'boxes': [('XL', 15), ('L', 1), ('S', 1)]}]}
# Test Case 5: {'Output': [{'region': 'Delhi', 'total_cost': 840, 'boxes': [('XL', 2)]}, {'region': 'Mumbai', 'total_cost': 780, 'boxes': [('XL', 2)]}, {'region': 'Kolkata', 'total_cost': 708, 'boxes': [('XL', 2)]}]}
