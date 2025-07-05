import os
import json
import firebase_admin
from firebase_admin import credentials, messaging
from django.conf import settings

# ✅ Use Firebase service account from environment variable
firebase_json = os.environ.get('FIREBASE_CREDENTIALS_JSON')

if firebase_json and not firebase_admin._apps:
    try:
        cred = credentials.Certificate(json.loads(firebase_json))
        firebase_admin.initialize_app(cred)
    except Exception as e:
        print("Firebase initialization error:", e)

def send_fcm_notification(user, title, message):
    from .models import FCMToken

    try:
        token_obj = FCMToken.objects.get(user=user)
        message_obj = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=message,
            ),
            token=token_obj.token,
        )
        response = messaging.send(message_obj)
        print("Notification sent successfully:", response)

    except FCMToken.DoesNotExist:
        print("FCM Token not found for user:", user)
    except Exception as e:
        print("Error sending notification:", e)


def send_fcm_notifications_to_tokens(tokens, title, message):
    # tokens: list of device tokens (strings)
    if not tokens:
        return
    
    message_obj = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=message,
        ),
        tokens=tokens,
    )
    response = messaging.send_multicast(message_obj)
    print(f"Multicast notifications sent: {response.success_count} successful, {response.failure_count} failed")
    if response.failure_count > 0:
        for resp in response.responses:
            if not resp.success:
                print("Failed to send notification:", resp.exception)
