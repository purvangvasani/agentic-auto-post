# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# def post_to_linkedin(text):
#     token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    
#     # Step 1: Get your LinkedIn user URN
#     profile_res = requests.get(
#         "https://api.linkedin.com/v2/me",
#         headers={"Authorization": f"Bearer {token}"}
#     )
#     print(profile_res.json())
#     user_urn = profile_res.json().get("id")

#     if not user_urn:
#         print("❌ Failed to get user ID")
#         return

#     author_urn = f"urn:li:person:{user_urn}"

#     # Step 2: Create a post
#     post_data = {
#         "author": author_urn,
#         "lifecycleState": "PUBLISHED",
#         "specificContent": {
#             "com.linkedin.ugc.ShareContent": {
#                 "shareCommentary": {"text": text},
#                 "shareMediaCategory": "NONE"
#             }
#         },
#         "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
#     }

#     res = requests.post(
#         "https://api.linkedin.com/v2/ugcPosts",
#         headers={
#             "Authorization": f"Bearer {token}",
#             "Content-Type": "application/json",
#             "X-Restli-Protocol-Version": "2.0.0"
#         },
#         json=post_data
#     )

#     if res.status_code == 201:
#         print("✅ Post successfully published on LinkedIn.")
#     else:
#         print(f"❌ Failed to post: {res.status_code} - {res.text}")
    # }

    # res = requests.post(
    #     "https://api.linkedin.com/v2/ugcPosts",
    #     headers={
    #         "Authorization": f"Bearer {token}",
    #         "Content-Type": "application/json",
    #         "X-Restli-Protocol-Version": "2.0.0"
    #     },
    #     json=post_data
    # )

    # if res.status_code == 201:
    #     print("✅ Post successfully published on LinkedIn.")
    # else:
    #     print(f"❌ Failed to post: {res.status_code} - {res.text}")
    # }

    # res = requests.post(
    #     "https://api.linkedin.com/v2/ugcPosts",
    #     headers={
    #         "Authorization": f"Bearer {token}",
    #         "Content-Type": "application/json",
    #         "X-Restli-Protocol-Version": "2.0.0"
    #     },
    #     json=post_data
    # )

    # if res.status_code == 201:
    #     print("✅ Post successfully published on LinkedIn.")
    # else:
    #     print(f"❌ Failed to post: {res.status_code} - {res.text}")
    # }

    # res = requests.post(
    #     "https://api.linkedin.com/v2/ugcPosts",
    #     headers={
    #         "Authorization": f"Bearer {token}",
    #         "Content-Type": "application/json",
    #         "X-Restli-Protocol-Version": "2.0.0"
    #     },
    #     json=post_data
    # )

    # if res.status_code == 201:
    #     print("✅ Post successfully published on LinkedIn.")
    # else:
    #     print(f"❌ Failed to post: {res.status_code} - {res.text}")
    # }

    # res = requests.post(
    #     "https://api.linkedin.com/v2/ugcPosts",
    #     headers={
    #         "Authorization": f"Bearer {token}",
    #         "Content-Type": "application/json",
    #         "X-Restli-Protocol-Version": "2.0.0"
    #     },
    #     json=post_data
    # )

    # if res.status_code == 201:
    #     print("✅ Post successfully published on LinkedIn.")
    # else:
    #     print(f"❌ Failed to post: {res.status_code} - {res.text}")



import os
import requests
from dotenv import load_dotenv

load_dotenv()

def post_to_linkedin(text):
    token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    if not token:
        print("❌ No access token found in environment variables")
        return

    # Step 1: Get your LinkedIn user info
    profile_res = requests.get(
        "https://api.linkedin.com/v2/userinfo",
        headers={"Authorization": f"Bearer {token}"}
    )

    # Check for errors
    if profile_res.status_code != 200:
        print(f"❌ Failed to get user info: {profile_res.status_code} - {profile_res.text}")
        return

    user_info = profile_res.json()
    print("User Info:", user_info)

    # Extract the 'sub' field as the user ID
    user_id = user_info.get("sub")
    if not user_id:
        print("❌ Failed to get user ID from 'sub' field")
        return

    # Construct the author URN (assuming 'sub' is the person ID)
    author_urn = f"urn:li:person:{user_id}"

    # Step 2: Create a post
    post_data = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    res = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        },
        json=post_data
    )

    if res.status_code == 201:
        print("✅ Post successfully published on LinkedIn.")
    else:
        print(f"❌ Failed to post: {res.status_code} - {res.text}")
