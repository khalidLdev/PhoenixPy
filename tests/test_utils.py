from feathers.utils import formater_message

def test_formater_message():
    assert formater_message("Test") == "🪄 Test 🪄"