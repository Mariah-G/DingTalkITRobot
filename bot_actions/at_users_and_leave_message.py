import argparse
import logging
from dingtalk_stream import AckMessage
import dingtalk_stream


def setup_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('%(asctime)s %(name)-8s %(levelname)-8s %(message)s [%(filename)s:%(lineno)d]'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


#通过命令行参数读取 Client ID 和 Client Secret 选项
def define_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--client_id', dest='client_id', required=True,
        help='app_key or suite_key from https://open-dev.digntalk.com'
    )
    parser.add_argument(
        '--client_secret', dest='client_secret', required=True,
        help='app_secret or suite_secret from https://open-dev.digntalk.com'
    )
    options = parser.parse_args()
    return options


#通过 Client ID 和 Client Secret 创建 Stream Client
class EchoTextHandler(dingtalk_stream.ChatbotHandler):
    def __init__(self, logger: logging.Logger = None):
        super(dingtalk_stream.ChatbotHandler, self).__init__()
        if logger:
            self.logger = logger

    #在 Stream Client 中注册机器人消息回调方法，实现消息接收能力
    async def process(self, callback: dingtalk_stream.CallbackMessage):
        #在消息回调方法中，简单 echo 机器人消息回去，实现消息发送(回复)能力
        incoming_message = dingtalk_stream.ChatbotMessage.from_dict(callback.data)
        text = incoming_message.sender_nick.strip()+'需要帮助，提示相关用户'
        outgoing_message = incoming_message
        outgoing_message.at_users = [''] #填写需要@的用户的手机号，如["13800000000", "13900000000"]
        self.reply_text(text, outgoing_message)
        return AckMessage.STATUS_OK, 'OK'

def main():
    logger = setup_logger()
    options = define_options()

    credential = dingtalk_stream.Credential(options.client_id, options.client_secret)
    client = dingtalk_stream.DingTalkStreamClient(credential)
    client.register_callback_handler(dingtalk_stream.chatbot.ChatbotMessage.TOPIC, EchoTextHandler(logger))
    client.start_forever()


if __name__ == '__main__':
    main()