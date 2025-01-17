import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item

# @pytest.mark.skip
def test_best_by_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Decor(condition=5.0)
    item_e = Clothing(condition=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

# @pytest.mark.skip
def test_best_by_category_no_matches_is_none():
    item_a = Decor(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_category("Electronics")

    assert best_item is None

# @pytest.mark.skip
def test_best_by_category_with_duplicates():
    # Arrange
    item_a = Clothing(condition=2.0)
    item_b = Clothing(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_best_by_category("Clothing")

    # Assert
    assert best_item.category == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

# @pytest.mark.skip
def test_swap_best_by_category():
    # Arrange
    # me
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    actual_length_tai = len(tai.inventory)

    # them
    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    actual_length_jesse = len(jesse.inventory)

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

#     raise Exception("Complete this test according to comments below.")
#     # *********************************************************************
#     # ****** Complete Assert Portion of this test **********
#     # *********************************************************************
#     # Assertions should check:
#     # - That the results is truthy
#     # - That tai and jesse's inventories are the correct length
#     # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
    
    # Assert
    assert result == True
    expected_length_tai = len(tai.inventory)
    assert expected_length_tai == actual_length_tai

    expected_length_jesse = len(jesse.inventory)
    assert expected_length_jesse == actual_length_jesse

    assert (item_f in tai.inventory) == True
    assert (item_c not in tai.inventory) == True 
    assert (item_c in jesse.inventory) == True
    assert (item_f not in jesse.inventory) == True 




    

# @pytest.mark.skip
def test_swap_best_by_category_reordered():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )
    actual_length_tai = len(tai.inventory)

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )
    actual_length_jesse = len(jesse.inventory)

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # Assert
    assert result == True
    expected_length_tai = len(tai.inventory)
    assert expected_length_tai == actual_length_tai

    expected_length_jesse = len(jesse.inventory)
    assert expected_length_jesse == actual_length_jesse

    assert (item_f in tai.inventory) == True
    assert (item_c not in tai.inventory) == True 
    assert (item_c in jesse.inventory) == True
    assert (item_f not in jesse.inventory) == True 

#     raise Exception("Complete this test according to comments below.")
#     # *********************************************************************
#     # ****** Complete Assert Portion of this test **********
#     # *********************************************************************
#     # Assertions should check:
#     # - That result is truthy
#     # - That tai and jesse's inventories are the correct length
#     # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there

# @pytest.mark.skip
def test_swap_best_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    actual_length_tai = len(tai.inventory)

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    actual_length_jesse = len(jesse.inventory)

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    # Assert
    assert result == False
    expected_length_tai = len(tai.inventory)
    assert expected_length_tai == actual_length_tai

    expected_length_jesse = len(jesse.inventory)
    assert expected_length_jesse == actual_length_jesse

    assert (item_a in tai.inventory) == True
    assert (item_b in tai.inventory) == True 
    assert (item_c in tai.inventory) == True 
    assert (item_d in jesse.inventory) == True
    assert (item_e in jesse.inventory) == True
    assert (item_f in jesse.inventory) == True 

#     raise Exception("Complete this test according to comments below.")
#     # *********************************************************************
#     # ****** Complete Assert Portion of this test **********
#     # *********************************************************************
#     # Assertions should check:
#     # - That result is falsy
#     # - That tai and jesse's inventories are the correct length
#     # - That all the correct items are in tai and jesse's inventories

# @pytest.mark.skip
def test_swap_best_by_category_no_other_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )
    actual_length_tai = len(tai.inventory)

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )
    actual_length_jesse = len(jesse.inventory)

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    # Assert
    assert result == False
    expected_length_tai = len(tai.inventory)
    assert expected_length_tai == actual_length_tai

    expected_length_jesse = len(jesse.inventory)
    assert expected_length_jesse == actual_length_jesse

    assert (item_a in tai.inventory) == True
    assert (item_b in tai.inventory) == True 
    assert (item_c in tai.inventory) == True 
    assert (item_d in jesse.inventory) == True
    assert (item_e in jesse.inventory) == True
    assert (item_f in jesse.inventory) == True 

#     raise Exception("Complete this test according to comments below.")
#     # *********************************************************************
#     # ****** Complete Assert Portion of this test **********
#     # *********************************************************************
#     # Assertions should check:
#     # - That result is falsy
#     # - That tai and jesse's inventories are the correct length
#     # - That all the correct items are in tai and jesse's inventories

# Optional enhancement 
# @pytest.mark.skip
def test_swap_by_newest_returns_True():
    # Arrange
    item_a = Item(age = 5)
    item_b = Item(age = 1)
    item_c = Item(age = 13)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age = 6)
    item_e = Item(age = 2) 
    jolie = Vendor(
        inventory=[item_d, item_e]
    )
    # Act

    result = fatimah.swap_items(jolie, item_b, item_e)

    # Assert

    assert len(fatimah.inventory) == 3
    assert item_b not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_e in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_e not in jolie.inventory
    assert item_d in jolie.inventory
    assert item_b in jolie.inventory
    assert result

    
