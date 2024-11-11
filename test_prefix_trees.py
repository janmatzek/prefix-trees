from prefix_trees import add_contact, search_contact


def test_name_not_in_db():
    assert search_contact("Anthony") == []


def test_search_existing_name():
    assert search_contact("Alexander") == ["478-392-5907"]


def test_search_existing_name_lowercase():
    assert search_contact("alexander") == ["478-392-5907"]


def test_returns_multiple_numbers():
    # returns a numbers of Alec, Alex, Alexander
    assert len(search_contact("Ale")) == 3


def test_add_new_contact():
    assert add_contact("Anthony", "123-456-7890")


def test_add_existing_contact():
    assert not add_contact("Alex", "123-456-7890")
