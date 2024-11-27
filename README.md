# DingTalkITRobot
**借助钉钉机器人@指定用户组**  
当机器人被@时，机器人@指定用户组  
A Dingtalk Robot used to @ specific users when the bot is @.  

* 运行方法  
  带参数 Client ID 和参数 Client Secret 运行 bot_actions/at_users_and_leave_message.py（Client ID 和 Client Secret 为机器人应用的应用凭证，可在机器人的“应用信息”查看）  
  `python3 ./at_users_and_leave_message.py --client_id="your-client-id" --client_secret="your-client-secret`
  
* 本仓库信息
  * [bot_actions/at_users_and_leave_message.py](bot_actions/at_users_and_leave_message.py) 为Stream Mode下开发的机器人服务，实现了当机器人被@时，留下“<某用户>需要帮助，提示相关用户”的信息（<某用户>为@机器人的用户的昵称），并@指定用户组。
  * [robot_response.py](robot_response.py) 为Webhook模式下开发的机器人服务，实现了回复“机器人被@了，相关用户被提醒！”，并@指定用户组。但无法实时响应，仅能通过模拟消息测试。

* 创建机器人
  * [Stream Mode](https://opensource.dingtalk.com/developerpedia/docs/learn/stream/overview/) 为钉钉在2023年全新推出的数据交互形式，可以极大的减轻应用开发和运维的负担。为使用Stream模式，需[创建一个机器人应用](https://opensource.dingtalk.com/developerpedia/docs/explore/tutorials/stream/bot/python/create-bot)，即先在开发平台创建应用，再在应用中创建机器人。
  * 从群聊中直接[创建自定义机器人](https://open.dingtalk.com/document/orgapp/custom-bot-creation-and-installation)  可支持Webhook模式的开发，但不支持Stream模式，同时需注意，此类跟应用并列的“机器人”将逐渐退出历史舞台。
