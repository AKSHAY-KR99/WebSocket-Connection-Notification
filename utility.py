# 0-2022/0001
def push_notification(group, message_obj):
    channel_layer = get_channel_layer()
    print(group)
    async_to_sync(channel_layer.group_send)(
        'notification_'+group, {
            "type": "notification_message",
            "message": json.dumps(message_obj)
        }
    )
  
