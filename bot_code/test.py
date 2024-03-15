import unittest
from unittest.mock import Mock
from bot import start, end_message_handler

class TestHandlers(unittest.TestCase):

  def test_start_message_handler_initial(self):
    message_mock = Mock()
    bot_mock = Mock()
    message_mock.chat.id = 12345 
    bot_mock.send_message.return_value = None

    # Call the start message handler
    start(message_mock, bot_mock)

    # Assert that send_message was called with the correct parameters
    bot_mock.send_message.assert_called_once_with(
        message_mock.chat.id,
        "Hi there. What can I help you with?",
        reply_markup=None  # No custom keyboard expected
        )
  
  def test_start_message_handler_final(self):
    message_mock = Mock()
    bot_mock = Mock()
    message_mock.chat.id = 12345
    bot_mock.send_message.return_value = None #we don't actually want to send anything 

    end_message_handler(message_mock, bot_mock)

    bot_mock.send_message.assert_called_once_with(
      message_mock.chat.id, 
      'Goodbye. Have a great day!',
      reply_markup = None

    )
if __name__ == '__main__': 
  unittest.main()
