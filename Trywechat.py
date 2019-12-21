import itchat
import time
@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print(msg['User']['NickName'])
    print("says:",msg.text)
    itchat.send_msg(msg['User']['NickName'] + "说："+ msg.text, user_name)

if __name__ == '__main__':
    itchat.auto_login()
    user_info = itchat.search_friends(name='小明')
    user_name = user_info[0]['UserName']
    itchat.send_msg('登录成功 开始转发', user_name)
    itchat.run()

# change 小明 to the account name that you wish to forward to
# 把 小明 改成你要发去的微信号的名字

# run 
#pip install itchat 
#in cmd if itchat has not been installed
