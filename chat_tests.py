import requests


class ChatAPITests:
    def __init__(self, base_url):
        self.base_url = base_url

    def print_response(self, response):
        print(f"Status Code: {response.status_code}, Response: {response.text}")

    def test_get_chat(self, room):
        response = requests.get(f"{self.base_url}/api/chat/{room}")
        self.print_response(response)

    def test_post_chat(self, room, username, message):
        data = {'username': username, 'msg': message}
        response = requests.post(f"{self.base_url}/api/chat/{room}", data=data)
        self.print_response(response)

    def run_tests(self):
        print("Running GET tests...")
        self.test_get_chat("general")  # Existing room
        self.test_get_chat("unknown")  # Non-existing room

        print("Running POST tests...")
        self.test_post_chat("general", "Alice", "Hello World!")  # Valid post
        self.test_post_chat("general", "", "")  # Empty fields
        self.test_post_chat("general", None, None)  # Missing fields (should handle edge cases in actual function)

if __name__ == '__main__':
    tests = ChatAPITests("http://127.0.0.1:5000")
    tests.run_tests()